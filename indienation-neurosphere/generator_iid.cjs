const admin = require('firebase-admin');
const serviceAccount = require('./firebase-adminsdk.json');

if (!admin.apps.length) {
  admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
}
const db = admin.firestore();

async function createCitizenBatch(start, count) {
  const batch = db.batch();
  console.log(`🚀 Memulai pendaftaran ${count} warga internasional baru...`);

  for (let i = 0; i < count; i++) {
    const nextId = (start + i).toString().padStart(10, '0');
    const iid = `IID-021-${nextId}`;
    const docRef = db.collection('passports').doc(iid);
    
    batch.set(docRef, {
      iid: iid,
      name: `Citizen-${nextId}`,
      role: "CITIZEN",
      balance_eur: 0, // Akan diisi bertahap sesuai Living Value Scheme
      luv_balance: 0,
      enpe_balance: 0,
      status: "PENDING_ACTIVATION",
      created_at: admin.firestore.FieldValue.serverTimestamp()
    });
  }

  await batch.commit();
  console.log(`✅ Berhasil mendaftarkan warga hingga ${start + count - 1}`);
}

// Mulai pendaftaran dari ID ke-2 (Setelah Founder)
createCitizenBatch(2, 10); 
