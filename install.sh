#!/usr/bin/env bash
# ==============================================================================
# Victorious Desktop Environment (VDE) Web Installer
# Official Domain: vopple.uk
# Master Repository: https://github.com/i2qq/VDE
# License: Victorian Privacy License (VPL) - Strict Zero Telemetry
# ==============================================================================

set -e

INSTALL_URL="https://raw.githubusercontent.com/i2qq/VDE/main/install.sh"

echo "=========================================================="
echo " Fetching Victorious Desktop Environment (VDE)..."
echo " Official Source: vopple.uk -> github.com/i2qq/VDE"
echo "=========================================================="

if command -v curl >/dev/null 2>&1; then
    exec curl -fsSL "$INSTALL_URL" | bash -s -- "$@"
elif command -v wget >/dev/null 2>&1; then
    exec wget -qO- "$INSTALL_URL" | bash -s -- "$@"
else
    echo "Error: Neither curl nor wget is installed on this machine." >&2
    echo "Install curl or wget first: sudo apt update && sudo apt install -y curl" >&2
    exit 1
fi
