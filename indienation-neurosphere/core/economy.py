class EconomyEngine:
    def __init__(self):
        self.bonus_rate = 1.25  # Penjual terima 125%
        self.discount_rate = 0.80 # Pembeli bayar 80%

    def calculate_impact(self, price):
        buyer_pays = price * self.discount_rate
        merchant_gets = price * self.bonus_rate
        subsidy = merchant_gets - buyer_pays
        return buyer_pays, merchant_gets, subsidy

if __name__ == "__main__":
    engine = EconomyEngine()
    bp, mg, sub = engine.calculate_impact(10000)
    print(f"Harga Real: 10.000 | Pembeli Bayar: {bp} | Penjual Terima: {mg}")
    print(f"Sistem Menanggung: {sub} (IND-EUR)")
