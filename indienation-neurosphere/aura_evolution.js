import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function evolveAura() {
    const { data: vaults } = await supabase.from('tm_vault').select('iid, luv_balance, nft_metadata');

    for (const vault of vaults) {
        let newAura = "Pioneer Blue";
        const luv = vault.luv_balance;

        // Logika Kasta Baru
        if (luv > 1001000) newAura = "Sovereign Violet";
        else if (luv > 1000500) newAura = "Diamond Cyan"; // Kasta baru di atas Emerald
        else if (luv > 1000050) newAura = "Emerald Green";

        if (vault.nft_metadata?.aura !== newAura) {
            console.log(`✨ EVOLUTION: ${vault.iid} naik kasta ke ${newAura}!`);
            await supabase.from('tm_vault').update({
                nft_metadata: { ...vault.nft_metadata, aura: newAura }
            }).eq('iid', vault.iid);
        }
    }
}
evolveAura();
