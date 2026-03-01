const fs = require('fs');
const QRCode = require('qrcode');

const citizens = [
    {id: "011", name: "PURWANTORO"},
    {id: "012", name: "MARSELUS HASAN"},
    {id: "013", name: "KIKI KESTURI"},
    {id: "014", name: "DIAVATCHE BOGUI EUGÈNE"},
    {id: "015", name: "Miftahudin"},
    {id: "016", name: "Kastim"},
    {id: "017", name: "Meiriska"},
    {id: "018", name: "Rasheed Abiodun O. Gbaiye"},
    {id: "019", name: "Lugard Jumbo"},
    {id: "020", name: "Heri Heryanto"}
];

async function updateCertificates() {
    for (let c of citizens) {
        const iid = `IID-021-00000000${c.id}`;
        const qrImage = await QRCode.toDataURL(`https://indienation-tm.web.app/cert/${c.id}`, {
            color: { dark: '#00ff00', light: '#000000' }
        });

        const html = `<!DOCTYPE html><html><head><title>Cert - ${c.name}</title><style>body{background:#000;color:#0f0;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}.cert{border:2px solid #0f0;padding:30px;text-align:center;box-shadow:0 0 20px #0f0;max-width:400px;}.iid{color:white;margin:10px 0;}.qr{border:1px solid #0f0;padding:10px;margin:20px 0;}</style></head><body><div class="cert"><h2>NEUROSPHERE</h2><p>VERIFIED IDENTITY</p><div class="qr"><img src="${qrImage}" width="150"></div><div class="iid">HOLDER: ${c.name}</div><div class="iid">ID: ${iid}</div><h3 style="color:gold;">VALUE: €100,000</h3><p style="font-size:0.7em;">AI-GUARD AUTHENTICATED</p></div></body></html>`;
        
        const path = `./public/cert/${c.id}`;
        if (!fs.existsSync(path)) fs.mkdirSync(path, { recursive: true });
        fs.writeFileSync(`${path}/index.html`, html);
        console.log(`✅ Updated: ${c.name} (${iid})`);
    }
}
updateCertificates();
