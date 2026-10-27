
/*
Deux event listeners : pour keydown et keyup.
*/
document.addEventListener(
  'keydown',
  function(event) {
    event.preventDefault();
    switch(event.key) {
      case 'ArrowUp':
        sendCommand('start_forward');
        break;
      case 'ArrowDown':
        sendCommand('start_backward');
        break;
      case 'ArrowLeft':
        sendCommand('start_left');
        break;
      case 'ArrowRight':
        sendCommand('start_right');
        break;
      case ' ':
        sendCommand('stop');
        break;
      case 'Enter':
        sendCommand('start');
        break;
      case 'Shift':
        sendCommand('start_boost');
        break;
    }
  }
);
document.addEventListener(
  'keyup',
  function(event) {
    switch(event.key) {
      case 'ArrowUp':
        sendCommand('end_forward');
        break;
      case 'ArrowDown':
        sendCommand('end_backward');
        break;
      case 'ArrowLeft':
        sendCommand('end_left');
        break;
      case 'ArrowRight':
        sendCommand('end_right');
        break;
      case 'Shift':
        sendCommand('end_boost');
        break;
    }
  }
);

/*
L'objet socket se connecte à la WebSocket
*/
const socket = io();

/*
Fonctions qui envoient des commandes au serveur
*/
function sendCommand(action) {
  socket.emit('command', { action });
}
function sendAsyncCommand(action) {
  socket.emit('async_command', { action });
}
function refreshBattery() {
  socket.emit('refresh_battery');
}

/*
Fonctions qui reçoivent la réponse du serveur
*/

// 'csl' sert à afficher des messages
var lastMessages = [];
socket.on(
  'csl',
  handleConsole
);
function handleConsole(msg) {
  var existing = lastMessages.find(
    m =>
      m.raw_text === msg.raw_text &&
      (msg.raw_text.includes('battery') || msg.raw_text.includes('Status'))
  );
  if (existing) {
    existing.count += 1;
    existing.shown_text = `${existing.text} (${existing.count})`;
  }
  else {
    lastMessages.push({
      text: msg.text,
      color: msg.color || "black",
      raw_text: msg.raw_text,
      count: 1,
      shown_text: msg.text
    });
  }
  if (lastMessages.length > 25) lastMessages.shift();
  var n_lines = 25;
  var csl = "";
  for (var i = 0; i < Math.min(lastMessages.length, n_lines); i++) {
    var m = lastMessages[lastMessages.length - i - 1];
    csl += `<span style="color:${m.color}">${m.shown_text}</span><br>`;
  }
  document.getElementById('console').innerHTML = csl;
}

// 'ack' s'assure de la reception de la commande par app.py
var myList = [];
socket.on(
  'ack',
  handleAcknowledge
);
function handleAcknowledge(msg) {
  myList.push("Commande confirmée : " + msg.action + "\n");
  var n_lines = 20;
  var csl = "";
  for (var i = 0; i < Math.min(myList.length, n_lines); i++) {
    csl += myList[myList.length - i - 1];
  }
  document.getElementById('console').innerText = "Console :\n" + csl;
}

// 'bat' sert à recevoir l'état de la batterie
socket.on(
  'bat',
  handleBattery
);
function handleBattery(msg) {
  var soc = msg.soc
  var conso_mw = msg.conso_mw
  var soc_sur_10 = parseInt(soc / 10);
  var bat = "";
  for (var i = 0; i < 10; i++) {
    if (i < soc_sur_10) {
      bat += "■"
    }
    else {
      bat += "□"
    }
  }
  document.getElementById('battery').innerText =
    bat + "\nNiveau : " + soc.toString() + "%" + "\nConsommation : " + conso_mw.toString() + "mW";
}

// 'upd' sert à update les informations du robot
const canvas = document.getElementById("minimap");
const ctx = canvas.getContext("2d");
socket.on(
  'upd',
  handleUpdate
);
function handleUpdate(msg) {
  var txt = "";
  for (const key in msg) {
    txt += `${key} : ${msg[key]}\n`;
  }
  document.getElementById('status').innerText = txt;
  // Mettre à jour la minimap
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawRobot(ctx, msg["x"], msg["y"], msg["dir"]);
  drawMap(ctx);
  ctx.closePath();
}

/*
Fonctions auxiliaires
*/

function drawRobot(ctx, x, y, dir) {
  var drawX = 100 + x / 2;
  var drawY = 100 - y / 2;
  var drawDir = -dir;
  const rectLength = 20;
  const rectWidth = 10;
  const coneLength = 400;
  const coneFOV = Math.PI / 12;
  ctx.save();
  ctx.translate(drawX, drawY);
  ctx.rotate(drawDir);
  ctx.fillStyle = "red";
  ctx.beginPath();
  ctx.fillRect(-rectLength / 2, -rectWidth / 2, rectLength, rectWidth);
  ctx.closePath();
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(coneLength * Math.cos(coneFOV), coneLength * Math.sin(coneFOV));
  ctx.lineTo(coneLength * Math.cos(-coneFOV), coneLength * Math.sin(-coneFOV));
  ctx.closePath();
  ctx.fillStyle = "rgba(255, 0, 0, 0.3)"; // translucent green
  ctx.fill();
  ctx.restore();
}

function drawMap(ctx) {
  ctx.beginPath();
  ctx.arc(100, 100, 150 / 2, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(100, 100, 20 / 2, 0, 2 * Math.PI);
  ctx.stroke();
  for (var i = 0; i < 4; i++) {
    var angle_secteur = i * Math.PI / 2;
    ctx.beginPath();
    ctx.fillStyle = "green";
    ctx.fillRect(100 + 150 * Math.cos(angle_secteur) / 2, 100 - 150 * Math.sin(angle_secteur) / 2, 5, 5);
    ctx.closePath();
  }
}