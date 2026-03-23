class IIDMathematics:
    def __init__(self):
        self.total_enpe = 100 * 10**12 # 100 Trillion
        self.total_luv = 100 * 10**12  # 100 Trillion
        self.founder_allocation = 0.20 # 20%
        
    def validate_distribution(self, user_count):
        # Memastikan alokasi 1 juta per orang tidak mengganggu pool publik
        founder_share = self.total_luv * self.founder_allocation
        required_for_people = user_count * 1_000_000
        
        if required_for_people <= (founder_share * 0.05): # Hanya ambil dari porsi founder
            return "✅ Allocation Valid: Founder Pool used."
        else:
            return "⚠️ Warning: Potential Conflict of Interest detected!"

if __name__ == "__main__":
    check = IIDMathematics()
    print(check.validate_distribution(1_000_000))
