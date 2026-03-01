import { execSync } from 'child_process';

const SUPABASE_URL = 'https://seytfmjndfvjrneaupvry.supabase.co';
const SUPABASE_SERVICE_KEY = 'MASUKKAN_KEY_BARU_DI_SINI'; 

const pioneers = [
    "IID-2026-000000011", "IID-2026-000000012", "IID-2026-000000013",
    "IID-2026-000000014", "IID-2026-000000015", "IID-2026-000000016",
    "IID-2026-000000017", "IID-2026-000000018", "IID-2026-000000019",
    "IID-2026-000000020"
];

function massTransfer(amount) {
    console.log(`\n[NEUROLANG]: Mengaktifkan Jalur Sistem (CURL-Bypass)...`);
    
    pioneers.forEach(iid => {
        try {
            // Memaksa koneksi menggunakan CURL sistem agar tidak kena TypeError Fetch
            const command = `curl -s -X POST "${SUPABASE_URL}/rest/v1/rpc/increment_balance" \
                -H "apikey: ${SUPABASE_SERVICE_KEY}" \
                -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
                -H "Content-Type: application/json" \
                -d '{"target_iid": "${iid}", "inc_amount": ${amount}}'`;

            execSync(command);
            console.log(`[✔] SUCCESS: ${iid} | Terdistribusi: Rp ${amount}`);
        } catch (err) {
            console.error(`[!] GAGAL di ${iid}: Jalur sistem terhambat.`);
        }
    });
    console.log(`\n[SYSTEM]: Kedaulatan Terlaksana. Cek Saldo di Dashboard.`);
}

const amountInput = process.argv[2] || 5;
massTransfer(parseFloat(amountInput));
