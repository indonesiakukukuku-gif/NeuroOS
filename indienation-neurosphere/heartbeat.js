import { deployPioneer } from './engine.js';
import { syncVault } from './vault_sync.js';
import { generateNFTMetadata } from './nft_generator.js';
import { processKarmaRewards } from './karma_system.js';

async function pulse() {
    console.log(`\n💓 HEARTBEAT: ${new Date().toLocaleString()}`);
    
    try {
        // Jalankan Sinkronisasi Vault untuk IID yang sudah ada
        await syncVault();
        await generateNFTMetadata();
        await processKarmaRewards();
        // Auto Evolution
        const { exec } = await import('child_process');
        exec('node aura_evolution.js');
    } catch (err) {
        console.error("⚠️ Heartbeat Sync Error:", err.message);
    }

    // Set interval 15 detik untuk denyut berikutnya
    setTimeout(pulse, 15000);
}

console.log("🛡️ AI-GUARD: Heartbeat System Activated...");
console.log("Monitoring NeuroSphere Pulse Every 15 Seconds...");
pulse();
