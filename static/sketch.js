sq = n => Math.pow(n, 2);
sqrt = n => Math.sqrt(n);
function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
    s4() + '-' + s4() + s4() + s4();
}

let myID = guid();

let centerX, centerY;
let minDim;
let maxTravel;
let circleSize;
let circleX, circleY;
var grabbed = false;
var active = false;
let returnRate = 0.1;

var ws;

function attemptToConnectWebSocket() {
  // open a new websocket if we haven't opened one at all yet
  if (ws == undefined) { ws = new WebSocket("ws://localhost:5050/"); }
  // if the current websocket is still open, do nothing
  else if (ws.readyState == ws.OPEN) { return; }
  // otherwise, try to open a websocket with one of the viable server addrs
  else {
    if (ws.readyState > 1) { ws = new WebSocket("ws://localhost:5050/"); }
    if (ws.readyState > 1) { ws = new WebSocket("ws://beanbagbot.local:5050/"); }
    if (ws.readyState > 1) { ws = new WebSocket("ws://10.0.0.1:5050/"); }
    if (ws.readyState > 1) { ws = new WebSocket("ws://beanbagbot:5050/"); }
  }

  // Send myID to the websocket server once the socket has opened
  ws.onopen = function(event) {
    console.log('sending id');
    data = {id: myID};
    ws.send(JSON.stringify(data));
  }

  ws.onmessage = function (event) {
    msg = JSON.parse(event.data);
    // become activate we receive our own ID
    if ('id' in msg) {
      active = (myID == msg['id']);
    }
  }
}

// config all the variables based on the window size
function sizeDependentSetup(w, h) {
  minDim = Math.min(w, h);
  centerX = w/2;
  centerY = h/2;
  circleX = centerX;
  circleY = centerY;
  circleSize = minDim/6;
  fontSize = minDim/25;
  maxTravel = minDim/2-circleSize/2;
}

// gets called when the window is resized
function windowResized() {
  sizeDependentSetup(windowWidth, windowHeight);
  resizeCanvas(windowWidth, windowHeight);
}

// called once on startup
function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  sizeDependentSetup(window.innerWidth, window.innerHeight);
  attemptToConnectWebSocket();
}

// called at 60hz
function draw() {
  background(0);
  ellipseMode(CENTER);

  // try to reconnect the websocket if it has closed
  attemptToConnectWebSocket();

  // deactviate if the websocket is not open
  active = active && (ws.readyState == ws.OPEN);

  // update the circle position
  if (active && grabbed) {
    // limit how far the circle can move from the center
    var d = sqrt(sq(mouseX-centerX) + sq(mouseY-centerY));
    var dx = (mouseX-centerX)/d;
    var dy = (mouseY-centerY)/d;
    d = Math.min(maxTravel, d);

    circleX = dx*d+centerX;
    circleY = dy*d+centerY;

    // only send commands when the user is moving the stick
    data = {turn : (circleX-centerX)/maxTravel,
            forward : -(circleY-centerY)/maxTravel};
    ws.send(JSON.stringify(data));
  }
  // drift the circle back towards the center
  else {
    circleX = (1 - returnRate) * circleX + returnRate * centerX;
    circleY = (1 - returnRate) * circleY + returnRate * centerY;
  }

  if (active) { drawActive(); }
  else { drawInactive(); }
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
    if (ws.readyState == ws.OPEN) {
      text('Tap to take control.', centerX, centerY);
    }
    else {
      text('WebSocket not connected.', centerX, centerY);
    }
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
  // if the user has clicked and we are not active, send an activate message
  if (!active) {
    console.log('blyat');
    data = {'activate': true};
    ws.send(JSON.stringify(data));
  }
}
