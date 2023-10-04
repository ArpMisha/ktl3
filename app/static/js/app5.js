document.addEventListener("DOMContentLoaded", function () {
    // Находим форму по её ID
    const form = document.getElementById("task-form");
    // Добавляем обработчик события отправки формы
    form.addEventListener("submit", function (e) {
    e.preventDefault(); // Предотвращаем стандартное действие формы (отправку на сервер)
    // Получаем значения полей формы
    const krName = document.getElementById("task-kr_name").value;
    const name = document.getElementById("task-name").value;
    const kategor = document.getElementById("task-kategor").value;
    const tip = document.getElementById("task-tip").value;
    // Создаем JSON объект
    const data = {
        kr_name: krName,
        name: name,
        kategor: kategor,
        tip: tip
    };
    // Преобразуем JSON объект в строку
    const jsonData = JSON.stringify(data);
    // Отправляем JSON данные на сервер с помощью Fetch API
    fetch(window.location + '_create', {
    method: 'POST', // Метод запроса
    headers: {
        'Content-Type': 'application/json' // Устанавливаем заголовок для JSON данных
    },
    body: jsonData // Передаем JSON данные как тело запроса
    })
    .then(response => response.json()) // Преобразуем ответ сервера в JSON формат
    .then(data => {
    console.log('Сервер ответил:', data);
    // Здесь вы можете выполнить дополнительную обработку ответа сервера, если необходимо
    })
    .catch(error => {
    console.error('Произошла ошибка:', error);
    });
    });
});

document.getElementById("search-form").addEventListener("submit", function (e) {
    e.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получаем значение поля ввода
    var kr_name = document.getElementById("search-kr_name").value;

    // Создаем объект JSON с данными
    var data = {
        kr_name: kr_name
    };

    // Отправляем POST-запрос
    fetch(window.location + '_search', {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(function (response) {
        if (response.ok) {
            return response.json();
        }
        throw new Error("Ошибка сети");
    })
    .then(function (data) {
        // Обработка успешного ответа и вывод данных в таблицу
        var tableBody = document.getElementById("table-body");
        tableBody.innerHTML = ""; // Очистка таблицы

        data.forEach(function (item) {
            var row = document.createElement("tr");
            var keys = ["kr_name", "name", "kategor", "tip"];

            keys.forEach(function (key) {
                var cell = document.createElement("td");
                cell.innerHTML = item[key];
                row.appendChild(cell);
            });

            tableBody.appendChild(row);
        });
    })
    .catch(function (error) {
        // Обработка ошибок
        console.error(error);
    });
})