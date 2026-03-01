const fs = require('fs');
const path = './logs/pioneer_ledger.json';

if (fs.existsSync(path)) {
    let data = JSON.parse(fs.readFileSync(path, 'utf8'));
    
    // Cegah penambahan jika sudah mencapai batas distribusi 100rb
    if (data.relay_state.current_day >= 365) {
        console.log("Distribusi Selesai: Anchor Value €100.000 telah tercapai.");
        process.exit();
    }

    data.relay_state.current_day += 1;

    // Logika Khusus Hari ke-365
    if (data.relay_state.current_day === 365) {
        // Tambahkan jatah harian terakhir (270) + Bonus Akhir (990)
        data.tm_structure.ind_eur_liquid += (270 + 990);
        data.relay_state.final_bonus_locked = 0; // Buka kunci bonus
        console.log("FINAL RELAY: Bonus €990 dicairkan!");
    } else {
        // Hari biasa (Day 2 sampai 364)
        data.tm_structure.ind_eur_liquid += 270;
    }

    data.last_update = new Date().toISOString();
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
    
    console.log(`Relay Day ${data.relay_state.current_day} Success!`);
    console.log(`Total Liquid: €${data.tm_structure.ind_eur_liquid}`);
}
