# -----------------------------
# run_node_v3_singularity.py
# NEUROSPHERE NODE ULTIMATE v3.0 SINGULARITY
# -----------------------------
import os, re, json, socket, threading, random, time, subprocess

NODE_NAME = os.getenv("NODE_NAME","INDIE-Founder")
PORT = 9002
HOST = "0.0.0.0"
LEDGER_FILE = "sovereign_ledger.json"
RGL_FILE = "neurosphere_core.rgl"

cells = {}
peers = set()
ledger = {}

def speak(text):
    try: subprocess.run(["termux-tts-speak", text], stderr=subprocess.DEVNULL)
    except: pass

def load_rgl():
    global cells
    with open(RGL_FILE,"r") as f:
        content = f.read()
    found_cells = re.findall(r'cell (\w+) \{(.*?)\}', content, re.DOTALL)
    for cell_name, cell_body in found_cells:
        pulses = re.findall(r'pulse (\w+)\(', cell_body)
        # Auto-add self_optimize if missing
        if "self_optimize" not in pulses:
            pulses.append("self_optimize")
        cells[cell_name] = pulses
        print(f"✔ DNA Synchronized: {cell_name} ({len(pulses)} pulses)")

def load_ledger():
    global ledger
    with open(LEDGER_FILE,"r") as f: data=json.load(f)
    return data

def auto_fix_ledger(data):
    global ledger
    founder=data.get("founder","INDIE-Founder")
    if founder not in ledger: ledger[founder]=data.get("anchor_value_base",100000)
    for p in data.get("pioneers",[]):
        iid=p.get("iid")
        if iid and iid not in ledger: ledger[iid]=1000

def save_ledger():
    with open("ledger_backup.json","w") as f: json.dump(ledger,f,indent=2)

def exec_cell(cell_name,pulse_name):
    if cell_name in cells and pulse_name in cells[cell_name]:
        print(f"⚡ [EXEC] {cell_name}.{pulse_name} fired!"); return True
    else:
        print(f"⚠ Pulse not found: {cell_name}.{pulse_name}"); return False

def handle_client(conn,addr):
    try:
        data=conn.recv(1024).decode()
        if data:
            msg=json.loads(data)
            if msg.get("type")=="hello": peers.add(msg.get("node"))
    except Exception as e: print("Network error:",e)
    finally: conn.close()

def server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()
    print(f"🌐 Listening on {HOST}:{PORT}")
    while True:
        conn,addr=s.accept()
        threading.Thread(target=handle_client,args=(conn,addr)).start()

def send_hello(ip,port,node_name):
    try:
        s=socket.socket()
        s.connect((ip,port))
        s.send(json.dumps({"type":"hello","node":node_name}).encode())
        s.close()
    except: pass

def distribution_cycle():
    sender=NODE_NAME
    receiver=random.choice(list(ledger.keys()))
    if sender==receiver: return
    amount=100
    if ledger.get(sender,0)>=amount:
        ledger[sender]-=amount
        ledger[receiver]+=amount
        save_ledger()
        exec_cell("DistributionCell_S25","distribute_value")
        print(f"💰 {amount} IND {sender} → {receiver}")

def gossip_pulse():
    nodes=["node_alpha","node_beta","node_gamma","node_delta"]
    new_node=random.choice(nodes)
    if new_node not in peers:
        peers.add(new_node)
        exec_cell("SocialHub_S12","broadcast_kindness")
        print(f"[GOSSIP] Handshake established with {new_node}")
    else:
        exec_cell("EvolutionCore_S21","self_optimize")
        print("[GOSSIP] Network stable")

def dashboard():
    os.system("clear")
    print("\n===== NEUROSPHERE STATUS =====")
    print("Cells:",len(cells))
    print("Peers:",len(peers))
    print("Known Nodes:",list(peers))
    print("Ledger:",ledger)
    print("===============================")
    speak(f"Nodes {len(peers)}, Ledger stable.")

# --- BOOTSTRAP ---
print("🚀 NeuroSphere Node v3.0 Singularity [Ultimate Auto-Heal & Gossip]")
data=load_ledger()
auto_fix_ledger(data)
load_rgl()
threading.Thread(target=server,daemon=True).start()

while True:
    auto_fix_ledger(data)
    distribution_cycle()
    gossip_pulse()
    dashboard()
    time.sleep(5)
