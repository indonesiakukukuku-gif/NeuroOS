import os, socket, threading, random, json, time, re, subprocess

NODE_NAME = os.getenv("NODE_NAME","node_founder")
PORT = 9003
PEERS = set()
LEDGER_FILE = "sovereign_ledger.json"
CELLS_FILE = "neurosphere_core.rgl"

CELLS = {}
LEDGER = {}

def speak(text):
    try:
        subprocess.run(["termux-tts-speak", text], stderr=subprocess.DEVNULL)
    except: pass

def load_cells(auto_save=True):
    global CELLS
    CELLS.clear()
    with open(CELLS_FILE,"r") as f:
        content = f.read()
        found_cells = re.findall(r'cell (\w+) \{(.*?)\}', content, re.DOTALL)
        for cell_name, cell_body in found_cells:
            pulses = re.findall(r'pulse (\w+)\((.*?)\)', cell_body)
            CELLS[cell_name] = [p[0] for p in pulses]
            if cell_name=="EvolutionCore_S21" and "self_optimize" not in CELLS[cell_name]:
                CELLS[cell_name].append("self_optimize")
                print("🛠️ Pulse self_optimize ditambahkan ke EvolutionCore_S21")
                if auto_save:
                    save_rgl(cell_name, CELLS[cell_name])

def save_rgl(cell_name, pulses):
    with open(CELLS_FILE,"r") as f:
        content = f.read()
    pattern = rf'(cell {cell_name} \{{)(.*?)(\}})'
    replacement = rf'\1\n' + ''.join([f'    pulse {p}()\n' for p in pulses]) + r'\3'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(CELLS_FILE,"w") as f:
        f.write(new_content)
    print(f"💾 RGL updated: {cell_name} pulses saved")

def load_ledger():
    global LEDGER
    with open(LEDGER_FILE,"r") as f: data = json.load(f)
    founder = data.get("founder","INDIE-Founder")
    LEDGER[founder] = data.get("anchor_value_base",100000)
    for p in data.get("pioneers",[]):
        iid=p.get("iid")
        LEDGER[iid]=1000
    return data

def auto_fix_ledger(data):
    founder = data.get("founder","INDIE-Founder")
    if founder not in LEDGER: LEDGER[founder]=data.get("anchor_value_base",100000)
    for p in data.get("pioneers",[]):
        iid=p.get("iid")
        if iid not in LEDGER:
            LEDGER[iid]=1000

def save_ledger():
    with open("ledger_backup.json","w") as f:
        json.dump(LEDGER,f,indent=2)

def handle_client(conn,addr):
    try:
        data=conn.recv(1024).decode()
        if data:
            msg=json.loads(data)
            if msg.get("type")=="hello": PEERS.add(msg.get("node"))
    except Exception as e:
        print("Network error:", e)
    finally:
        conn.close()

def server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",PORT))
    s.listen()
    print(f"🌐 Listening on port {PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client,args=(conn,addr)).start()

def send_hello(ip,port,node_name):
    try:
        s=socket.socket()
        s.connect((ip,port))
        msg=json.dumps({"type":"hello","node":node_name})
        s.send(msg.encode())
        s.close()
    except: pass

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

def gossip_pulse():
    nodes=["node_alpha","node_beta","node_gamma","node_delta"]
    new_node=random.choice(nodes)
    if new_node not in PEERS:
        PEERS.add(new_node)
        exec_cell("SocialHub_S12","broadcast_kindness")
    else:
        exec_cell("EvolutionCore_S21","self_optimize")

def exec_cell(cell,pulse):
    if cell in CELLS and pulse in CELLS[cell]:
        print(f"⚡ [EXEC] {cell}.{pulse} fired!")
        return True
    else:
        print(f"⚠ Pulse not found: {cell}.{pulse}")
        return False

def draw_dashboard():
    os.system("clear")
    print("="*70)
    print(f"🌀 NEUROOS v3.3 ULTIMATE | Node: {NODE_NAME}")
    print("="*70)
    print(f"[Cells Online] : {', '.join(CELLS.keys())}")
    print(f"[Peers Known]  : {len(PEERS)} nodes")
    print(f"[Ledger Snapshot]:")
    for k,v in LEDGER.items():
        bar="█"*(v//5000)
        print(f"{k:15} | {v:8} IND | {bar}")
    print("="*70)
    print(f"📡 Last Sync: {time.ctime()}\n")

print("🚀 NeuroOS v3.3 Ultimate Booting...")
data=load_ledger()
auto_fix_ledger(data)
load_cells(auto_save=True)
threading.Thread(target=server,daemon=True).start()
subprocess.run(["termux-tts-speak","NeuroOS v3.3 Ultimate initialized"],stderr=subprocess.DEVNULL)

while True:
    load_cells(auto_save=True)
    auto_fix_ledger(data)
    distribution_cycle()
    gossip_pulse()
    draw_dashboard()
    time.sleep(5)
