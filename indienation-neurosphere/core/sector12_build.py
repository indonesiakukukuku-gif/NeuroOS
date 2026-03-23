import json
import os

def get_construction_progress():
    sync_path = os.path.expanduser("~/indienation-neurosphere/core/sync_state.json")
    try:
        with open(sync_path, 'r') as f:
            data = json.load(f)
            focus = data['sentiment_profile']['Focus']
    except:
        focus = 10 # Default focus jika file tidak ditemukan

    # Progres konstruksi ditentukan oleh level Focus
    # Semakin tinggi focus, semakin cepat pembangunan
    progress = min(100, focus * 1.5) 
    
    # ASCII Art Generator untuk Gedung
    def draw_building(p):
        height = int(p / 10)
        building = ""
        for i in range(10 - height): building += "          \n"
        for i in range(height): building += "  | [][][|  \n"
        building += "  |______|_ \n"
        return building

    return round(progress, 2), draw_building(progress)

if __name__ == "__main__":
    p, b = get_construction_progress()
    print(f"Progress: {p}%")
    print(b)
