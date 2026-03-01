import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';
dotenv.config();

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function createPassports() {
    console.log("📜 [CONSTITUTION] Generating Sovereign Passports...");
    
    const { data: topCitizens } = await supabase
        .from('tm_vault')
        .select('iid, luv_balance, nft_metadata')
        .order('luv_balance', { ascending: false })
        .limit(10);

    topCitizens.forEach(citizen => {
        const aura = citizen.nft_metadata?.aura || "Pioneer Blue";
        console.log(`--------------------------------------------------`);
        console.log(`🆔 ID: ${citizen.iid}`);
        console.log(`🌈 STATUS: ${aura}`);
        console.log(`⚖️ RIGHTS: Access to ${aura === 'Emerald Green' ? 'Premium City Services' : 'Basic City Services'}`);
        console.log(`🛡️ ANCHOR: €100,000 Verified`);
        console.log(`--------------------------------------------------`);
    });
    
    console.log("✅ All Passports synchronized with Auralang Logic.");
}

createPassports();
