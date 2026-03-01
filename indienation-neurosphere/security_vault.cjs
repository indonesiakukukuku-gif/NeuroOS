const crypto = require('crypto');
const fs = require('fs');

const PIONEER_ID = "IID-2026-000000011";
const SECRET_SALT = crypto.randomBytes(16).toString('hex');

const vaultData = {
    iid: PIONEER_ID,
    encryption_key: crypto.createHash('sha256').update(PIONEER_ID + SECRET_SALT).digest('hex'),
    created_at: new Date().toISOString()
};

fs.writeFileSync('vault_key.json', JSON.stringify(vaultData, null, 2));
console.log("=== SECURITY VAULT CREATED ===");
console.log("Private Key Generated for:", PIONEER_ID);
console.log("Key stored safely in: vault_key.json");
