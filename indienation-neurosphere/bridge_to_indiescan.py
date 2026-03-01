import requests
import json

# Konfigurasi Akses 1001NDONESIA
# Ganti URL dan KEY dengan data dari dashboard Supabase Anda
SUPABASE_URL = "https://your-project-id.supabase.co/rest/v1/sovereign_ledger"
SUPABASE_KEY = "your-anon-key"

def log_transaction_to_indiescan(tx_hash, identity, brand, amount, metadata):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    payload = {
        "tx_hash": tx_hash,
        "source_identity": identity,
        "brand_entity": brand,
        "amount_ind_eur": amount,
        "metadata": metadata,
        "status": "VALIDATED_BY_AI_GUARD"
    }
    
    try:
        response = requests.post(SUPABASE_URL, headers=headers, data=json.dumps(payload))
        if response.status_index() in [200, 201]:
            print(f"✅ Success: Logged to IndieScan via 1001NDONESIA Investment")
            print(f"🔗 Hash: {tx_hash}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")

if __name__ == "__main__":
    # Test Run: Acquisition 1001NDONESIA Properties
    log_transaction_to_indiescan(
        tx_hash="0x1001_DXB_PROPS_001",
        identity="00000009",
        brand="1001NDONESIA Properties",
        amount=250000,
        metadata="Dubai Property Acquisition - Alpha Sector"
    )
