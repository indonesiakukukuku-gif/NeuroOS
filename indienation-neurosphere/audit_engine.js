import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function runAudit() {
    console.log("🔍 [AUDIT] Starting Integrity Check...");
    
    // Ambil data distribusi dari log atau kalkulasi manual
    const { data: vaults } = await supabase.from('tm_vault').select('iid, luv_balance');
    
    const MAX_ALLOWED_LUV = 1000500; // Batas wajar untuk fase awal ini
    let anomalies = [];

    vaults.forEach(v => {
        if (v.luv_balance > MAX_ALLOWED_LUV) {
            anomalies.push({ iid: v.iid, balance: v.luv_balance });
        }
    });

    if (anomalies.length > 0) {
        console.log("⚠️ [ALERT] Anomalies Detected!");
        anomalies.forEach(a => {
            console.log(`🚫 IID: ${a.iid} | Suspicious Balance: ${a.balance}`);
        });
    } else {
        console.log("✅ [CLEAN] No LUV anomalies detected. Integrity intact.");
    }
}

runAudit();
