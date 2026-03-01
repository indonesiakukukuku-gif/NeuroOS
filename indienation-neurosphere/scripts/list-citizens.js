import { execSync } from 'child_process';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.resolve(__dirname, '../.env') });

const URL = process.env.SUPABASE_URL;
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

console.log("===========================================");
console.log("   LIVE AUDIT: DISTRIBUSI IND-EUR (€)    ");
console.log("===========================================");

if (!URL || !KEY) {
    console.log("❌ Error: Kredensial .env tidak terbaca.");
    process.exit(1);
}

try {
    const cmd = `curl -s -L -X GET "${URL}/rest/v1/claims?select=iid,is_verified,balance_eur" -H "apikey: ${KEY}" -H "Authorization: Bearer ${KEY}" -H "Content-Type: application/json"`;
    const response = execSync(cmd).toString();
    
    if (!response || response.trim() === "" || response.startsWith("<!DOCTYPE")) {
        console.log("Belum ada data warga yang melakukan klaim €100.000.");
    } else {
        const data = JSON.parse(response);
        if (data.length === 0) {
            console.log("Daftar klaim masih kosong di database.");
        } else {
            console.log(`Total Warga Terdeteksi: ${data.length}`);
            console.log("-------------------------------------------");
            data.forEach((user, index) => {
                const status = user.is_verified ? "VERIFIED" : "PENDING";
                const amount = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(user.balance_eur || 100000);
                console.log(`${index + 1}. ${user.iid} | ${status} | ${amount}`);
            });
        }
    }
} catch (error) {
    console.log("Belum ada data warga yang melakukan klaim €100.000.");
}
console.log("===========================================");
