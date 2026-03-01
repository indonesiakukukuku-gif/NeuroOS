import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

export async function processKarmaRewards() {
    console.log(`\n🌟 [E-KINDNESS] Processing Daily Rewards: ${new Date().toLocaleDateString()}`);

    // Ambil semua Vault yang aktif
    const { data: vaults, error } = await supabase
        .from('tm_vault')
        .select('iid, luv_balance, nft_metadata');

    if (error) return console.error("❌ Karma Error:", error.message);

    for (const vault of vaults) {
        // Algoritma Reward: 0-10 LUV secara acak (Simulasi aktivitas sosial)
        const dailyReward = Math.floor(Math.random() * 11);
        const newBalance = vault.luv_balance + dailyReward;

        // Logika Evolusi Aura: Jika LUV > 1,000,050, Aura naik ke "Emerald Green"
        let currentAura = vault.nft_metadata?.aura || "Pioneer Blue";
        if (newBalance > 1000050) {
            currentAura = "Emerald Green";
        }

        console.log(`✨ ${vault.iid}: Received +${dailyReward} LUV Reward.`);

        // Update Balance dan Metadata
        const { error: updateError } = await supabase
            .from('tm_vault')
            .update({ 
                luv_balance: newBalance,
                nft_metadata: { 
                    ...vault.nft_metadata, 
                    aura: currentAura,
                    last_reward: new Date().toISOString()
                }
            })
            .eq('iid', vault.iid);

        if (updateError) console.error(`❌ Update Error ${vault.iid}:`, updateError.message);
    }
}
