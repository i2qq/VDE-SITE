# Changelog 2: Vercel Production Configuration, CNAME Removal & Deployment Guide

## Summary
Migrated `VDE-SITE` deployment architecture from GitHub Pages static CNAME to Vercel production hosting for `vopple.uk`:

1. **Vercel Infrastructure (`vercel.json`)**:
   - Configured `cleanUrls: true` and edge rewrite `/install` -> `/install.sh`.
   - Set custom response headers for `/install.sh` forcing `Content-Type: text/plain; charset=utf-8`, CORS origin `*`, and 60-second caching.
   - Added security headers (`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `X-XSS-Protection`).

2. **CNAME Removal**:
   - Removed GitHub Pages legacy `CNAME` file to prevent domain clash with external hosting.

3. **IONOS & Vercel Deployment Documentation (`VERCEL.md`)**:
   - Authored complete walkthrough detailing Vercel project import and DNS record mapping (`A` record to `76.76.21.21` and `CNAME` for `www` to `cname.vercel-dns.com`) inside IONOS control panel.

4. **Test Suite Refresh**:
   - Updated `tests/verify_site.py` to validate `vercel.json` JSON schema and header rules (100% PASS).
