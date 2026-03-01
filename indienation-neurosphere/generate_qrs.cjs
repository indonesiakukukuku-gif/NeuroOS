const QRCode = require('qrcode');
const fs = require('fs');

async function generateBatch() {
    console.log("📡 AI-Guard: Generating Sovereign QR Batch...");
    
    for (let i = 11; i <= 20; i++) {
        const iid = `IID-021-00000000${i}`;
        const url = `https://indienation-tm.web.app/cert/0${i}`;
        const path = `./public/cert/0${i}`;
        
        // Generate QR Code sebagai DataURL
        const qrImage = await QRCode.toDataURL(url, {
            color: { dark: '#00ff00', light: '#000000' },
            margin: 1
        });

        // Update Sertifikat dengan QR Code
        const certHtml = `
<!DOCTYPE html>
<html>
<head>
    <title>Sovereign Cert - ${iid}</title>
    <style>
        body { background: #000; color: #0f0; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .cert { border: 2px solid #0f0; padding: 30px; text-align: center; box-shadow: 0 0 20px #0f0; max-width: 400px; }
        .iid { color: white; font-size: 1.2em; margin: 10px 0; }
        .qr { background: #000; padding: 10px; display: inline-block; border: 1px solid #0f0; margin: 20px 0; }
        .footer { font-size: 0.7em; color: #555; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="cert">
        <h2 style="letter-spacing: 5px;">NEUROSPHERE</h2>
        <p>SOVEREIGN IDENTITY VERIFIED</p>
        <div class="qr"><img src="${qrImage}" width="150"></div>
        <div class="iid">${iid}</div>
        <h3 style="color:gold; margin: 5px 0;">VALUE: €100,000</h3>
        <p style="font-size: 0.8em;">STATUS: ANCHORED PIONEER</p>
        <div class="footer">AI-GUARD AUTHENTICATED | IID-010</div>
    </div>
</body>
</html>`;

        if (!fs.existsSync(path)) fs.mkdirSync(path, { recursive: true });
        fs.writeFileSync(`${path}/index.html`, certHtml);
        console.log(`✅ QR & Cert Ready: ${iid}`);
    }
}

generateBatch();
