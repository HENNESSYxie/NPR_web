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

const drawButton2 = document.getElementById('select-point-btn2');
const canvas2 = document.getElementById('my-canvas2');
const context2 = canvas2.getContext('2d');
var pointSelected2 = false;

// Обработчик события клика по кнопке
drawButton2.addEventListener('click', function() {
pointSelected2 = false;
context2.clearRect(0, 0, canvas2.width, canvas2.height);
  // Обработчик события клика по холсту
  canvas2.addEventListener('click', function(event) {
  if (!pointSelected2) {
  pointSelected2 = true;
  context2.clearRect(0, 0, canvas2.width, canvas2.height);
    // Получаем координаты клика
    var x2 = event.clientX - canvas2.offsetLeft;
    var y2 = event.clientY - canvas2.offsetTop;

    // Рисуем точку
    context2.beginPath();
    context2.strokeStyle = "red";
    context2.lineWidth = 1;
    // Рисуем вертикальную линию
    context2.moveTo(x2, 0);
    context2.lineTo(x2, canvas2.height);


    // Отображаем линию на холсте
    context2.stroke();


    const data2 = {
  'x': x2,
  'y': y2,
  "x_relative": x2 / 800,
  'camera': 2
};

// Кодируем объект в формат URL-encoded для отправки
const formEncodedData2 = new URLSearchParams(data2).toString();

// Создаем объект запроса с методом POST и данными для отправки
const request2 = new Request('/save_point/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    "X-CSRFToken": getCookie('csrftoken')
  },
  body: formEncodedData2
});

// Отправляем запрос на сервер
fetch(request2)
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
