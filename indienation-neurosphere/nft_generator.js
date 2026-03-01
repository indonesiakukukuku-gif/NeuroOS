import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';
import QRCode from 'qrcode';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

export async function generateNFTMetadata() {
    console.log("[PROCESS] Generating NFT Metadata Containers...");

    // Ambil data dari Vault yang belum punya Metadata NFT
    const { data: vaults, error } = await supabase
        .from('tm_vault')
        .select('iid, luv_balance, ind_eur_balance');

    if (error) return console.error("❌ Error:", error.message);

    for (const vault of vaults) {
        // Buat String Data untuk QR Code (Standard NeuroSphere)
        const qrData = `NEURO|${vault.iid}|LUV:${vault.luv_balance}|EUR:${vault.ind_eur_balance}`;
        
        // Generate QR dalam bentuk Base64 (untuk UI/NFT Container)
        const qrBase64 = await QRCode.toDataURL(qrData);

        console.log(`🎨 Creating NFT Container for ${vault.iid}...`);
        
        // Update Metadata ke database
        const { error: updateError } = await supabase
            .from('tm_vault')
            .update({ 
                nft_metadata: {
                    type: "Living Value Identity",
                    aura: "Pioneer Blue",
                    qr_code: qrBase64,
                    evolution_stage: 1,
                    last_update: new Date().toISOString()
                }
            })
            .eq('iid', vault.iid);

        if (updateError) {
            console.error(`❌ Metadata Error ${vault.iid}:`, updateError.message);
        } else {
            console.log(`✅ ${vault.iid}: NFT Metadata Integrated.`);
        }
    }
}
