function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const drawButton = document.getElementById('select-point-btn');
const canvas = document.getElementById('my-canvas');
const context = canvas.getContext('2d');
var pointSelected = false;

// Обработчик события клика по кнопке
drawButton.addEventListener('click', function() {
pointSelected = false;
context.clearRect(0, 0, canvas.width, canvas.height);
  // Обработчик события клика по холсту
  canvas.addEventListener('click', function(event) {
  if (!pointSelected) {
  pointSelected = true;
  context.clearRect(0, 0, canvas.width, canvas.height);
    // Получаем координаты клика
    var x = event.clientX - canvas.offsetLeft;
    var y = event.clientY - canvas.offsetTop;

    // Рисуем точку
    context.beginPath();
    context.strokeStyle = "black";
    context.lineWidth = 1;
    // Рисуем вертикальную линию
    context.moveTo(x, 0);
    context.lineTo(x, canvas.height);


    // Отображаем линию на холсте
    context.stroke();


    const data = {
  'x': x,
  'y': y,
  "x_relative": x / 800,
  'camera': 1
};

// Кодируем объект в формат URL-encoded для отправки
const formEncodedData = new URLSearchParams(data).toString();

// Создаем объект запроса с методом POST и данными для отправки
const request = new Request('/save_point/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    "X-CSRFToken": getCookie('csrftoken')
  },
  body: formEncodedData
});

// Отправляем запрос на сервер
fetch(request)
  .then(response => {
    // Обрабатываем ответ от сервера
    console.log(response);
  })
  .catch(error => {
    // Обрабатываем ошибку при отправке запроса
    console.error(error);
  })};
  });
});
