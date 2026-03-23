import json
import sys

def draw_bar(day):
    length = 20
    # Memastikan progres maksimal di angka 365
    progress_day = min(day, 365)
    filled = int(length * progress_day // 365)
    bar = "█" * filled + "░" * (length - filled)
    percent = (progress_day / 365) * 100
    return f"[{bar}] {percent:.1f}%"

def calculate_relay(current_day):
    day_1 = 1000
    daily_rate = 270
    final_day_payout = 990
    total_target = 100000

    if current_day == 1:
        balance = day_1
        payout_today = day_1
    elif 2 <= current_day <= 364:
        balance = day_1 + ((current_day - 1) * daily_rate)
        payout_today = daily_rate
    elif current_day == 365:
        balance = total_target
        payout_today = final_day_payout
    else:
        balance = total_target
        payout_today = 0

    return {
        "visual_progress": draw_bar(current_day),
        "fase": "KICK-OFF" if current_day == 1 else "RUNNING" if current_day < 365 else "ARCHIVED",
        "hari_ke": current_day,
        "penerimaan_hari_ini": f"€{payout_today}",
        "akumulasi_saldo": f"€{balance:,}",
        "sisa_hari": max(0, 365 - current_day),
        "target_akhir": f"€{total_target:,}"
    }

if __name__ == "__main__":
    try:
        # Mengambil input dari CLI
        day = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        print(json.dumps(calculate_relay(day), indent=4))
    except Exception as e:
        print(json.dumps({"error": f"Invalid input: {str(e)}"}))
