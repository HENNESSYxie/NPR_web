var canvas2 = document.getElementById("myCanvas2");
var context2 = canvas2.getContext("2d");
var isDrawing2 = false;
var startX2, startY2;

canvas2.addEventListener("mousedown", function(e) {
isDrawing2 = true;
startX2 = e.clientX - canvas2.offsetLeft;
startY2 = e.clientY - canvas2.offsetTop;

});

canvas2.addEventListener("mousemove", function(e) {
if (isDrawing2) {
  var endX2 = e.clientX - canvas2.offsetLeft;
  var endY2 = e.clientY - canvas2.offsetTop;
  context2.clearRect(0, 0, canvas2.width, canvas2.height);
  context2.beginPath();
  context2.moveTo(startX2, startY2);
  context2.lineTo(endX2, endY2);
  context2.stroke();
}
});

canvas2.addEventListener("mouseup", function() {
isDrawing2 = false;
});

