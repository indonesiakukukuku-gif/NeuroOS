const fs = require('fs');

// Memuat data dari Ledger yang sudah kita kunci di nano tadi
const ledger = JSON.parse(fs.readFileSync('sovereign_ledger.json', 'utf8'));

function calculateGlobalAura() {
    console.log("📊 NEUROSPHERE GLOBAL MONITORING - IID-010");
    console.log("------------------------------------------");
    
    let totalAura = 0;
    let anchoredCitizens = 0;

    ledger.pioneers.forEach(p => {
        // Simulasi pembacaan aura real-time (bisa dikembangkan via API)
        totalAura += p.aura_initial; 
        anchoredCitizens++;
        console.log(`Citizen ${p.iid} (${p.name}): Aura ${p.aura_initial.toFixed(4)}`);
    });

    const ecosystemStability = (totalAura / anchoredCitizens) * 100;

    console.log("------------------------------------------");
    console.log(`TOTAL CITIZENS  : ${anchoredCitizens}`);
    console.log(`TOTAL GLOBAL AURA: ${totalAura.toFixed(4)}`);
    console.log(`STABILITY INDEX  : ${ecosystemStability.toFixed(2)}%`);
    console.log("------------------------------------------");
    console.log("🛡️ STATUS: GUARD ONLINE - ALL SYSTEMS NOMINAL");
}

calculateGlobalAura();
