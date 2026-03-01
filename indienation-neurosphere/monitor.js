import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function showStats() {
    // 1. Ambil Data Identitas & Vault
    const { count: totalIDs } = await supabase.from('identities').select('*', { count: 'exact', head: true });
    const { data: vaultData } = await supabase.from('tm_vault').select('luv_balance, ind_eur_balance');
    
    // 2. Ambil Data SWF & Emergency
    const { data: swfData } = await supabase.from('swf_registry').select('*').single();
    const { data: emergencyData } = await supabase.from('emergency_funds').select('*').single();

    const totalLUV = vaultData.reduce((acc, curr) => acc + curr.luv_balance, 0);
    const totalEUR = vaultData.reduce((acc, curr) => acc + curr.ind_eur_balance, 0);

    console.clear();
    console.log("==================================================");
    console.log("🛡️  INDIENATION - NEUROSPHERE COMMAND CENTER  🛡️");
    console.log("             (ULTIMATE MONITOR V3)                ");
    console.log("==================================================");
    console.log(`🌍 TOTAL POPULATION  : ${totalIDs} IIDs`);
    console.log(`💎 LUV CIRCULATION   : ${totalLUV.toLocaleString()} LUV`);
    console.log(`💶 TOTAL ANCHOR VAL  : €${totalEUR.toLocaleString()}`);
    console.log("--------------------------------------------------");
    console.log("📊 SOVEREIGN WEALTH FUND (SWF)");
    console.log(`🔒 ENPE RESERVE      : ${swfData ? Number(swfData.total_enpe_reserve).toLocaleString() : 0} ENPE`);
    console.log(`📅 UNLOCK SCHEDULE   : ${swfData ? new Date(swfData.lock_until).toLocaleDateString() : 'N/A'}`);
    console.log("--------------------------------------------------");
    console.log("🆘 EMERGENCY & DISASTER POOL");
    console.log(`🔓 LIQUID LUV        : ${emergencyData ? Number(emergencyData.total_balance).toLocaleString() : 0} LUV`);
    console.log(`📡 STATUS            : ${emergencyData ? emergencyData.status : 'OFFLINE'}`);
    console.log("--------------------------------------------------");
    console.log(`🛡️  STATUS: AI-GUARD ACTIVE | SYSTEM STABLE`);
    console.log(`💓 HEARTBEAT: ${new Date().toLocaleTimeString()}`);
    console.log("==================================================");
    
    setTimeout(showStats, 5000); 
}

showStats();
