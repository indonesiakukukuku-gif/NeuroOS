const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.get('/', (req, res) => {
    res.send('<h1>📡 Neuro-Messenger Service Active</h1>');
});

io.on('connection', (socket) => {
    console.log('🔗 Sinyal IID terdeteksi...');

    socket.on('join', (iid) => {
        socket.join(iid);
        console.log(`👤 ${iid} telah masuk ke jaringan mandiri.`);
    });

    socket.on('private_message', (data) => {
        // data = { to: 'IID-021-0000000002', msg: 'Halo Warga!' }
        io.to(data.to).emit('new_msg', { from: data.from, body: data.msg });
        console.log(`📩 Pesan dari ${data.from} ke ${data.to} terkirim.`);
    });
});

server.listen(8081, '0.0.0.0', () => {
    console.log('🚀 Neuro-Communications menyala di Port 8081');
});
