import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function initializeSWF() {
    console.log("🛡️ [SWF] Initializing Sovereign Wealth Fund...");

    // Definisi Suplai sesuai kesepakatan
    const TOTAL_ENPE = 100000000000000; // 100 Triliun
    const SWF_ALLOCATION = TOTAL_ENPE * 0.8; // 80% (80 Triliun)
    const STAKING_ALLOCATION = TOTAL_ENPE * 0.2; // 20% (20 Triliun)

    // Tanggal Buka Kunci (2 tahun dari sekarang)
    const unlockDate = new Date();
    unlockDate.setFullYear(unlockDate.getFullYear() + 2);

    const { data, error } = await supabase
        .from('swf_registry')
        .insert([{
            fund_name: "IndieNation Sovereign Reserve",
            total_enpe_reserve: SWF_ALLOCATION,
            staking_pool: STAKING_ALLOCATION,
            lock_until: unlockDate.toISOString(),
            status: "LOCKED",
            ai_guard_controlled: true
        }]);

    if (error) {
        if (error.code === '42P01') {
            console.error("❌ SWF Error: Tabel 'swf_registry' belum ada di database.");
        } else {
            console.error("❌ Error:", error.message);
        }
    } else {
        console.log("==========================================");
        console.log("✅ SWF INITIALIZED & LOCKED");
        console.log(`💰 Reserve : ${SWF_ALLOCATION.toLocaleString()} ENPE (80%)`);
        console.log(`🥩 Staking : ${STAKING_ALLOCATION.toLocaleString()} ENPE (20%)`);
        console.log(`🔓 Unlocks : ${unlockDate.toLocaleDateString()}`);
        console.log("==========================================");
    }
}

initializeSWF();
