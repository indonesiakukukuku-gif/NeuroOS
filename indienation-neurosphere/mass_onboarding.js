import { deployPioneer } from './engine.js';

const targetCountries = [
    'BRAZIL', 'INDIA', 'CANADA', 'SOUTH_AFRICA', 'AUSTRALIA', 
    'SOUTH_KOREA', 'MEXICO', 'EGYPT', 'UK', 'ITALY',
    'RUSSIA', 'CHINA', 'ARGENTINA', 'TURKEY', 'SAUDI_ARABIA',
    'NIGERIA', 'VIETNAM', 'THAILAND', 'SPAIN', 'POLAND'
];

async function startGlobalExpansion() {
    console.log("🚀 STARTING GLOBAL ONBOARDING SIMULATION...");
    console.log(`📍 Targeting ${targetCountries.length} Strategic Nations...`);
    
    for (const country of targetCountries) {
        console.log(`🌐 Deploying Infrastructure for: ${country}...`);
        try {
            await deployPioneer(country);
            // Jeda singkat agar tidak overload database
            await new Promise(resolve => setTimeout(resolve, 500)); 
        } catch (e) {
            console.error(`❌ Failed for ${country}:`, e.message);
        }
    }
    console.log("\n✅ GLOBAL EXPANSION COMPLETE.");
}

startGlobalExpansion();
