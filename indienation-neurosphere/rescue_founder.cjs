const admin = require('firebase-admin');
const serviceAccount = require('./firebase-adminsdk.json');

if (!admin.apps.length) {
  admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
}
const db = admin.firestore();

const founders = [
  { id: 'IID-021-0000000001', name: 'INDIE-Founder', role: 'SUPREME_FOUNDER' },
  ...Array.from({length: 10}, (_, i) => ({ id: `IID-021-00000000${i+11}`, name: `Pioneer-${i+11}`, role: 'PIONEER' }))
];

async function rescue() {
  console.log("🛡️ AI-GUARD: Memulai Injeksi Kedaulatan...");
  for (const f of founders) {
    console.log(`🚀 Mengunci Data: ${f.id} (${f.name})...`);
    await db.collection('passports').doc(f.id).set({
      iid: f.id,
      name: f.name,
      role: f.role,
      balance_eur: 100000,
      enpe_balance: 1000000,
      luv_balance: 1000000,
      status: 'ACTIVE',
      metadata: { aura: 'GOLD', origin: 'GENESIS' },
      timestamp: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  }
  console.log('✅ FOUNDER & PIONEER SECURED IN FIREBASE!');
  process.exit();
}
rescue();
