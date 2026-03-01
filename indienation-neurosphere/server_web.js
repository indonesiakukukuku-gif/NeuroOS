import express from 'express';
import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';

dotenv.config();
const app = express();
const port = 3001;
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

// HALAMAN DEPAN (Mencegah 404)
app.get('/', (req, res) => {
    res.send(`
        <body style="background:#000; color:#FFD700; font-family:monospace; display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;">
            <h1>🏛️ NEUROSPHERE CITY GATES</h1>
            <p style="color:#555">Sovereign Identity Network is LIVE</p>
            <a href="/passport/IID-021-0000000023" style="color:#00ff88; text-decoration:none; border:1px solid #00ff88; padding:10px; border-radius:5px; margin-top:20px;">VIEW FOUNDER PASSPORT</a>
        </body>
    `);
});

// HALAMAN PASPOR
app.get('/passport/:iid', async (req, res) => {
    const { data } = await supabase.from('tm_vault').select('*').eq('iid', req.params.iid).single();
    if (!data) return res.status(404).send("IID Not Found in Sovereign Database");
    
    const aura = data.nft_metadata?.aura || "Pioneer Blue";
    const color = aura === "Emerald Green" ? "#2ecc71" : "#3498db";

    res.send(`
        <body style="background:#0a0a0a; color:white; font-family:monospace; display:flex; justify-content:center; align-items:center; height:100vh;">
            <div style="border:2px solid ${color}; padding:40px; border-radius:15px; text-align:center; box-shadow: 0 0 20px ${color}; max-width:400px;">
                <h1 style="color:${color}">NEUROSPHERE PASSPORT</h1>
                <hr style="border:0.5px solid #333">
                <p>ID: ${data.iid}</p>
                <h2 style="text-transform:uppercase;">${aura}</h2>
                <p>ANCHOR VALUE: €100,000 (VERIFIED)</p>
                <div style="background:white; padding:10px; display:inline-block; border-radius:5px;">
                    <img src="${data.nft_metadata?.qr_code}" width="150">
                </div>
                <p style="font-size:10px; margin-top:20px; color:#555;">SOVEREIGN IDENTITY LAYER v1.0</p>
            </div>
        </body>
    `);
});

app.listen(port, () => console.log(`🌍 Web Server Updated on Port ${port}`));
