# VDE-SITE — Vercel Deployment & IONOS DNS Guide

Deploying the official **Victorious Desktop Environment (VDE)** website and web installer to **Vercel** with custom domain **`vopple.uk`** or **`vde.vopple.uk`** on **IONOS**.

---

## 🚀 1. Deploy Repository to Vercel

1. Log into your [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **Add New...** > **Project**.
3. Import **`i2qq/VDE-SITE`**.
4. Framework Preset: **Other** (Static HTML/CSS/JS).
5. Root Directory: `./` (default).
6. Click **Deploy**.

---

## 🌐 2. Add Custom Domain in Vercel

In your Vercel project, go to **Settings** > **Domains**:

- **Option A (Subdomain `vde.vopple.uk`)**:
  - Enter **`vde.vopple.uk`** and click **Add**.
  - Target: `cname.vercel-dns.com`
- **Option B (Apex `vopple.uk`)**:
  - Enter **`vopple.uk`** and click **Add**.
  - Vercel will prompt for `@` (A record) and `www` (CNAME).

---

## 🛠️ 3. Configure DNS in IONOS

From your IONOS dashboard (**Domains & SSL**):

### For Subdomain `vde.vopple.uk`:
1. Go to **vde.vopple.uk** (or `vopple.uk` > **DNS**).
2. Click **Add record**:
   - **Type**: `CNAME`
   - **Host Name**: `vde`
   - **Points to**: `cname.vercel-dns.com`
   - **TTL**: `1 hour` &rarr; Click **Save**.

### For Root Domain `vopple.uk`:
1. Under **vopple.uk** > **DNS**, click **Add record**:
   - **Type**: `A`
   - **Host Name**: `@`
   - **Points to**: `76.76.21.21`
   - **TTL**: `1 hour` &rarr; Click **Save**.
2. For `www`:
   - **Type**: `CNAME`
   - **Host Name**: `www`
   - **Points to**: `cname.vercel-dns.com` &rarr; Click **Save**.

---

## ⚡ 4. Verification & 1-Command Installer

Once DNS resolves (typically 1–2 minutes):
- **Live Website**:
  - `https://vde.vopple.uk` (or `https://vopple.uk`)
- **Direct Web Installer**:
  ```bash
  wget -qO- https://vde.vopple.uk/install.sh | sudo bash
  ```
  *or:*
  ```bash
  curl -sSL https://vde.vopple.uk/install.sh | sudo bash
  ```
- **Clean Alias**:
  ```bash
  curl -sSL https://vde.vopple.uk/install | sudo bash
  ```
