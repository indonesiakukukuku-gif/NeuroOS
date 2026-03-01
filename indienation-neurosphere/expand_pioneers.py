import os

names = [
    "International_021", "International_022", "International_023", 
    "International_024", "International_025", "International_026", 
    "International_027", "International_028", "International_029", 
    "International_030"
]

cert_dir = "certificates"
os.makedirs(cert_dir, exist_ok=True)

for i, name in enumerate(names, 21):
    iid = f"IID_0{i}"
    file_path = os.path.join(cert_dir, f"CERTIFICATE_{iid}.txt")
    with open(file_path, "w") as f:
        f.write(f"NEUROSPHERE SOVEREIGN IDENTITY\n")
        f.write(f"------------------------------\n")
        f.write(f"HOLDER: {name}\n")
        f.write(f"IDENTITY-TYPE: International Masyarakat (inter6)\n")
        f.write(f"STATUS: ACTIVE\n")

print("Expansion complete: IID-021 to IID-030 created.")
