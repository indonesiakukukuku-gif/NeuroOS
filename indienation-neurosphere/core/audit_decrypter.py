import sys
import os
from ghost_vault import decrypt_data

# @path: ~/indienation-neurosphere/core/audit_decrypter.py
# @authority: IID-021+

def audit_log_entry(vault_ref):
    try:
        # Menghapus '...' jika input diambil dari tampilan dashboard
        clean_ref = vault_ref.replace("...", "")
        decrypted = decrypt_data(clean_ref)
        print(f"\n🔓 [AUDIT_SUCCESS]")
        print(f"📄 Raw Data: {decrypted}")
    except Exception as e:
        print(f"\n❌ [AUDIT_FAILED] Key Mismatch or Invalid Ref: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 audit_decrypter.py <VAULT_REF_STRING>")
    else:
        audit_log_entry(sys.argv[1])
