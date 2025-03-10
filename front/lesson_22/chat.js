const apiKey = 'sk-or-vv-32acad84830483432df6bb1eb3114ede486fe620ba237c07f152b84c6a27e782';
const apiUrl = 'https://api.vsegpt.ru/v1/chat/completions';

// 'openai/gpt-4o-mini'
// 'anthropic/claude-3-5-haiku'
const modelAI = 'anthropic/claude-3-5-haiku'; 
const chatHistory = [];
const systemPrompt = 'Ты асистент-помощник. Ты отвечаешь на вопросы пользователя на русском языке. Великолепно знаешь русский. Ты отвечаешь лаконично, если тебя не попросят об ином.';

// Основные элементы DOM
const chatMessages = document.getElementById('chat-messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const maxTokens = 200;
const temperature = 0.7;

// Универсальная функция для текстовых запросов.
// Принимает пользовательский запрос и модель. Возвращает ответ сервера. и пополняет историю чата (которая лежит в chatHistory)
async function makeRequest(userPrompt, model = modelAI) {
    // Добавляем системный промпт в начало истории, если история пуста
    if (chatHistory.length === 0) {
        chatHistory.push({
            role: 'system',
            content: systemPrompt
        });
    }

    // Добавляем запрос пользователя в историю
    chatHistory.push({
        role: 'user',
        content: userPrompt
    });

    // Формируем тело запроса
    const requestBody = {
        model: model,
        messages: chatHistory,
        temperature: temperature,
        // Для gpt4o серии это 16000
        // Для claude haiku 3.5 это 8100
        max_tokens: maxTokens,
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        
        // Добавляем ответ ассистента в историю
        if (data.choices && data.choices[0].message) {
            chatHistory.push(data.choices[0].message);
        }
        console.log(data.choices[0].message.content);
        return data.choices[0].message.content;
    } catch (error) {
        console.error('Ошибка при выполнении запроса:', error);
        throw error;
    }
}



// Функция создания сообщения в чате
function createMessageElement(content, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', isUser ? 'user-message' : 'ai-message');
    
    if (isUser) {
        messageDiv.textContent = content;
    } else {
        // Для сообщений ИИ используем marked для парсинга MD
        messageDiv.innerHTML = marked.parse(content);
        // Подсвечиваем код во всех code-блоках
        messageDiv.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightElement(block);
        });
    }
    
    return messageDiv;
}


// Функция добавления сообщения в чат
function addMessageToChat(content, isUser) {
    const messageElement = createMessageElement(content, isUser);
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Если это сообщение от ИИ, добавляем кнопки копирования
    if (!isUser) {
        addCodeCopyButtons(messageElement);
    }
}

// Функция обработки отправки формы
async function handleSubmit(event) {
    event.preventDefault();
    
    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    // Добавляем сообщение пользователя
    addMessageToChat(userMessage, true);
    userInput.value = '';

    try {
        // Получаем ответ от ИИ
        const aiResponse = await makeRequest(userMessage);
        // Добавляем ответ ИИ
        addMessageToChat(aiResponse, false);
    } catch (error) {
        addMessageToChat('Произошла ошибка при получении ответа', false);
        console.error('Ошибка:', error);
    }
}

// Инициализация обработчиков событий
function initChat() {
    chatForm.addEventListener('submit', handleSubmit);
    userInput.focus();
}


function addCodeCopyButtons(container) {
    container.querySelectorAll("pre").forEach((preBlock) => {
        preBlock.classList.add("pre-container");
        const copyButton = createCopyButton();
        preBlock.appendChild(copyButton);
        copyButton.addEventListener(
            "click",
            handleCopyButtonClick.bind(null, preBlock, copyButton)
        );
    });
}

function createCopyButton() {
    const btn = document.createElement("i");
    btn.classList.add("bi", "bi-clipboard", "code-copy-btn");
    return btn;
}

function handleCopyButtonClick(preBlock, copyButton) {
    const codeContent = preBlock.querySelector("code").innerText;
    navigator.clipboard.writeText(codeContent).then(() => {
        toggleCopyIcon(copyButton, true);
        setTimeout(() => toggleCopyIcon(copyButton, false), 3000);
    });
}

function toggleCopyIcon(copyButton, copied) {
    copyButton.classList.toggle("bi-clipboard", !copied);
    copyButton.classList.toggle("bi-clipboard-check", copied);
    copyButton.style.color = copied ? "lightgreen" : "white";
}


// Запуск чата
initChat();



