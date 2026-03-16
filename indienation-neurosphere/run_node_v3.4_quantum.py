import socket, threading, random, json, time, os, re, subprocess
from datetime import datetime

# --- CONFIG ---
NODE_NAME = "node_founder"
PORT = 9004
PEERS = set()
LEDGER_FILE = "sovereign_ledger.json"
CELLS = {}

# --- SYSTEM FUNCTIONS ---
def speak(text):
    try: subprocess.run(["termux-tts-speak", text], stderr=subprocess.DEVNULL)
    except: pass

def load_ledger():
    global LEDGER
    with open(LEDGER_FILE,"r") as f:
        data=json.load(f)
    return data

def auto_fix_ledger(data):
    global LEDGER
    founder = data.get("founder","INDIE-Founder")
    if founder not in LEDGER: LEDGER[founder]=data.get("anchor_value_base",100000)
    for pioneer in data.get("pioneers",[]):
        iid=pioneer.get("iid")
        if iid and iid not in LEDGER: LEDGER[iid]=1000

def save_ledger():
    with open("ledger_backup.json","w") as f: json.dump(LEDGER,f,indent=2)

def load_cells(auto_save=False):
    global CELLS
    with open("neurosphere_core.rgl","r") as f:
        content=f.read()
    found_cells=re.findall(r'cell (\w+) \{(.*?)\}', content,re.DOTALL)
    for cell_name, cell_body in found_cells:
        pulses=re.findall(r'pulse (\w+)\((.*?)\)', cell_body)
        CELLS[cell_name]=[p[0] for p in pulses]
    if auto_save:
        with open("neurosphere_core.rgl","w") as f: f.write(content)

# --- PULSES & EXEC ---
def exec_cell(cell,pulse):
    if cell in CELLS and pulse in CELLS[cell]:
        print(f"⚡ [EXEC] {cell}.{pulse} fired!")
        return True
    else:
        print(f"⚠ Pulse not found: {cell}.{pulse}")
        return False

def distribution_cycle():
    sender="INDIE-Founder"
    receiver=random.choice(list(LEDGER.keys()))
    if sender==receiver: return
    amt=100
    if LEDGER.get(sender,0)>=amt:
        LEDGER[sender]-=amt
        LEDGER[receiver]+=amt
        save_ledger()
        exec_cell("DistributionCell_S25","distribute_value")
        print(f"💰 {amt} IND {sender} → {receiver}")

def gossip_pulse():
    nodes=["node_alpha","node_beta","node_gamma","node_delta"]
    new_node=random.choice(nodes)
    if new_node not in PEERS:
        PEERS.add(new_node)
        exec_cell("SocialHub_S12","broadcast_kindness")
        print(f"[GOSSIP] Handshake with {new_node}")
    else: exec_cell("EvolutionCore_S21","self_optimize")

# --- NETWORK ---
def handle_client(conn,addr):
    try:
        data=conn.recv(1024).decode()
        if data:
            msg=json.loads(data)
            if msg.get("type")=="hello": PEERS.add(msg.get("node"))
    except Exception as e: print("Network error:",e)
    finally: conn.close()

def server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",PORT))
    s.listen()
    print(f"🌐 Listening on port {PORT}")
    while True:
        conn, addr=s.accept()
        threading.Thread(target=handle_client,args=(conn,addr)).start()

# --- DASHBOARD ---
def draw_dashboard():
    os.system("clear")
    print("="*80)
    print(f"🌀 NEUROOS v3.4 QUANTUM | Node: {NODE_NAME}")
    print("="*80)
    print(f"[Cells Online]: {', '.join(CELLS.keys())}")
    print(f"[Peers Known]: {len(PEERS)} nodes")
    print(f"[Ledger Snapshot]:")
    for k,v in LEDGER.items():
        bar="█"*(v//5000)
        print(f"{k:15} | {v:8} IND | {bar}")
    print("="*80)
    print(f"📡 Last Sync: {datetime.now()}\n")

# --- BOOTSTRAP ---
print("🚀 NeuroOS v3.4 Quantum Booting...")
data=load_ledger()
LEDGER=data
auto_fix_ledger(data)
load_cells(auto_save=True)
threading.Thread(target=server,daemon=True).start()
speak("NeuroOS v3.4 Quantum initialized")

# --- MAIN LOOP ---
while True:
    auto_fix_ledger(data)
    load_cells(auto_save=True)
    distribution_cycle()
    gossip_pulse()
    draw_dashboard()
    time.sleep(5)
