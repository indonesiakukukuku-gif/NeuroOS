#!/bin/bash
# Pindahkan semua file Proof dari folder download internal ke folder evidence
# (Asumsi menggunakan folder download Termux/Shared)
mv ~/storage/downloads/Proof_*.txt ~/indienation-neurosphere/evidence/ 2>/dev/null
echo "Evidence Updated: $(ls evidence | wc -l) files secured."
