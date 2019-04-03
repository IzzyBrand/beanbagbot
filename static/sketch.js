sq = n => Math.pow(n, 2);
sqrt = n => Math.sqrt(n);

let centerX, centerY;
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
  centerX = window.innerWidth/2;
  centerY = window.innerHeight/2;
  circleX = centerX;
  circleY = centerY;
  circleSize = Math.min(window.innerWidth, window.innerHeight)/6;
  // ws = new WebSocket("ws://localhost:5000/cmd");
}

function draw() {
  // ws.send('hi');
  background(0);
  ellipseMode(CENTER);



  // update the mouse position
  if (active && grabbed) {
    circleX = mouseX;
    circleY = mouseY;
  }
  // drift the mouse back towards the center
  else {
    circleX = (1 - returnRate) * circleX + returnRate * centerX;
    circleY = (1 - returnRate) * circleY + returnRate * centerY;
  }

  if (active) {
    socket.emit('cmd', { x : Math.round(circleX-centerX), y : Math.round(circleY-centerY) });

    // draw the underlying ellipse
    fill(0);
    stroke(255);
    strokeWeight(2);
    ellipse(centerX, centerY, circleSize, circleSize);

    // set the fill for the actual circle
    fill(255);
  }
  else {
    fill(255);
    noStroke();
    textSize(circleSize/6);
    textAlign(CENTER, CENTER);
    text('tap to take control', centerX, centerY*1.5);

    // set the fill for the actual circle
    fill(150);
  }
  noStroke();
  ellipse(circleX, circleY, circleSize, circleSize);
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

function mouseClicked() {
  if (!active) {
    socket.emit('activate', {}, function(data) {active = true;});
  }
}
