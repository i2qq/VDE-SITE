# Changelog 4: Cloudflare Pages Integration & Routing Configuration

**Date:** 2026-10-28
**Commit Tag:** `[changelog4]`
**Repository:** `i2qq/VDE-SITE`

### Summary of Changes:
1. **Cloudflare Pages Routing**:
   - Added `_headers` to enforce `Content-Type: text/plain; charset=utf-8`, CORS, and 300s cache headers for `/install.sh` and `/install`.
   - Added `_redirects` with HTTP 200 internal proxy rewrite from `/install` to `/install.sh`.
2. **Automated Verification**:
   - Updated `tests/verify_site.py` with `test_cloudflare_config()` to guarantee `_headers` and `_redirects` integrity on every build.
3. **Deployment Documentation**:
   - Updated `README.md` with step-by-step Cloudflare Pages connection and 1-click custom domain attachment guide.
