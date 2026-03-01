import express from 'express';
import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';

dotenv.config();
const app = express();
const port = 3000;
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

app.get('/api/v1/leaderboard', async (req, res) => {
    const { data } = await supabase
        .from('tm_vault')
        .select('iid, luv_balance, nft_metadata')
        .order('luv_balance', { ascending: false })
        .limit(10);
    res.json(data);
});

app.get('/api/v1/stats', async (req, res) => {
    const { data: identities } = await supabase.from('identities').select('count');
    res.json({ total_citizens: identities[0]?.count || 0, status: 'SOVEREIGN' });
});

app.listen(port, () => {
    console.log(`🚀 NeuroSphere API Live at http://localhost:${port}`);
});
