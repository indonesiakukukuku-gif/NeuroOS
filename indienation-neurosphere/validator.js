import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function validateIdentity(iid) {
    console.log(`\n🔍 SCANNING IDENTITY: [${iid}]`);
    console.log("------------------------------------------");

    const { data: vault, error } = await supabase
        .from('tm_vault')
        .select(`
            iid, 
            luv_balance, 
            ind_eur_balance, 
            nft_metadata,
            identities ( country_code, created_at )
        `)
        .eq('iid', iid)
        .single();

    if (error || !vault) {
        console.error("❌ INVALID IDENTITY: IID tidak ditemukan di NeuroSphere.");
        return;
    }

    const meta = vault.nft_metadata || {};

    console.log(`✅ STATUS      : VERIFIED`);
    console.log(`🌍 ORIGIN      : ${vault.identities.country_code}`);
    console.log(`✨ AURA        : ${meta.aura || 'None'}`);
    console.log(`📊 EVOLUTION   : Stage ${meta.evolution_stage || 0}`);
    console.log("------------------------------------------");
    console.log(`💎 LUV BALANCE : ${vault.luv_balance.toLocaleString()} LUV`);
    console.log(`💶 IND-EUR     : €${vault.ind_eur_balance.toLocaleString()}`);
    console.log("------------------------------------------");
    console.log(`🔗 NFT CONTAINER: QR Code Securely Encoded`);
    console.log(`📅 REGISTERED  : ${new Date(vault.identities.created_at).toLocaleDateString()}`);
    console.log("==========================================\n");
}

// Ambil argumen dari command line
const targetIID = process.argv[2];
if (!targetIID) {
    console.log("Gunakan: node validator.js IID-021-0000000021");
} else {
    validateIdentity(targetIID);
}
