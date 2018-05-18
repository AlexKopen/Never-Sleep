var robot = require('robotjs');

var moveMouseUp = true;
var mouseMoveCount = 0;

moveMouse();

setInterval(function () {
  moveMouse()
}, 60000);

function moveMouse() {
  moveMouseUp = !moveMouseUp;
  var yPixelChange = moveMouseUp ? 1 : -1;
  var mousePosition = robot.getMousePos();

  robot.moveMouseSmooth(mousePosition.x, mousePosition.y + yPixelChange);
  console.log('Mouse moved ' + ++mouseMoveCount + ' times');
}
