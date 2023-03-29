var canvas2line = document.getElementById("my-canvas2");
var ctx2 = canvas2line.getContext("2d");

fetch('/last_point?camera=' + 2)
    .then(response => response.json())
    .then(data => {
        ctx2.beginPath();
        ctx2.strokeStyle = "black";
        ctx2.lineWidth = 1;
        // Рисуем вертикальную линию
        ctx2.moveTo(data.x, 0);
        ctx2.lineTo(data.x, canvas2line.height);
        ctx2.stroke();
    })
    .catch(error => console.error(error));