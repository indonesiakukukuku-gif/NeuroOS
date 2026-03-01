import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';
import fs from 'fs';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function generateSnapshot() {
    console.log("📄 Generating Sovereign Snapshot Report...");

    const { data: identities } = await supabase.from('identities').select('iid, country_code, created_at');
    const { data: vaults } = await supabase.from('tm_vault').select('iid, luv_balance, ind_eur_balance, nft_metadata');
    const { data: swf } = await supabase.from('swf_registry').select('*').single();
    const { data: emergency } = await supabase.from('emergency_funds').select('*').single();

    const report = {
        timestamp: new Date().toISOString(),
        founder: "INDIE-Founder",
        summary: {
            total_citizens: identities ? identities.length : 0,
            total_luv_in_vaults: vaults ? vaults.reduce((acc, v) => acc + (v.luv_balance || 0), 0) : 0,
            total_anchor_value_eur: vaults ? vaults.reduce((acc, v) => acc + (v.ind_eur_balance || 0), 0) : 0,
        },
        sovereign_wealth: {
            enpe_reserve: swf ? swf.total_enpe_reserve : 0,
            staking_pool: swf ? swf.staking_pool : 0,
            status: swf ? swf.status : "N/A"
        },
        emergency_pool: {
            liquid_luv: emergency ? emergency.total_balance : 0,
            status: emergency ? emergency.status : "N/A"
        },
        identities: (identities || []).map(id => {
            const vault = (vaults || []).find(v => v.iid === id.iid);
            return {
                iid: id.iid,
                country: id.country_code,
                aura: vault?.nft_metadata?.aura || "N/A",
                luv: vault?.luv_balance || 0,
                eur: vault?.ind_eur_balance || 0
            };
        })
    };

    const fileName = `snapshot_${new Date().toISOString().split('T')[0]}.json`;
    fs.writeFileSync(fileName, JSON.stringify(report, null, 4));

    console.log("==========================================");
    console.log(`✅ SNAPSHOT CREATED: ${fileName}`);
    console.log(`📊 Recorded ${identities ? identities.length : 0} Identities`);
    console.log(`💰 Total Anchor: €${report.summary.total_anchor_value_eur.toLocaleString()}`);
    console.log("==========================================");
}

generateSnapshot();
