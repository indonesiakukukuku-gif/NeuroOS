const admin = require('firebase-admin');
const serviceAccount = require('./firebase-adminsdk.json');

if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

async function createPeopleVault() {
  console.log("🔒 Auralang: Mengunci 1% Alokasi Founder ke Vault Rakyat...");
  
  const totalLUV = 100000000000000;
  const rakyatAllocation = totalLUV * 0.01; // 1 Triliun LUV

  const vaultRef = db.collection('vaults').doc('RAKYAT_1M_LUV');
  
  await vaultRef.set({
    vault_name: "1 Million People LUV Pool",
    total_allocation: rakyatAllocation,
    amount_per_person: 1000000,
    remaining_slots: 1000000,
    distributed_count: 0,
    source: "Founder Allocation (IID-021-0000000001)",
    status: "LOCKED_FOR_DISTRIBUTION_2027",
    updated_at: admin.firestore.FieldValue.serverTimestamp()
  });

  console.log("✅ Vault Rakyat Berhasil Dibuat: 1 Triliun LUV telah dipisahkan.");
}

createPeopleVault();
