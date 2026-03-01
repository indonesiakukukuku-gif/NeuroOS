// MASTER SCAN LOGIC - NEUROSPHERE KEDAULATAN
import { createClient } from '@supabase/supabase-js';

const SUPABASE_URL = 'https://seytfmjndfvjrneaupvry.supabase.co';
const SUPABASE_KEY = 'MASUKKAN_KEY_SERVICE_ROLE_BARU_ABANG'; 

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

/**
 * Fungsi Utama Master Scan
 * Alur: Validasi Pendaftaran (€1000) -> Distribusi Reward E-KINDNESS (0-10 LUV)
 */
async function validateAndDistribute(scannedIid) {
    console.log(`\n[MASTER SCAN]: Memindai IID ${scannedIid}...`);
    
    try {
        // 1. CEK STATUS PIONEER (Living Value Check)
        const { data, error } = await supabase
            .from('wallets')
            .select('balance_eur, balance_idr')
            .eq('iid', scannedIid)
            .single();

        if (error || !data) {
            console.error("✘ [GAGAL]: IID tidak ditemukan. Pioneer harus daftar €1000 dulu!");
            return;
        }

        if (data.balance_eur < 1000) {
            console.error("✘ [DITOLAK]: Status pendaftaran belum aktif (Kurang dari €1000).");
            return;
        }

        console.log("✔ [VERIFIKASI SUKSES]: Pioneer Kedaulatan Terdeteksi.");
        console.log(`[SALDO SAAT INI]: €${data.balance_eur} | Rp${data.balance_idr}`);

        // 2. LOGIKA E-KINDNESS (Rewards 0-10 Koin LUV secara acak/algoritma)
        const rewards = Math.floor(Math.random() * 11); // Menghasilkan 0 - 10 koin
        
        console.log(`[E-KINDNESS]: Membagikan ${rewards} Koin LUV Estafet...`);

        // Update ke database (asumsi ada kolom koin_luv atau via RPC)
        const { error: rewardError } = await supabase.rpc('distribute_kindness', {
            target_iid: scannedIid,
            reward_amount: rewards
        });

        if (rewardError) throw rewardError;

        console.log(`[SUCCESS]: ${scannedIid} mendapatkan ${rewards} LUV sebagai Living Value Identity.`);
        
    } catch (err) {
        console.error("[CRITICAL ERROR]:", err.message);
    }
}

// Menjalankan debug untuk Pioneer pertama
validateAndDistribute('IID-2026-000000011');
