#!/bin/bash
BASE="https://indienation-tm-default-rtdb.asia-southeast1.firebasedatabase.app/pioneers.json"
DATA='{
  "IID-011": {"name": "PURWANTORO", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-012": {"name": "MARSELUS HASAN", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-013": {"name": "KIKI KESTURI", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-014": {"name": "DIAVATCHE BOGUI EUGÈNE", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-015": {"name": "MIFTAHUDIN", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-016": {"name": "KASTIM", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-017": {"name": "MEIRISKA", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-018": {"name": "RASHEED ABIODUN O. GBAIYE", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-019": {"name": "LUGARD JUMBO", "balance_eur": 1270, "enpe": 0, "luv": 0},
  "IID-020": {"name": "HERI HERYANTO", "balance_eur": 1270, "enpe": 0, "luv": 0}
}'
curl -X PUT -d "$DATA" "$BASE"
