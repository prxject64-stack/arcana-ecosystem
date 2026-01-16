#!/bin/bash
# 2026 Sovereign Environment Initializer

# 1. Activate Python Virtual Environment
if [ -d "$HOME/arcana-ecosystem/venv" ]; then
    source "$HOME/arcana-ecosystem/venv/bin/activate"
    echo "[✔] Python Sovereign Environment: ACTIVE"
else
    echo "[!] Error: venv not found. Run the setup script first."
fi

# 2. Link Rust/Cargo Path
if [ -f "$HOME/.cargo/env" ]; then
    . "$HOME/.cargo/env"
    echo "[✔] Rust Industrial Toolchain: LINKED"
else
    echo "[!] Error: Rustup not found."
fi

# 3. Final Verification
python_version=$(python3 --version)
rust_version=$(rustc --version)
echo "[*] System Ready | $python_version | $rust_version"
