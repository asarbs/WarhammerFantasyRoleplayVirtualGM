import './style.css'
import { setupCounter } from './counter.js'
import OBR from '@owlbear-rodeo/sdk'

document.querySelector('#app').innerHTML = `
  <div>
    <textarea id="chat-log" cols="40" rows="20"></textarea><br>
  </div>
`

let roomName = "game"
let protocol = window.location.protocol == "http:" ? "wss" : "wss"
var url = protocol+'://wfrpg.skorupa.net/ws/chat/'+roomName + '/'
console.log(url)
const chatSocket = new WebSocket(url);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
    OBR.notification.show(data.message, "DEFAULT")
};
