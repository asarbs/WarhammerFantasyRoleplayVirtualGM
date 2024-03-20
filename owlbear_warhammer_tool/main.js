import './style.css'
import { setupCounter } from './counter.js'

document.querySelector('#app').innerHTML = `
  <div>
    <textarea id="chat-log" cols="40" rows="20"></textarea><br>
  </div>
`

let roomName = "game"
let protocol = "ws"
var url = 'ws://wfrpg.skorupa.net/ws/chat/'+roomName + '/'
console.log(url)
const chatSocket = new WebSocket(url);


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};
