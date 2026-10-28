# Vercel Deployment & IONOS DNS Guide for vopple.uk

Deploying **`VDE-SITE`** to **Vercel** with your custom domain **`vopple.uk`** on **IONOS**.

---

## 🚀 1. Deploy Repository to Vercel

1. Log into your [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **Add New...** > **Project**.
3. Import **`i2qq/VDE-SITE`**.
4. Framework Preset: **Other** (Static HTML/CSS/JS).
5. Root Directory: `./` (default).
6. Click **Deploy**.

---

## 🌐 2. Add Custom Domain `vopple.uk` in Vercel

1. In your Vercel project, go to **Settings** > **Domains**.
2. Enter **`vopple.uk`** and click **Add**.
3. Vercel will ask you to also add `www.vopple.uk` (recommended).
4. Vercel will show the required DNS records:
   - **Type A**: `@` -> `76.76.21.21`
   - **Type CNAME**: `www` -> `cname.vercel-dns.com`

---

## 🛠️ 3. Configure DNS in IONOS

From your IONOS screenshot (**Domains & SSL** > **vopple.uk**):

1. Click on the **DNS** tab at the top.
2. Click **Add record**:
   - **Record Type**: `A`
   - **Host Name**: `@` (leave empty or enter `@` depending on IONOS prompt)
   - **Points to**: `76.76.21.21`
   - **TTL**: `1 hour` (or default)
   - Click **Save**.
3. *(Optional for `www`)*:
   - If an existing `A` record for `www` exists, change it, or click **Add record**:
   - **Record Type**: `CNAME`
   - **Host Name**: `www`
   - **Points to**: `cname.vercel-dns.com`
   - Click **Save**.

---

## ⚡ 4. Verification

Once IONOS DNS propagates (usually 1–2 minutes):
- Website will be live at: `https://vopple.uk`
- Direct bash installer:
  ```bash
  wget -qO- https://vopple.uk/install.sh | sudo bash
  ```
  *or:*
  ```bash
  curl -sSL https://vopple.uk/install.sh | sudo bash
  ```
- Short alias:
  ```bash
  curl -sSL https://vopple.uk/install | sudo bash
  ```
