var canvas1line = document.getElementById("my-canvas");
var ctx = canvas1line.getContext("2d");

fetch('/last_point?camera=' + 1)
    .then(response => response.json())
    .then(data => {
        ctx.beginPath();
        ctx.strokeStyle = "red";
        ctx.lineWidth = 1;
        ctx.rect(data.x, 0, canvas1line.width, canvas1line.height);
        ctx.fillStyle = "#90EE90";
        // Рисуем вертикальную линию
        ctx.moveTo(data.x, 0);
        ctx.lineTo(data.x, canvas1line.height);
        ctx.fill();
        ctx.stroke();
    })
    .catch(error => console.error(error));