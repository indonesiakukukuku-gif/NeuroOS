import requests, hmac, hashlib, time

DB_BASE = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/"
SECRET_KEY = b"NEURO-FOUNDER-SECRET-2026"

pioneers = ["IID-011", "IID-012", "IID-013", "IID-014", "IID-015", "IID-016", "IID-017", "IID-018", "IID-019", "IID-020"]
amounts = [1, 3, 2, 4, 5, 7, 6, 9, 1]

def execute_precision_tx(sender_id, receiver_id, amount):
    try:
        # Fetch current data dengan default values untuk mencegah KeyError
        res = requests.get(f"{DB_BASE}pioneers/{sender_id}.json")
        sender = res.json() if res.json() else {}
        
        current_bal = sender.get("balance_eur", 1270.0) # Fallback ke 1270 jika null
        current_nonce = sender.get("nonce", 0)
        
        new_nonce = current_nonce + 1
        new_balance_sender = current_bal - amount

        # Cryptographic Signature
        payload = f"{sender_id}{receiver_id}{amount}{new_nonce}"
        signature = hmac.new(SECRET_KEY, payload.encode(), hashlib.sha256).hexdigest()

        # Update Sender
        requests.patch(f"{DB_BASE}pioneers/{sender_id}.json", json={
            "balance_eur": new_balance_sender,
            "nonce": new_nonce
        })

        # Update Receiver
        res_rec = requests.get(f"{DB_BASE}pioneers/{receiver_id}.json")
        receiver = res_rec.json() if res_rec.json() else {}
        new_balance_receiver = receiver.get("balance_eur", 1270.0) + amount
        
        requests.patch(f"{DB_BASE}pioneers/{receiver_id}.json", json={
            "balance_eur": new_balance_receiver
        })

        # Log to Ledger
        tx_id = f"NS-PRECISION-{int(time.time()*1000)}"
        tx_entry = {
            "from": sender_id, "to": receiver_id, "amount": amount,
            "nonce": new_nonce, "sig": signature, "status": "CONFIRMED",
            "type": "PRECISION_SHIFT",
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        requests.put(f"{DB_BASE}ledger/{tx_id}.json", json=tx_entry)
        
        print(f"✅ [{new_nonce}] {sender_id} --(€{amount})--> {receiver_id} | SIG: {signature[:8]}")
        return True
    except Exception as e:
        print(f"⚠️ Gagal pada {sender_id}: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎯 RE-STARTING PRECISION SHIFT (SELF-HEALING ACTIVE)...")
    for i in range(len(amounts)):
        execute_precision_tx(pioneers[i], pioneers[i+1], amounts[i])
        time.sleep(0.2)
    print("🛡️ PROTOKOL SELESAI. SILAKAN CEK MASTER PORTAL.")
