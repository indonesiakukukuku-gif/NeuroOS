import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

export async function syncVault() {
    console.log("[PROCESS] Scanning for new Identities without Vaults...");

    // 1. Ambil Identities yang belum punya baris di tm_vault
    const { data: identities, error: fetchError } = await supabase
        .from('identities')
        .select('iid, anchor_balance');

    if (fetchError) return console.error("❌ Fetch Error:", fetchError.message);

    for (const identity of identities) {
        // Cek apakah sudah ada di vault
        const { data: vault } = await supabase
            .from('tm_vault')
            .select('iid')
            .eq('iid', identity.iid)
            .single();

        if (!vault) {
            console.log(`[SYNC] Initializing Vault for ${identity.iid}...`);
            
            // 2. Alokasikan Nilai sesuai Tokenomi
            // LUV: 1 Juta (Initial Grant dari 1% alokasi)
            // IND-EUR: Sesuai Anchor Value (€100.000)
            const { error: insertError } = await supabase
                .from('tm_vault')
                .insert([{
                    iid: identity.iid,
                    enpe_balance: 0, 
                    luv_balance: 1000000, 
                    ind_eur_balance: identity.anchor_balance
                }]);

            if (insertError) {
                console.error(`❌ Sync Error for ${identity.iid}:`, insertError.message);
            } else {
                console.log(`✅ ${identity.iid}: Vault Active. LUV & IND-EUR Synced.`);
            }
        }
    }
}
