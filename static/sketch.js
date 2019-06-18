
let strokeIndex = 0;
let index = 0;
let rainbow;
let prevx, prevy;
let seconds = 3;
let fps;
let pointsInDrawing;


function setup() {
  createCanvas(255, 255);
  newRainbow();
}

function newRainbow() {
  loadJSON('/rainbow', gotRainbow);
}


function draw() {
  if (rainbow) {
    let x = rainbow[strokeIndex][0][index];
    let y = rainbow[strokeIndex][1][index];
    stroke(0);
    strokeWeight(3);
    if (prevx !== undefined) {
      line(prevx, prevy, x, y);

    }
    index++;
    if (index === rainbow[strokeIndex][0].length) {
      strokeIndex++;
      prevx = undefined;
      prevy = undefined;
      index = 0;
      if (strokeIndex === rainbow.length) {
        console.log(strokeIndex);
        rainbow = undefined;
        strokeIndex = 0;
        setTimeout(newRainbow, 250);
      }
    } else {
      prevx = x;
      prevy = y;
    }
  }
}

function gotRainbow(data) {
  background(250);
  rainbow = data.drawing;
  console.log(rainbow);
  pointsInDrawing = rainbow.flat().flat().length / 2 //2 as x, and y
  fps = (pointsInDrawing / seconds);
  console.log(fps);

  frameRate(fps);
}