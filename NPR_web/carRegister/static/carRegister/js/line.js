var canvas1line = document.getElementById("my-canvas");
var ctx = canvas1line.getContext("2d");

fetch('/last_point?camera=' + 1)
    .then(response => response.json())
    .then(data => {
        ctx.beginPath();
        ctx.strokeStyle = "black";
        ctx.lineWidth = 1;
        // Рисуем вертикальную линию
        ctx.moveTo(data.x, 0);
        ctx.lineTo(data.x, canvas1line.height);
        ctx.stroke();
    })
    .catch(error => console.error(error));