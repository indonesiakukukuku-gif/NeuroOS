const express = require('express');
const admin = require('firebase-admin');
const app = express();
const port = 8080;

const serviceAccount = require('./firebase-adminsdk.json');
if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

app.get('/', (req, res) => res.send('<h1>🛡️ NeuroSphere Online!</h1>'));
app.get('/passport/:iid', async (req, res) => {
    const doc = await db.collection('passports').doc(req.params.iid).get();
    if (!doc.exists) return res.status(404).send('IID Not Found');
    const data = doc.data();
    res.send(`<body style="background:#111;color:gold;font-family:sans-serif;text-align:center;padding:50px;">
        <div style="border:5px solid gold;padding:20px;display:inline-block;border-radius:15px;">
            <h1>INDIENATION PASSPORT</h1>
            <p>IID: ${data.iid}</p>
            <h2>NAME: ${data.name}</h2>
            <h1 style="color:#00ff00;">€${Number(data.balance_eur).toLocaleString()}</h1>
            <p>LUV: ${data.luv_balance} | ENPE: ${data.enpe_balance}</p>
        </div>
    </body>`);
});
app.listen(port, '0.0.0.0', () => console.log(`✅ Server Siap di Port ${port}`));
