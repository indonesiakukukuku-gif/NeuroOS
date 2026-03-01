const express = require('express');
const admin = require('firebase-admin');
const QRCode = require('qrcode');
const app = express();
const port = 8081;

const serviceAccount = require('./firebase-adminsdk.json');
if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

app.use(express.urlencoded({ extended: true }));

// --- SECURITY MONITORING ---
app.use(async (req, res, next) => {
    const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    const time = new Date().toISOString();
    
    // Log intrusion attempt to Firebase
    await db.collection('security_logs').add({
        event: "ACCESS_ATTEMPT",
        ip_address: ip,
        timestamp: admin.firestore.FieldValue.serverTimestamp(),
        agent: req.headers['user-agent']
    });
    next();
});

// --- THE WATCHMAN: FETCH RECENT LOGS ---
async function showSecurityBriefing() {
    console.log("\n--- 🛡️ SECURITY BRIEFING: RECENT ACCESS ATTEMPTS ---");
    const snapshot = await db.collection('security_logs')
        .orderBy('timestamp', 'desc')
        .limit(5)
        .get();

    if (snapshot.empty) {
        console.log("✅ System Clean: No intrusion attempts detected.");
    } else {
        snapshot.forEach(doc => {
            const data = doc.data();
            console.log(`📍 IP: ${data.ip_address} | Time: ${data.timestamp?.toDate().toLocaleString() || 'Just Now'}`);
        });
    }
    console.log("---------------------------------------------------\n");
}

app.get('/', async (req, res) => {
    const iid = "IID-021-0000000001";
    const qrData = await QRCode.toDataURL(iid);

    res.send(`
    <body style="background:#050505; color:#00ff00; font-family:monospace; padding:20px; text-align:center;">
        <h1 style="border-bottom: 2px solid #00ff00;">🛡️ FOUNDER COMMAND CENTER v1.4</h1>
        <div style="margin: 10px auto; width: 150px; border: 3px solid #00ff00; padding: 5px; background: white;">
            <img src="${qrData}" style="width:100%;" />
        </div>
        <div style="background:rgba(255,0,0,0.1); border:1px solid red; padding:5px; margin-bottom:20px;">
            <marquee>SECURITY PROTOCOL: THE WATCHMAN IS ACTIVE</marquee>
        </div>
        <div style="display:flex; justify-content:space-around;">
            <div style="border: 1px solid #00ff00; padding: 10px; width:45%;">
                <h3>🚨 DONATION POOL</h3>
                <h2 style="color:white;">15T LUV</h2>
            </div>
            <div style="border: 1px solid #00ff00; padding: 10px; width:45%;">
                <h3>💎 VAULT RAKYAT</h3>
                <h2 style="color:white;">1T LUV</h2>
            </div>
        </div>
        <div style="border: 2px red solid; margin-top:30px; padding:20px; background:#200;">
            <h3 style="color:red;">⚠️ EMERGENCY DISTRIBUTION</h3>
            <form action="/distribute-emergency" method="POST">
                <input type="number" name="amount" placeholder="Amount LUV" style="padding:10px; width:80%;">
                <button type="submit" style="background:red; color:white; padding:10px; border:none; margin-top:10px; cursor:pointer;">TRIGGER DISASTER RELIEF</button>
            </form>
        </div>
        <p style="margin-top:30px; font-size:0.7em; color:#444;">AI-Guard Watchman v1.4 | IID-021 Verified</p>
    </body>
    `);
});

app.post('/distribute-emergency', async (req, res) => {
    const amount = req.body.amount;
    res.send(`<h1>✅ Distribution of ${amount} LUV Engaged</h1><a href="/" style="color:cyan;">Back</a>`);
});

app.listen(port, '0.0.0.0', async () => {
    console.log('🛡️ Command Center v1.4 LIVE');
    await showSecurityBriefing();
});
