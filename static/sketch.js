sq = n => Math.pow(n, 2);
sqrt = n => Math.sqrt(n);

let centerX, centerY;
let minDim;
let circleSize;
let circleX, circleY;
var grabbed = false;
var active = false;
let returnRate = 0.1;

var socket = io.connect('http://localhost:5000');

socket.on('deactivate', function(msg) {
        console.log(msg);
        active=false;
});


function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  minDim = Math.min(window.innerWidth, window.innerHeight);
  centerX = window.innerWidth/2;
  centerY = window.innerHeight/2;
  circleX = centerX;
  circleY = centerY;
  circleSize = minDim/6;
  fontSize = minDim/25;
}

function draw() {
  background(0);
  ellipseMode(CENTER);

  // update the circle position
  if (active && grabbed) {
    // limit how far the circle can move from the center
    var d = sqrt(sq(mouseX-centerX) + sq(mouseY-centerY));
    var dx = (mouseX-centerX)/d;
    var dy = (mouseY-centerY)/d;
    d = Math.min(minDim/2-circleSize/2, d);

    circleX = dx*d+centerX;
    circleY = dy*d+centerY;
  }
  // drift the mouse back towards the center
  else {
    circleX = (1 - returnRate) * circleX + returnRate * centerX;
    circleY = (1 - returnRate) * circleY + returnRate * centerY;
  }

  if (active) {
    socket.emit('cmd', { x : Math.round(circleX-centerX), y : Math.round(circleY-centerY) });
    drawActive();
  }
  else {
    drawInactive();
  }
}

function drawActive() {
    // draw the circle
    fill(255);
    noStroke();
    ellipse(circleX, circleY, circleSize, circleSize);
    ellipse(centerX, centerY, circleSize, circleSize);

    var a = circleSize/2;
    var d = sqrt(sq(circleX-centerX) + sq(circleY-centerY));
    var w = a/3;
    var r = (-4*sq(a) + sq(d) + 4*sq(w))/(8*(a-w));
    var dx = (circleX - centerX)/d;
    var dy = (circleY - centerY)/d;

    if (r > 0) {

      strokeWeight(a/(a+r)*(w+r)*2);
      stroke(255);
      line(centerX, centerY, circleX, circleY);

      var c1x = d*dx/2 + (w+r)*dy;
      var c1y = d*dy/2 - (w+r)*dx;
      var c2x = d*dx/2 - (w+r)*dy;
      var c2y = d*dy/2 + (w+r)*dx;
      fill(0);
      noStroke();
      ellipse(centerX+c1x, centerY+c1y, r*2, r*2);
      ellipse(centerX+c2x, centerY+c2y, r*2, r*2);
    }


}

function drawInactive() {
    // draw the circle
    fill(50);
    noStroke();
    ellipse(circleX, circleY, circleSize, circleSize);

    // draw a message telling the user to take control
    fill(255);
    noStroke();
    textSize(fontSize);
    textAlign(CENTER, CENTER);
    text('Tap to take control.', centerX, centerY);
}

// handle the mouse down event
function mousePressed() {
  let distToCenter = sqrt(sq(mouseX - circleX) + sq(mouseY - circleY));
  if (distToCenter < circleSize/2) {
    grabbed = true;
  }
}

// handle the mouse up event
function mouseReleased() {
  grabbed = false;
}

// handle mouse clicking to grab control
function mouseClicked() {
  if (!active) {
    socket.emit('activate', {}, function(data) {active = true;});
  }
}
