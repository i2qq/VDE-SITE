# Changelog 1: Official VDE Website Deployment for vopple.uk with Direct Install Endpoint & CNAME

## Summary
Initial deployment of the official Victorious Desktop Environment (VDE) web platform on `vopple.uk`:

1. **Custom Domain & CNAME**:
   - Configured `CNAME` targeting `vopple.uk` for GitHub Pages static hosting.
2. **Direct Web Installer Endpoint (`install.sh`)**:
   - Created root `install.sh` so users can run `curl -sSL https://vopple.uk/install.sh | sudo bash` or `wget -qO- https://vopple.uk/install.sh | sudo bash`.
   - Chains automatically to the master release script at `https://raw.githubusercontent.com/i2qq/VDE/main/install.sh`.
3. **Full Desktop Showcase Platform (`index.html`, `style.css`, `main.js`)**:
   - High-contrast Dark Mica aesthetic with acrylic glassmorphism styling (`#18181b`, `#09090b`, `#38bdf8`).
   - One-click copy terminal installer widget supporting both `wget` and `curl`.
   - Showcase cards and vector SVG icon links for all 12 native applications (Crossmanager, Crossings, Crosspad, Crossminal, Crossaint, Crosstos, Crossculator, Crosslock, Cross Bin, Cross Narrator, Crossnip, Crosslink).
   - Interactive keybindings and quadrant window snapping cheatsheet.
4. **Site Verification Test Suite**:
   - Created `tests/verify_site.py` validating CNAME, script routing, HTML structure, and asset integrity (100% PASS).
