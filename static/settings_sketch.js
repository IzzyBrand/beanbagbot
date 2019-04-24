sq = n => Math.pow(n, 2);
sqrt = n => Math.sqrt(n);

let motor1Slider, motor2Slider, motor3Slider, motor4Slider;
let verticalSpacing = 60;
let usableWidth;
let leftBorder;
var servoMidpoint = 1500;
var sliderThickness = 15;
var servoValWidth = 80;

var socket = io.connect('http://10.0.0.1.local:5000'); // for when deployed on beanbagbot
if (!socket.connected) { socket = io.connect('http://beanbagbot:5000'); } // for when deployed on beanbagbot
if (!socket.connected) { socket = io.connect('http://beanbagbot.local:5000'); } // for when deployed on beanbagbot
if (!socket.connected) { socket = io.connect('http://localhost:5000'); } // for testing locally


socket.on('deactivate', function(msg) {
        console.log(msg);
        active=false;
});

// gets called when the window is resized
function windowResized() {
  sizeDependentSetup(windowWidth, windowHeight);
  resizeCanvas(windowWidth, windowHeight);
  resetMotorSliders();
}

// config all the variables based on the window size
function sizeDependentSetup(w, h) {
  usableWidth = w - 50;
  leftBorder = (w - usableWidth) / 2;
}

function resetMotorSliders() {
  motor1Slider.remove();
  motor2Slider.remove();
  motor3Slider.remove();
  motor4Slider.remove();
  setupMotorSliders();
}

function setupMotorSliders() {
  textSize(30);
  fill(255, 255, 255);
  textAlign(LEFT, CENTER);

  motor1Slider = createSlider(1000, 2000, servoMidpoint, 1);
  motor1Slider.position(leftBorder, verticalSpacing * 1);
  motor1Slider.style('width', usableWidth - servoValWidth + 'px');
  motor1Text = text(servoMidpoint, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 1 + sliderThickness);
  
  motor2Slider = createSlider(1000, 2000, servoMidpoint, 1);
  motor2Slider.position(leftBorder, verticalSpacing * 2);
  motor2Slider.style('width', usableWidth - servoValWidth + 'px');
  motor2Text = text(servoMidpoint, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 2 + sliderThickness);
  
  motor3Slider = createSlider(1000, 2000, servoMidpoint, 1);
  motor3Slider.position(leftBorder, verticalSpacing * 3);
  motor3Slider.style('width', usableWidth - servoValWidth + 'px');
  
  motor4Slider = createSlider(1000, 2000, servoMidpoint, 1);
  motor4Slider.position(leftBorder, verticalSpacing * 4);
  motor4Slider.style('width', usableWidth - servoValWidth + 'px');
}

function setupButtons() {
  button1 = createButton('RESET');
  button1.style('width', '100px');
  button1.style('height', '60px');
  button1.position(leftBorder, verticalSpacing * 5);
  button1.mouseClicked(resetMotorSliders);

  button2 = createButton('BACK TO DRIVE');
  button2.style('width', '150px');
  button2.style('height', '60px');
  button2.position(leftBorder, verticalSpacing * 9);
  button2.mouseClicked(() => {
    (location = "/")
  });

}

// called once on startup
function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  sizeDependentSetup(window.innerWidth, window.innerHeight);

  background(100);
  setupMotorSliders();

  setupButtons();
}

// called at 60hz
function draw() {
  background(30);
  handleMotorValues();
  updateBattery();
}

function handleMotorValues() {
  motor1val = motor1Slider.value();
  motor2val = motor2Slider.value();
  motor3val = motor3Slider.value();
  motor4val = motor4Slider.value();
  
  textSize(30);
  fill(255, 255, 255);

  motor1Text = text(motor1val, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 1 + sliderThickness);
  motor2Text = text(motor2val, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 2 + sliderThickness);
  motor3Text = text(motor3val, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 3 + sliderThickness);
  motor4Text = text(motor4val, usableWidth - servoValWidth + leftBorder + 5, verticalSpacing * 4 + sliderThickness);

  //TODO: Deadband? This is kinda spammy to be sending at 60Hz
  if (motor1val !== servoMidpoint || motor2val !== servoMidpoint || motor3val !== servoMidpoint || motor4val !== servoMidpoint ) {
    data = { 
      motor1 : motor1val,
      motor2 : motor2val,
      motor3 : motor3val,
      motor4 : motor4val,
    };
    socket.emit('raw_pwm', data);
  }
}

function updateBattery() {
  // TODO: Get from app.py once we define the socket
  batteryVoltage = 12.4; 

  textSize(20);
  fill(155, 255, 155);

  batteryText = text("Voltage: " + batteryVoltage + "V ", leftBorder, verticalSpacing * 7);
}
