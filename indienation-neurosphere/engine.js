import dotenv from 'dotenv';
import { createClient } from '@supabase/supabase-js';

dotenv.config();

const supabase = createClient(
    process.env.SUPABASE_URL || "", 
    process.env.SUPABASE_KEY || ""
);

export async function deployPioneer(country = 'GLOBAL') {
    if (!process.env.SUPABASE_URL) {
        console.error("❌ ERROR: File .env tidak terbaca atau kosong.");
        return;
    }
    
    console.log(`[PROCESS] Connecting to NeuroSphere Vault...`);
    const { data, error } = await supabase
        .from('identities')
        .insert([{ country_code: country }])
        .select();

    if (error) {
        console.error('❌ DATABASE_ERROR:', error.message);
        return;
    }

    console.log(`✨ PULSE DETECTED: ${data[0].iid} [${country}]`);
    console.log(`💰 ANCHOR ACTIVE: €${data[0].anchor_balance}`);
    return data[0];
}
