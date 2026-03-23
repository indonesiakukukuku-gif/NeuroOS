class AIGuard:
    def __init__(self):
        self.status = "Vigilant"

    def track_activity(self, iid, activity):
        # Logika tracing aktivitas negatif (Narkotik/Kriminal)
        if activity in ["narcotics", "criminal", "violence"]:
            return self.apply_sanction(iid)
        return "Safe"

    def apply_sanction(self, iid):
        return f"🚨 ALERT: IID {iid} Flagged. Parental Wallet SUSPENDED for 3 Months."

if __name__ == "__main__":
    guard = AIGuard()
    print(guard.track_activity("IID-021-999", "narcotics"))
