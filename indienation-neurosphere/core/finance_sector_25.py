import json
import os
import datetime

# @identity: IID-021+
# @sector: 25 (Finance & Banking)
# @asset: IND-EUR (Indienation Coin - Value Anchor)

WALLET_PATH = os.path.expanduser("~/indienation-neurosphere/core/stable_wallet.json")

def issue_ind_eur(amount, reason):
    if not os.path.exists(WALLET_PATH):
        wallet = {"total_ind_eur": 0, "history": []}
    else:
        with open(WALLET_PATH, "r") as f:
            wallet = json.load(f)

    wallet["total_ind_eur"] += amount
    wallet["history"].append({
        "amount": amount,
        "reason": reason,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(WALLET_PATH, "w") as f:
        json.dump(wallet, f, indent=4)
    
    print(f"🪙  [S25_FINANCE] Berhasil Mencetak: {amount} IND-EUR")
    print(f"📝 [REASON] {reason}")

if __name__ == "__main__":
    # Pencetakan 1000 IND-EUR pertama untuk likuiditas awal
    issue_ind_eur(1000, "Initial Liquidity for UMKM Export Sync")
