#!/usr/bin/env python3
"""
VDE-SITE Verification Test Suite
Verifies static site integrity, CNAME routing, install script validity, and assets.
"""

import os
import sys

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_cname():
    cname_path = os.path.join(SITE_DIR, "CNAME")
    assert os.path.exists(cname_path), "CNAME file missing!"
    with open(cname_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    assert content == "vopple.uk", f"Expected 'vopple.uk', got '{content}'"
    print("[OK] CNAME verified: vopple.uk")

def test_install_script():
    install_path = os.path.join(SITE_DIR, "install.sh")
    assert os.path.exists(install_path), "install.sh missing!"
    with open(install_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "https://raw.githubusercontent.com/i2qq/VDE/main/install.sh" in content, "install.sh does not target master VDE repo!"
    assert "#!/usr/bin/env bash" in content, "Missing bash shebang!"
    print("[OK] install.sh verified and points to master VDE installer")

def test_html_and_assets():
    index_path = os.path.join(SITE_DIR, "index.html")
    assert os.path.exists(index_path), "index.html missing!"
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    assert "vopple.uk" in html, "vopple.uk not in index.html"
    assert "assets/css/style.css" in html, "Missing style.css reference"
    assert "assets/js/main.js" in html, "Missing main.js reference"
    assert "assets/images/hero-wallpaper.png" in html, "Missing hero-wallpaper.png reference"

    required_assets = [
        "assets/css/style.css",
        "assets/js/main.js",
        "assets/images/hero-wallpaper.png",
        "assets/images/vde_logo.png"
    ]
    for rel_path in required_assets:
        full_path = os.path.join(SITE_DIR, rel_path)
        assert os.path.exists(full_path), f"Asset missing: {rel_path}"
        assert os.path.getsize(full_path) > 0, f"Asset empty: {rel_path}"
        print(f"[OK] Asset exists: {rel_path} ({os.path.getsize(full_path)} bytes)")

    apps = [
        "crossmanager", "crossings", "crosspad", "crossminal",
        "crossaint", "crosstos", "crossculator", "crosslock",
        "crossbin", "crossnarrator", "crossnip", "crosslink"
    ]
    for app in apps:
        assert app in html, f"App {app} missing in index.html!"
    print(f"[OK] All {len(apps)} native apps documented in index.html")

if __name__ == "__main__":
    print("[1/3] Checking CNAME...")
    test_cname()
    print("[2/3] Checking install.sh...")
    test_install_script()
    print("[3/3] Checking HTML and Assets...")
    test_html_and_assets()
    print("\n[SUCCESS] VDE-SITE static site verified 100% healthy.")
