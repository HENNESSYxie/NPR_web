var canvas1 = document.getElementById("myCanvas");
var context1 = canvas1.getContext("2d");
var isDrawing1 = false;
var startX1, startY1;

canvas1.addEventListener("mousedown", function(e) {
isDrawing1 = true;
startX1 = e.clientX - canvas1.offsetLeft;
startY1 = e.clientY - canvas1.offsetTop;

});

canvas1.addEventListener("mousemove", function(e) {
if (isDrawing1) {
  var endX1 = e.clientX - canvas1.offsetLeft;
  var endY1 = e.clientY - canvas1.offsetTop;
  context1.clearRect(0, 0, canvas1.width, canvas1.height);
  context1.beginPath();
  context1.moveTo(startX1, startY1);
  context1.lineTo(endX1, endY1);
  context1.stroke();
}
});

canvas1.addEventListener("mouseup", function() {
isDrawing1 = false;
});

