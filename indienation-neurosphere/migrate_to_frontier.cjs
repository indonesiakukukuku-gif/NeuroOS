const admin = require('firebase-admin');
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

// 1. Inisialisasi Firebase (Indienation Frontier Portal)
const serviceAccount = require("./firebase-adminsdk.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
const db = admin.firestore();

// 2. Inisialisasi Sumber Data Lokal (Supabase)
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function startMigration() {
    console.log("🏙️  MEMULAI MIGRASI KE INDIENATION FRONTIER PORTAL...");
    
    // Ambil data 25 pionir
    const { data: citizens, error } = await supabase.from('tm_vault').select('*');
    
    if (error) {
        console.error("❌ Gagal mengambil data lokal:", error);
        return;
    }

    console.log(`📦 Ditemukan ${citizens.length} warga. Memulai sinkronisasi...`);

    for (const citizen of citizens) {
        console.log(`🔥 Mendaftarkan IID: ${citizen.iid}...`);
        
        await db.collection('citizens').doc(citizen.iid).set({
            identity: {
                iid: citizen.iid,
                founder_name: "INDIE-Founder",
                aura: citizen.nft_metadata?.aura || "Emerald Green",
                status: "VERIFIED_CITIZEN"
            },
            tm_wallet: {
                enpe_balance: 1000000, // Manifestasi E Coin
                luv_balance: citizen.luv_balance || 0,
                ind_eur_anchor: 100000, // €100,000 Dasar
                total_tm_value: "Technology Money"
            },
            metadata: {
                joined_at: new Date().toISOString(),
                last_heartbeat: new Date().toISOString(),
                sector: "Central District"
            }
        });
    }
    
    console.log("==========================================");
    console.log("✅ MIGRASI SELESAI!");
    console.log("🌐 KOTA DIGITAL SEKARANG LIVE DI FIREBASE.");
    console.log("==========================================");
}

startMigration();
