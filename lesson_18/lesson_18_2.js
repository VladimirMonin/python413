const events = [
    {
      name: "click",
      category: "Мышь",
      description: "Событие `click` срабатывает при клике на элемент. Оно часто используется для обработки нажатий кнопок и ссылок. Это одно из наиболее часто используемых событий в веб-разработке."
    },
    {
      name: "dblclick",
      category: "Мышь",
      description: "Событие `dblclick` возникает при двойном клике на элемент. Обычно используется для выполнения действий, требующих подтверждения пользователя. Например, открытие элемента для редактирования."
    },
    {
      name: "mousedown",
      category: "Мышь",
      description: "Событие `mousedown` срабатывает, когда кнопка мыши нажата над элементом. Это событие может быть использовано для начала перетаскивания или других интерактивных действий."
    },
    {
      name: "mouseup",
      category: "Мышь",
      description: "Событие `mouseup` возникает, когда кнопка мыши отпускается над элементом. Часто используется в сочетании с `mousedown` для реализации сложных взаимодействий."
    },
    {
      name: "mouseover",
      category: "Мышь",
      description: "Событие `mouseover` срабатывает, когда курсор мыши наводится на элемент. Используется для создания всплывающих подсказок или изменения стилей при наведении."
    },
    {
      name: "mousemove",
      category: "Мышь",
      description: "Событие `mousemove` возникает при движении курсора мыши над элементом. Может использоваться для отслеживания положения курсора или создания эффектов."
    },
    {
      name: "mouseout",
      category: "Мышь",
      description: "Событие `mouseout` происходит, когда курсор мыши покидает элемент. Часто используется для отмены изменений, внесенных при наведении курсора."
    },
    {
      name: "keydown",
      category: "Клавиатура",
      description: "Событие `keydown` срабатывает при нажатии клавиши на клавиатуре. Используется для обработки горячих клавиш и навигации с клавиатуры."
    },
    {
      name: "keyup",
      category: "Клавиатура",
      description: "Событие `keyup` возникает при отпускании клавиши на клавиатуре. Часто используется для валидации ввода и обновления интерфейса после ввода."
    },
    {
      name: "keypress",
      category: "Клавиатура",
      description: "Событие `keypress` срабатывает при нажатии клавиши, которая генерирует символ. Используется для обработки текстового ввода и предотвращения определенных символов."
    },
    {
      name: "submit",
      category: "Форма",
      description: "Событие `submit` возникает при отправке формы. Используется для валидации данных перед отправкой и предотвращения стандартного поведения браузера."
    },
    {
      name: "change",
      category: "Форма",
      description: "Событие `change` срабатывает при изменении значения элемента формы. Часто используется для обновления данных в режиме реального времени или выполнения зависимых действий."
    },
    {
      name: "focus",
      category: "Форма",
      description: "Событие `focus` возникает, когда элемент получает фокус. Используется для выделения поля ввода или отображения дополнительных подсказок."
    },
    {
      name: "blur",
      category: "Форма",
      description: "Событие `blur` происходит, когда элемент теряет фокус. Часто используется для валидации данных или сохранения изменений."
    },
    {
      name: "input",
      category: "Форма",
      description: "Событие `input` срабатывает при каждом изменении значения элемента ввода. Используется для создания динамических интерфейсов и быстрого реагирования на ввод пользователя."
    },
    {
      name: "load",
      category: "Документ",
      description: "Событие `load` происходит, когда вся страница и все связанные ресурсы полностью загрузились. Используется для инициализации скриптов после полной загрузки страницы."
    },
    {
      name: "unload",
      category: "Документ",
      description: "Событие `unload` возникает, когда пользователь покидает страницу. Используется для очистки ресурсов или сохранения состояния перед выходом."
    },
    {
      name: "resize",
      category: "Документ",
      description: "Событие `resize` срабатывает при изменении размера окна браузера. Используется для адаптации макета страницы и оптимизации отображения контента."
    },
    {
      name: "scroll",
      category: "Документ",
      description: "Событие `scroll` происходит при прокрутке содержимого элемента или страницы. Часто используется для подгрузки контента по мере прокрутки или создания эффектов параллакса."
    },
    {
      name: "error",
      category: "Документ",
      description: "Событие `error` возникает при загрузке ресурсов, если происходит ошибка. Используется для обработки ошибок загрузки изображений, скриптов и других ресурсов."
    },
    {
      name: "select",
      category: "Форма",
      description: "Событие `select` срабатывает при выборе текста в текстовом поле или textarea. Используется для реализации функционала копирования или форматирования выделенного текста."
    },
    {
      name: "contextmenu",
      category: "Мышь",
      description: "Событие `contextmenu` происходит при открытии контекстного меню, обычно правым кликом мыши. Используется для создания кастомных меню или предотвращения стандартного поведения."
    },
    {
      name: "copy",
      category: "Документ",
      description: "Событие `copy` срабатывает при попытке копирования содержимого. Используется для модификации данных при копировании или отслеживания действий пользователя."
    },
    {
      name: "paste",
      category: "Документ",
      description: "Событие `paste` возникает при вставке данных из буфера обмена. Используется для валидации или фильтрации вставляемого содержимого."
    },
    {
      name: "drag",
      category: "Мышь",
      description: "Событие `drag` происходит при перетаскивании элементов. Используется для реализации интерфейсов перетаскивания и сортировки элементов."
    },
    {
      name: "drop",
      category: "Мышь",
      description: "Событие `drop` срабатывает, когда перетаскиваемый элемент отпускается над целевым элементом. Используется для обработки данных, перетаскиваемых пользователем."
    },
    {
      name: "touchstart",
      category: "Мобильные устройства",
      description: "Событие `touchstart` возникает при касании экрана. Используется для обработки жестов и интерактивных действий на мобильных устройствах."
    },
    {
      name: "touchend",
      category: "Мобильные устройства",
      description: "Событие `touchend` происходит, когда палец отпускается с экрана. Часто используется в сочетании с `touchstart` для распознавания сложных жестов."
    },
    {
      name: "wheel",
      category: "Мышь",
      description: "Событие `wheel` срабатывает при прокрутке колесика мыши. Используется для реализации собственных механизмов прокрутки или масштабирования контента."
    },
    {
      name: "beforeunload",
      category: "Документ",
      description: "Событие `beforeunload` возникает перед выгрузкой страницы. Используется для предупреждения пользователя о несохраненных изменениях или для выполнения окончательных действий."
    },
    {
      name: "storage",
      category: "Документ",
      description: "Событие `storage` срабатывает при изменении данных в `localStorage` или `sessionStorage`. Используется для синхронизации данных между вкладками или окнами."
    },
    {
      name: "animationstart",
      category: "Анимация",
      description: "Событие `animationstart` происходит при начале CSS-анимации. Используется для отслеживания анимационных эффектов и выполнения действий при их старте."
    },
    {
      name: "animationend",
      category: "Анимация",
      description: "Событие `animationend` срабатывает по завершении CSS-анимации. Часто используется для выполнения действий после завершения анимации."
    },
    {
      name: "transitionend",
      category: "Анимация",
      description: "Событие `transitionend` возникает по завершении CSS-перехода. Используется для синхронизации изменений стилей и выполнения последовательных действий."
    },
    {
      name: "copy",
      category: "Документ",
      description: "Событие `copy` срабатывает при копировании текста или данных. Используется для модификации содержимого перед копированием или для аналитики действий пользователя."
    }
  ];
  const table = document.getElementById('table');
  const inputMethod = document.getElementById('inputMethod');

  // Функция для отрисовки таблиы. Принемает массив объектов и заголовки таблицы в виде массива строк

  function renderTable(data, headers) {
    // Очищаем содержимое таблицы перед новым рендером
    table.innerHTML = ''; 
    // Создаем заголовок таблицы
    const tableHead = document.createElement('thead');
  
    // В цикле идем по headers и создаем th внутрь tableHead
    headers.forEach(header => {
      const th = document.createElement('th');
      th.textContent = header;
      tableHead.appendChild(th);
    });

    // Добавляем заголовок таблицы в таблицу
    table.appendChild(tableHead);

    // Создаем тело таблицы
    const tableBody = document.createElement('tbody');

    // Обходим цикл по data и создаем строку таблицы в которую создаем ячейки td и наполняем их данными из объекта
    data.forEach(item => {
      const row = document.createElement('tr');
      // Создаем и наполняем ячейку с названием события
      td1 = document.createElement('td');
      td1.textContent = item.name;
      // Создаем и наполняем ячейку с категорией события
      td2 = document.createElement('td');
      td2.textContent = item.category;
      // Создаем и наполняем ячейку с описанием события
      td3 = document.createElement('td');
      td3.textContent = item.description;

      // Добавляем все ячейки в строку
      row.appendChild(td1);
      row.appendChild(td2);
      row.appendChild(td3);
      tableBody.appendChild(row);
      });

      // Добавляем тело таблицы в таблицу
      table.appendChild(tableBody);
  }

  // Инициализация таблицы при загрузке страницы с полным набором данных
  document.addEventListener('DOMContentLoaded', () => {
      renderTable(events, ['Название', 'Категория', 'Описание']);
  });

  // Функция фильтрации таблицы. Принимает массив объектов и строку поиска
  // Приводит к нижнему регистру и то и другое и проверяет на вхождение подстроки в строку через метод includes
  function filterTable(data, searchTerm) {
      // Фильтруем данные по всем полям объекта
      const filteredData = data.filter(item => {
          const name = item.name.toLowerCase();
          const category = item.category.toLowerCase();
          const description = item.description.toLowerCase();
          const search = searchTerm.toLowerCase();

          // Проверяем наличие поискового запроса в любом из полей
          return name.includes(search) || 
               category.includes(search) || 
               description.includes(search);
      });
    
      return filteredData;
  }

  // Обработка ввода в поле поиска и обновление таблицы отфильтрованными данными
  inputMethod.addEventListener('input', (e) => {
      // Получаем значение из поля ввода
      const searchTerm = e.target.value;
      // Фильтруем массив событий по введенному значению
      const filteredEvents = filterTable(events, searchTerm);
      // Перерисовываем таблицу с отфильтрованными данными
      renderTable(filteredEvents, ['Название', 'Категория', 'Описание']);
  });