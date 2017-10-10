function getRandomFloat(min, max) {
  return Math.random() * (max - min) + min;
}

function getRandomInteger(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function getRange(start, end, step = 1) {
  var arr = [];
  for (var j = start; j <= end; j += step) {
    arr.push(j);
  }
  return arr;
}

function getRandomColors() {
        var r = getRandomInteger(0,255);
        var g = getRandomInteger(0,255);
        var b = getRandomInteger(0,255);

        var dr, dg, db = 0

        if(r > 200) {dr = -50; } else {dr = 50;}
        if(g > 200) {dg = -50; } else {dg = 50;}
        if(b > 200) {db = -50; } else {db = 50;}

        c1 = "rgba(" + (r + dr) + ", " + (g + dg) + ", " + b + ",1)";
        c2 = "rgba(" + (r + dr) + ", " + g + ", " + (b + db) + ",1)";
        c3 = "rgba(" + r + ", " + (g + dg) + ", " + (b + db) + ",1)";

     console.log([c1,c2,c3])
        return [c1,c2,c3];
}


function shuffle(array) {
  var currentIndex = array.length,
    temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function sinx(value) {
  return 2 * Math.sin(value / 2);
}

function cosx(value) {

  return 2 * Math.cos(value / 2);
}

function sin3x(value) {
  return 2 * Math.sin(3 * value / 4);
}

function cos3x(value) {
  return 2 * Math.cos(3 * value / 4);
}

function genImage() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    var img_w = canvas.width;
    var img_h = canvas.height;

    var clrs = getRandomColors();
    var clr1 = 'red';
    var clr2 = 'blue';
    var clr3 = 'green';

    var square_size = 50;
    var sc_n = 6;
    var type = 1;
    var rnd_min_size = 50;
    var rnd_max_size = 80;

    ctx.fillStyle = clrs[0];
    ctx.fillRect(0, 0, img_w, img_h);

    var points = [];

    for (var xa = 0; xa <= img_w + rnd_min_size; xa += 0.8 * rnd_min_size) {
      for (var ya = 0; ya <= img_h; ya += 0.8 * rnd_min_size) {
        var rnd_x_shift = getRandomInteger(-5, 5);
        var rnd_y_shift = getRandomInteger(-5, 5);
        var y = 0;
        xa += rnd_x_shift;
        for (var cnt in getRange(0, 4)) {
          rnd = getRandomInteger(0, 4);
          if (rnd == 0)
            y += sinx(xa);
          else if (rnd == 1)
            y += cosx(xa);
          else if (rnd == 2)
            y += sin3x(xa);
          else if (rnd == 3)
            y += cos3x(xa);
        }
        y += ya;
        y += rnd_y_shift;
        points.push([xa, y])
      }
    }

    for (var p in shuffle(points)) {
      var x0 = points[p][0]
      var y0 = points[p][1];

      for (var sc = 6; sc > 0; sc--) {
        var dx = square_size / 2 / (sc_n - 1) * sc;
        var dy = square_size / 2 / (sc_n - 1) * sc;

        if (sc % 2 == 1) {
          ctx.fillStyle = clrs[1];
        } else {
          ctx.fillStyle = clrs[2];
        }
        //console.log("x" + sc + " = " + (x0 - dx) + " | y" + sc + " = " + (y0 -dy) + " | width" + sc + " = " + dss);
        if (type = 1) {
          ctx.fillRect(x0 - dx, y0 - dy, 2 * dx, 2 * dy);
        } else if (type = 2) {
          ctx.fillRect(x0 - dx, y0 - dy, 2 * dx, 2 * dy);
        }
      }
    }
  }
}
