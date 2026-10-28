# VDE-SITE — Cloudflare Pages & Vercel Deployment Guide

Deploying the official **Victorious Desktop Environment (VDE)** website and web installer to **Cloudflare Pages** (or Vercel) with custom domain **`vopple.uk`** or **`vde.vopple.uk`**.

---

## ⚡ Recommended: Deploy with Cloudflare Pages

### 1. Connect Repository
1. In the [Cloudflare Dashboard](https://dash.cloudflare.com/), go to **Workers & Pages** > **Create application** > **Pages** tab.
2. Select **Connect to Git** and authorize your GitHub account (`i2qq`).
3. Select the repository **`i2qq/VDE-SITE`** and click **Begin setup**.

### 2. Configure Build & Output
- **Project name**: `vde-site` (or `vde`)
- **Production branch**: `main`
- **Framework preset**: `None`
- **Build command**: *(leave empty)*
- **Build output directory**: `/` (or leave default root `.`)
- Click **Save and Deploy**.

Cloudflare Pages automatically processes `_headers` and `_redirects` included in this repository to serve `/install.sh` and `/install` as raw plain text with proper cache controls.

### 3. Attach Custom Domain (`vde.vopple.uk` or `vopple.uk`)
1. In your Cloudflare Pages project, click **Custom domains** tab > **Set up a custom domain**.
2. Enter **`vde.vopple.uk`** (or `vopple.uk`).
3. Since your domain is onboarded to Cloudflare, Cloudflare will automatically configure the DNS CNAME record with 1 click! No manual DNS record creation needed.

---

## 🚀 Alternative: Deploy to Vercel

1. Log into your [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **Add New...** > **Project** and import **`i2qq/VDE-SITE`**.
3. Framework Preset: **Other** (Static HTML/CSS/JS), Root Directory: `./`.
4. Click **Deploy**.

### DNS Setup for Vercel
- For `vde.vopple.uk`: Add CNAME record pointing `vde` to `cname.vercel-dns.com`.
- For `vopple.uk`: Add A record pointing `@` to `76.76.21.21` and CNAME for `www` to `cname.vercel-dns.com`.

---

## ⚡ Verification & 1-Command Installer

Once deployed:
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
