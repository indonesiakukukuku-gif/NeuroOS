import requests, json, time, hashlib

# KONFIGURASI CORE
DB_BASE = "https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/"
SECRET_KEY = "NEURO-FOUNDER-SECRET-2026" # Kunci kedaulatan

def execute_sovereign_tx(sender_id, receiver_id, amount):
    # 1. READ: Cek Saldo Pengirim
    sender_data = requests.get(f"{DB_BASE}pioneers/{sender_id}.json").json()
    current_bal = sender_data.get("balance_eur", 0)
    
    if current_bal < amount:
        print(f"❌ {sender_id}: Dana Tidak Cukup!")
        return False

    # 2. CALC: Hitung Saldo Baru
    new_bal_sender = current_bal - amount
    
    # 3. HASH: Generate Signature Auralang
    tx_timestamp = int(time.time() * 1000)
    signature = hashlib.sha256(f"{sender_id}{amount}{tx_timestamp}{SECRET_KEY}".encode()).hexdigest()

    # 4. WRITE: Atomic-like Update (Multi-node Patch)
    tx_data = {
        "from": sender_id,
        "to": receiver_id,
        "amount": amount,
        "timestamp": tx_timestamp,
        "sig": signature,
        "status": "VERIFIED_BY_AI_GUARD"
    }
    
    # Update Ledger & Update Saldo secara simultan
    requests.post(f"{DB_BASE}ledger.json", json=tx_data)
    requests.patch(f"{DB_BASE}pioneers/{sender_id}.json", json={"balance_eur": new_bal_sender})
    
    # Tambahkan saldo ke penerima
    receiver_data = requests.get(f"{DB_BASE}pioneers/{receiver_id}.json").json()
    new_bal_receiver = receiver_data.get("balance_eur", 0) + amount
    requests.patch(f"{DB_BASE}pioneers/{receiver_id}.json", json={"balance_eur": new_bal_receiver})

    print(f"✅ TX: {sender_id} -> {receiver_id} | AMT: {amount} | SIG: {signature[:8]}...")
    return True

if __name__ == "__main__":
    pioneers = ["IID-011", "IID-012", "IID-013", "IID-014", "IID-015", "IID-016", "IID-017", "IID-018", "IID-019", "IID-020"]
    print("🧠 AURALANG SOVEREIGN ENGINE STARTING...")
    
    # Simulasi Estafet 9 Putaran Sempurna
    for round_num in range(1, 10):
        for i in range(len(pioneers)):
            sender = pioneers[i]
            receiver = pioneers[(i + 1) % len(pioneers)]
            execute_sovereign_tx(sender, receiver, 10.0)
            time.sleep(0.05) # Kecepatan tinggi namun stabil
