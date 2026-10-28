#!/usr/bin/env python3
"""
VDE-SITE Verification Test Suite
Verifies static site integrity, Vercel configuration, install script validity, and assets.
"""

import os
import sys
import json

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_vercel_config():
    vercel_path = os.path.join(SITE_DIR, "vercel.json")
    assert os.path.exists(vercel_path), "vercel.json file missing!"
    with open(vercel_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data.get("cleanUrls") is True, "cleanUrls not enabled!"
    assert any(h.get("source") == "/install.sh" for h in data.get("headers", [])), "Missing header for /install.sh"
    print("[OK] vercel.json verified and valid JSON")

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

def test_cloudflare_config():
    headers_path = os.path.join(SITE_DIR, "_headers")
    redirects_path = os.path.join(SITE_DIR, "_redirects")
    assert os.path.exists(headers_path), "_headers file missing!"
    assert os.path.exists(redirects_path), "_redirects file missing!"
    with open(headers_path, "r", encoding="utf-8") as f:
        headers_content = f.read()
    assert "/install.sh" in headers_content, "Missing /install.sh in _headers"
    assert "Content-Type: text/plain" in headers_content, "Missing Content-Type header in _headers"
    with open(redirects_path, "r", encoding="utf-8") as f:
        redirects_content = f.read()
    assert "/install" in redirects_content and "/install.sh" in redirects_content, "Missing /install rewrite in _redirects"
    print("[OK] Cloudflare Pages _headers and _redirects verified")

if __name__ == "__main__":
    print("[1/4] Checking vercel.json...")
    test_vercel_config()
    print("[2/4] Checking Cloudflare Pages config...")
    test_cloudflare_config()
    print("[3/4] Checking install.sh...")
    test_install_script()
    print("[4/4] Checking HTML and Assets...")
    test_html_and_assets()
    print("\n[SUCCESS] VDE-SITE static site verified 100% healthy.")
