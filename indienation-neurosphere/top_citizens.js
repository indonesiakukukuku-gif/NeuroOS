import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function showTopCitizens() {
    console.log("🏆 [RANKING] Fetching Top Aura Citizens...");

    const { data: topList, error } = await supabase
        .from('tm_vault')
        .select('iid, luv_balance, nft_metadata')
        .order('luv_balance', { ascending: false })
        .limit(10);

    if (error) return console.error(error.message);

    console.clear();
    console.log("==================================================");
    console.log("🌟   NEUROSPHERE HEROES OF KINDNESS (TOP 10)   🌟");
    console.log("==================================================");
    console.log("RANK | IID                | LUV BALANCE  | AURA");
    console.log("--------------------------------------------------");

    topList.forEach((citizen, index) => {
        const rank = (index + 1).toString().padEnd(4);
        const iid = citizen.iid.padEnd(18);
        const luv = citizen.luv_balance.toLocaleString().padEnd(12);
        const aura = citizen.nft_metadata?.aura || "Pioneer Blue";
        
        console.log(`${rank} | ${iid} | ${luv} | ${aura}`);
    });

    console.log("==================================================");
    console.log("🛡️  Sovereign Reputation Layer Active");
    console.log(`⏰ Last Update: ${new Date().toLocaleTimeString()}`);
    console.log("==================================================");
}

showTopCitizens();
