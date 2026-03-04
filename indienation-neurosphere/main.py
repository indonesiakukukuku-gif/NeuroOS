import os
from core.kernel import NeuroOSKernel
from core.guard import AIGuard
from core.economy import EconomyEngine

def run_system():
    # 1. Bangkitkan Kernel
    os_kernel = NeuroOSKernel()
    os_kernel.boot()

    # 2. Inisialisasi Engine
    guard = AIGuard()
    economy = EconomyEngine()

    # 3. Simulasi Transaksi Riil
    price = 10000
    bp, mg, sub = economy.calculate_impact(price)

    print("\n" + "="*40)
    print("      OPERATIONAL DASHBOARD")
    print("="*40)
    print(f"Economy Engine : ACTIVE (Merchant Bonus: 25%)")
    print(f"AI Guard       : VIGILANT (IID Tracking Active)")
    print("-" * 40)
    print(f"Sample Sector  : Food & Beverage")
    print(f"Transaction    : Original Price {price}")
    print(f"Buyer Pays     : {bp} (Disc 20%)")
    print(f"Merchant Gets  : {mg} (Bonus 25%)")
    print(f"System Cost    : {sub} IND-EUR")
    print("="*40)
    print("💓 Heartbeat: Stable | Unity Flow Active")

if __name__ == "__main__":
    run_system()
