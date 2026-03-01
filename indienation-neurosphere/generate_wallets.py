import os
import hashlib

def generate_wallet_signature(iid):
    secret_salt = "NEUROSPHERE_2026_SOVEREIGN"
    raw_data = f"{iid}_{secret_salt}_100000"
    return hashlib.sha256(raw_data.encode()).hexdigest()

cert_dir = "certificates"
for filename in os.listdir(cert_dir):
    if filename.endswith(".txt"):
        iid = filename.replace("CERTIFICATE_", "").replace(".txt", "")
        signature = generate_wallet_signature(iid)
        
        # Rewrite file agar bersih dan berisi link unik
        content = [
            "NEUROSPHERE SOVEREIGN IDENTITY",
            "------------------------------",
            f"IID: {iid}",
            "STATUS: ACTIVE",
            f"TM-ANCHOR: €100,000",
            f"WALLET-HASH: {signature}",
            f"DIRECT-LINK: https://indienation-tm.web.app/verify.html?id={iid}&hash={signature[:12]}",
            "------------------------------",
            "AURA-LEVEL: 1.0"
        ]
        
        with open(os.path.join(cert_dir, filename), "w") as f:
            f.write("\n".join(content))

print("Kedaulatan Individu diperkuat: Setiap IID kini memiliki link mandiri.")
