/**
 * NEURO-OS API BRIDGE (Project: indienation-stable-coin)
 * Currency Fix: €1 = Rp19,691.33
 */

const PROJECT_ID = "indienation-stable-coin";
const BASE_URL = `https://${PROJECT_ID}-default-rtdb.firebaseio.com`;

export default async function handler(req, res) {
    const { iid } = req.query;

    if (!iid) return res.status(400).json({ error: "IID Required" });

    const iidNum = parseInt(iid.split('-')[2]);
    let shardName;
    
    // Logika Sharding
    if (iidNum <= 100) {
        shardName = "Database"; // Lokasi Genesis 1-100 Anda
    } else {
        const shardNum = Math.floor((iidNum - 1) / 1000) + 1;
        shardName = `shard_${String(shardNum).padStart(2, '0')}`;
    }

    try {
        const response = await fetch(`${BASE_URL}/shards/${shardName}/${iid}.json`);
        const data = await response.json();

        if (!data) return res.status(404).json({ error: "Sovereign ID not found" });

        res.status(200).json({
            identity: "NEUROSPHERE SOVEREIGN CITIZEN",
            iid: data.iid,
            status: "ACTIVE",
            anchor_value: {
                eur: "€100.000",
                idr: "Rp1.969.133.000"
            },
            rate: "Rp19.691,33",
            gateway: "Secure Node: bemmagz-stable-coin"
        });
    } catch (err) {
        res.status(500).json({ error: "Gateway Timeout" });
    }
}
