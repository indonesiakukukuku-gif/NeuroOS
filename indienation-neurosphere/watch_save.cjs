const fs = require('fs');
const path = require('path');

const targetFile = './engine.js';
const backupDir = './backups';

if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir);

console.log("🛡️ AI-Guard: Auto-Save Watcher Active...");

fs.watchFile(targetFile, { interval: 1000 }, (curr, prev) => {
    if (curr.mtime !== prev.mtime) {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const backupPath = path.join(backupDir, `engine_backup_${timestamp}.js`);

        try {
            fs.copyFileSync(targetFile, backupPath);
            console.log(`✅ Auto-Saved: ${backupPath}`);
        } catch (err) {
            console.log(`❌ Error: ${err.message}`);
        }
    }
});
