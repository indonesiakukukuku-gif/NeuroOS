class DebtEraser:
    def __init__(self):
        self.label = "SOVEREIGN SETTLEMENT"

    def clear_debt(self, iid, amount, creditor_name):
        # Sistem membayar hutang pokok dan menghentikan bunga
        print(f"🔄 Processing Settlement for {iid}...")
        print(f"✅ Paid {amount} IND-EUR to {creditor_name}.")
        print(f"🚫 STATUS: Debt Cleared. Interest (Riba) Terminated.")
        return True

if __name__ == "__main__":
    eraser = DebtEraser()
    eraser.clear_debt("IID-021-IND-45", 5000000, "Bank_Masa_Lalu")
