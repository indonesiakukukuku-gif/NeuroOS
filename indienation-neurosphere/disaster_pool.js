import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function initDisasterPool() {
    console.log("🛡️ [EMERGENCY] Initializing Disaster & Pool Donation...");

    const TOTAL_LUV = 100000000000000; // 100 Triliun
    const DISASTER_ALLOCATION = TOTAL_LUV * 0.15; // 15% (15 Triliun)

    const { data, error } = await supabase
        .from('emergency_funds')
        .insert([{
            fund_name: "Global Disaster & Emergency Pool",
            asset_type: "LUV",
            total_balance: DISASTER_ALLOCATION,
            status: "OPEN", // Status OPEN untuk distribusi cepat
            description: "Alokasi 15% untuk bantuan kemanusiaan dan bencana."
        }]);

    if (error) {
        console.error("❌ Error:", error.message);
    } else {
        console.log("==========================================");
        console.log("✅ DISASTER POOL ACTIVE & READY");
        console.log(`🆘 Allocation : ${DISASTER_ALLOCATION.toLocaleString()} LUV`);
        console.log(`🔓 Status     : OPEN (Liquid)`);
        console.log("==========================================");
    }
}

initDisasterPool();
