const admin = require('firebase-admin');
// Ganti ini dengan path file JSON dari Firebase Console Abang nanti
const serviceAccount = require("./firebase-adminsdk.json"); 

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://neurosphere-city.firebaseio.com"
});

const db = admin.firestore();

async function syncToFirebase(iid, data) {
    console.log(`🔥 Syncing ${iid} to Firebase City...`);
    await db.collection('citizens').doc(iid).set({
        ...data,
        city_sector: "Central District",
        last_sync: new Date().toISOString()
    });
}

console.log("🏙️ Firebase Bridge Ready for Groundbreaking!");
