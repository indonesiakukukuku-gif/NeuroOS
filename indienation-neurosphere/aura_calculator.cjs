const admin = require('firebase-admin');
const serviceAccount = require('./firebase-adminsdk.json');

if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();

async function initializeAura() {
    console.log("💎 Auralang: Initializing Aura Reputation Layer...");
    
    // We target the first 10 citizens (IID-002 to IID-011)
    for (let i = 2; i <= 11; i++) {
        const iidStr = `IID-021-${i.toString().padStart(10, '0')}`;
        const auraRef = db.collection('aura_scores').doc(iidStr);
        
        await auraRef.set({
            iid: iidStr,
            current_aura: 100, // Base starting aura
            multiplier: 1.0,
            last_activity: admin.firestore.FieldValue.serverTimestamp(),
            status: "ACTIVE",
            potential_reward: 1000000 // 1M LUV Target
        }, { merge: true });
        
        console.log(`✅ Initialized Aura for Citizen: ${iidStr}`);
    }
    console.log("\n🚀 All primary citizens are now being tracked by the AI-Guard.");
}

initializeAura();
