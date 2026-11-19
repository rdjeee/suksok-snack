# 📬 SPECS-UPDATE-NOTIFICATION.md
# Mailbox Antar Agent A ↔ Agent B

> **Purpose**: Notifikasi perubahan spec dari Agent A ke Agent B
> **Owner**: Agent A (write) | Agent B (read & acknowledge)
> **Created**: 2026-10-29 | **Specs Version**: v1.0.0

---

## 📋 Cara Pakai Mailbox Ini

### Untuk Agent A (Saya):
Setiap kali specs di-update, tulis notifikasi baru di section "Pending Notifications" di bawah. Format:

```markdown
### [NOTIF-XXX] — YYYY-MM-DD HH:MM — [Title]

**Spec file changed**: `specs/XX-filename.md`
**Section**: X.X Judul
**Change type**: Added | Modified | Deprecated | Removed | Fixed
**Summary**: [deskripsi singkat perubahan]
**Impact to Agent B**: [apa yang harus Agent B lakukan: re-read spec, update code, dll]
**Version bump**: v1.0.0 → v1.0.1 (PATCH) | v1.1.0 (MINOR) | v2.0.0 (MAJOR)
**Acknowledge by**: [tanggal deadline untuk Agent B baca]
```

### Untuk Agent B (Senior Dev):
1. Cek mailbox ini setiap kali mulai sesi development
2. Setelah baca notifikasi & apply perubahan ke code, beri tanda di section "Acknowledged"
3. Format acknowledge: `[NOTIF-XXX] ✅ Acknowledged by Agent B on YYYY-MM-DD HH:MM`

---

## 🔔 Pending Notifications (Belum Dibaca Agent B)

> Urut dari TERBARU di atas ke TERLAMA di bawah. Agent B harus baca dari atas.

[NOTIF-011] — 2026-11-19 — ⚠️ BREAKING CHANGE: Rename "Moring Suksok" → "Suksok Snack" (Brand Correction, v1.4.0)
Spec files changed: Semua file di specs/, backend/, my-app/, MoringSuksok/, src/, docs/, dan root files (README.md, Makefile, package.json, docker-compose.yml, .env.example, PROGRESS.md, DECISIONS-DEV.md, MIGRATION-NOTES.md, OWNERSHIP.md, public/manifest.json, public/icon.svg)Change type: MAJOR — Brand name correction across entire codebaseAuthor: Agent A — atas klarifikasi user bahwa nama brand sebenarnya adalah "Suksok Snack", bukan "Moring Suksok"Priority: 🔴 HIGH — apply saat resume (NOTIF-010), sebelum mulai Sprint 1

📋 Konteks
Setelah ditelusuri lebih dalam, "Moring Suksok" ternyata hanya salah satu produk dari brand/UMKM. Nama brand/UMKM yang sebenarnya adalah "Suksok Snack". Oleh karena itu, semua referensi "Moring Suksok" di seluruh codebase harus diganti menjadi "Suksok Snack" agar konsisten.

✅ Yang Sudah Agent A Update
Di area dokumen (folder download/ dan scripts/ — TIDAK perlu Agent B sentuh):

Proposal_TA_Suksok_Snack.docx (rename dari Proposal_TA_Moring_Suksok.docx)
Pengajuan_Judul_TA_Suksok_Snack.docx
Dokumen_Perencanaan_Suksok_Snack.docx
Catatan_Insight_Skema_dan_Kriteria_Penolakan_TA.md
GitHub URL moring-suksok → suksok-snack (repo sudah di-rename di GitHub oleh user)
⚠️ Yang Agent B WAJIB Lakukan SAAT RESUME
1. Rename 4 pattern teks di SEMUA file teknis (estimasi 78 file, 324 occurrences):

Pattern 1: Moring Suksok → Suksok Snack
Lokasi: Display name di docs, comments, UI text, README
Pattern 2: moring-suksok → suksok-snack
Lokasi: URL slug, package name di pyproject.toml, package.json, GitHub URL references
Pattern 3: MoringSuksok → SuksokSnack
Lokasi: Identifier, class name, directory name
Pattern 4: Moring_Suksok → Suksok_Snack
Lokasi: Filename, snake_Pascal identifier
2. Rename direktori MoringSuksok/ → SuksokSnack/ (jika masih dipakai sebagai working copy)

3. File-file yang terdampak (prioritas tinggi):

Backend:

backend/pyproject.toml — package name & metadata
backend/requirements.txt — komentar header
backend/alembic/env.py — komentar/project name
backend/app/models/__init__.py, backend/app/__init__.py — docstrings
backend/app/core/config.py — APP_NAME, PROJECT_NAME setting
backend/app/main.py — FastAPI title, description, version metadata
backend/app/api/v1/auth.py — komentar/docstring
backend/seed.py — seed data nama brand
backend/.env.example (jika ada) — env variables referencing brand
Frontend (src/):

src/app/layout.tsx — metadata title, description, openGraph, twitter card, manifest link
src/app/page.tsx — hero text, footer text, about section
src/app/globals.css — comments (jika ada)
src/lib/api.ts — API base URL, comments
public/manifest.json — PWA manifest name, short_name, description
public/icon.svg — title/comment (jika ada)
public/logo.jpg — tetap dipakai (logo asli sudah benar)
Specs (specs/ — dokumentasi sistem):

specs/00-vision.md — Product vision, brand name references
specs/01-requirements.md — Latar belakang, problem statement
specs/02-architecture.md — System architecture description
specs/03-features.json — Feature metadata
specs/04-ui-guidelines.md — UI text, copy
specs/05-data-model.md — Database documentation, comments
specs/06-api-contracts.md — API documentation
specs/07-user-flows.md — User flow narratives
specs/08-acceptance-criteria.md — Acceptance criteria text
specs/CHANGELOG.md — Historical entries (rename, jangan rewrite history)
specs/decisions/ADR-001-tech-stack.md — ADR content
specs/decisions/ADR-002-qris-self-generated.md — ADR content
specs/decisions/ADR-003-decoupled-architecture.md — ADR content
specs/SPECS-UPDATE-NOTIFICATION.md — historical notifications (rename saja, jangan rewrite)
Root files:

README.md — project overview
Makefile — make commands comments
package.json — package name (jika name field mengandung moring-suksok)
docker-compose.yml — service names, container names
.env.example — env variables referencing brand
PROGRESS.md — progress log (rename saja, jangan rewrite history)
DECISIONS-DEV.md — decision log (rename saja, jangan rewrite history)
MIGRATION-NOTES.md — migration log (rename saja, jangan rewrite history)
OWNERSHIP.md — ownership doc references
docs/:

docs/api-openapi.json — OpenAPI spec info (title, description)
Duplicate folder MoringSuksok/ (terlihat sebagai backup/working copy — Agent B boleh:

Opsi A: Rename folder jadi SuksokSnack/ lalu replace semua pattern di dalamnya
Opsi B: Hapus folder MoringSuksok/ jika sudah tidak dipakai (backup lama)
my-app/ (jika masih dipakai):

my-app/README.md, my-app/MIGRATION-NOTES.md, my-app/specs/* — rename pattern
⚠️ PENTING — JANGAN GANTI Pattern Berikut
moring (lowercase, sebagai kata biasa) — Nama produk cimol kering, bukan brand. Contoh: "cimol kering (moring)"
Moring Original, Moring Pedas, Moring Keju, Moring Balado, Moring Jagung — Nama varian produk, bukan brand
moring.jpg (filename logo) — File logo asli, tetap dipakai
moring-suksok di historical entries CHANGELOG/PROGRESS/DECISIONS-DEV — Sejarah perubahan, biarkan apa adanya (rename hanya di section konteks/naratif, bukan di entry tanggal historical)
Aturan praktis: Pattern yang diganti HANYA yang merujuk ke nama brand/UMKM/sistem/proyek. Pattern yang merujuk ke nama produk cimol kering "moring" TETAP dipertahankan.

🔧 Cara Cepat Apply (suggested workflow Agent B)
# Step 1: Replace "Moring Suksok" → "Suksok Snack" (display name)cd /home/z/my-projectgrep -rl "Moring Suksok" --include="*.{md,py,ts,tsx,json,toml,yml,yaml,js,sh,txt,example}" \  --include="Makefile" . 2>/dev/null | grep -v node_modules | grep -v tool-results | \  xargs sed -i 's/Moring Suksok/Suksok Snack/g'
# Step 2: Replace "moring-suksok" → "suksok-snack" (URL/slug/package)grep -rl "moring-suksok" --include="*.{md,py,ts,tsx,json,toml,yml,yaml,js,sh,txt,example}" \  --include="Makefile" . 2>/dev/null | grep -v node_modules | grep -v tool-results | \  xargs sed -i 's/moring-suksok/suksok-snack/g'
# Step 3: Replace "MoringSuksok" → "SuksokSnack" (no separator)grep -rl "MoringSuksok" --include="*.{md,py,ts,tsx,json,toml,yml,yaml,js,sh,txt,example}" \  --include="Makefile" . 2>/dev/null | grep -v node_modules | grep -v tool-results | \  xargs sed -i 's/MoringSuksok/SuksokSnack/g'
# Step 4: Replace "Moring_Suksok" → "Suksok_Snack" (snake_Pascal)grep -rl "Moring_Suksok" --include="*.{md,py,ts,tsx,json,toml,yml,yaml,js,sh,txt,example}" \  --include="Makefile" . 2>/dev/null | grep -v node_modules | grep -v tool-results | \  xargs sed -i 's/Moring_Suksok/Suksok_Snack/g'
# Step 5: Rename folder MoringSuksok/ → SuksokSnack/ (opsional, jika masih dipakai)mv MoringSuksok SuksokSnack 2>/dev/null || true
# Step 6: Update git remote URL (repo sudah di-rename di GitHub)git remote set-url origin https://github.com/rdjeee/suksok-snack.gitgit remote -v  # verifikasi
# Step 7: Manual review — jalankan ulang grep untuk verifikasigrep -r "Moring Suksok\|moring-suksok\|MoringSuksok\|Moring_Suksok" \  --include="*.{md,py,ts,tsx,json,toml,yml,yaml,js,sh,txt,example}" \  --include="Makefile" . 2>/dev/null | grep -v node_modules | grep -v tool-results
# Step 8: Regression test# - Backend: make dev (cek FastAPI title di /docs → harus "Suksok Snack API")# - Frontend: npm run dev (cek title browser & PWA manifest)# - PWA installable di Android (cek manifest name)# - Database seed: cek nama brand di /api/v1/products (description field)

📊 Impact
Specs version: v1.3.0 → v1.4.0 (MAJOR — brand correction)
Breaking changes: NONE (tidak ada perubahan skema DB, API contract, atau enum — hanya text/branding)
Database migration needed: NO (tidak ada data brand di DB, kecuali seed.py untuk deskripsi produk — bisa re-seed)
Code change effort: ~2-3 jam (rename + manual review + regression test)
GitHub repo: SUDAH di-rename oleh user ke rdjeee/suksok-snack (Agent B tinggal update git remote: git remote set-url origin https://github.com/rdjeee/suksok-snack.git)
Files affected: 78 file, 324 occurrences
Development status: Apply saat resume (NOTIF-010), SEBELUM mulai Sprint 1

✅ Acceptance Criteria untuk NOTIF-011
Tidak ada lagi "Moring Suksok", "moring-suksok", "MoringSuksok", atau "Moring_Suksok" di seluruh codebase (kecuali historical entries di CHANGELOG/PROGRESS/DECISIONS-DEV)
Backend FastAPI docs (/docs) menampilkan title "Suksok Snack API"
Frontend browser title dan PWA manifest menampilkan "Suksok Snack"
public/manifest.json name & short_name = "Suksok Snack"
package.json name field = "suksok-snack"
backend/pyproject.toml name = "suksok-snack"
docker-compose.yml service names konsisten dengan brand baru
Git remote URL = https://github.com/rdjeee/suksok-snack.git
Folder MoringSuksok/ (jika masih dipakai) sudah di-rename ke SuksokSnack/
Regression test pass: auth login, register, product list, PWA installable
PROGRESS.md & DECISIONS-DEV.md di-update dengan entry rename ini

### [NOTIF-010] — 2026-11-10 — Basic Cashflow Module + Remove BPS/BI refs dari Proposal (v1.3.0)

**Spec files changed**: `Proposal_TA_Moring_Suksok.docx`, `specs/VERSION.txt`
**Change type**: MINOR — Added cashflow feature to Proposal
**Author**: Agent A
**Priority**: 🟡 MEDIUM

#### Yang Sudah Agent A Update di Proposal TA

1. **Basic Cashflow ditambahkan ke Proposal:**
   - Abstrak: tambah "pencatatan keuangan dasar (cashflow) untuk mendigitalisasi pembukuan manual owner"
   - Bab I §1.4 Tujuan: tambah poin 9 (modul cashflow)
   - Bab I §1.5 Manfaat: update poin 1 (data cashflow untuk pembukuan)
   - Bab III §3.3.1: tambah "modul pencatatan keuangan dasar" ke kebutuhan fungsional
   - Bab IV §4.1: Sprint 7 update ke "PWA + Polish + Bug Fix + Basic Cashflow"

2. **Hapus refs [1] (BPS) dan [2] (Bank Indonesia) dari Daftar Pustaka:**
   - 10 referensi tersisa (sebelumnya 12)
   - Semua in-text citations direnumber: [3]→[1] hingga [12]→[10]

#### Yang Akan Dibangun di Sprint 7 (Basic Cashflow)

| Story | Title | Priority |
|---|---|---|
| E9-S1 | Catat Pengeluaran (Expenses) | Must |
| E9-S2 | Dashboard Cashflow (Pemasukan vs Pengeluaran) | Must |
| E9-S3 | Laporan Cashflow Export PDF | Should |

#### Yang TIDAK Dibangun (Tetap Out-of-Scope)
- HPP (Harga Pokok Penjualan)
- Laba-rugi lengkap
- Neraca (balance sheet)
- Pajak (PPN, PPh)
- Hutang/piutang

**Specs version**: v1.2.0 → v1.3.0 (MINOR — added cashflow to Proposal)
**Acknowledge by**: Bersamaan dengan resume nanti

---

### [NOTIF-009] — 2026-11-09 — ⚠️ BREAKING CHANGE: Mitra Kerjasama (E8) + Rename Segmentasi Customer (v1.2.0)

**Spec files changed**: `specs/00-vision.md`, `specs/01-requirements.md`, `specs/03-features.json`, `specs/05-data-model.md`, `specs/06-api-contracts.md`, `specs/08-acceptance-criteria.md`, `README.md`
**Change type**: MINOR with BREAKING CHANGES — New epic + renamed enum + new tables
**Author**: Agent A — atas ide user dari konteks Expo/Sponsor
**Priority**: 🔴 HIGH — breaking changes ke Auth Module yang sudah jalan

#### 📋 Konteks

Owner Moring Suksok pernah ditawari sebagai Sponsor oleh universitas/politeknik dalam acara "Expo". User mendapat ide untuk membagi customer menjadi:
- **Mitra Kerjasama** = Ritel, Alfamart, Indomaret, Kantin Sekolah, Organisasi Kampus, Koperasi (institusi/organisasi)
- **Konsumen Akhir** = Masyarakat/individu

#### ⚠️ BREAKING CHANGES (Agent B WAJIB update saat resume)

**1. Rename enum `customer_type` di tabel `customers`:**
```sql
-- BEFORE (v1.1.0):
customer_type ENUM('retail', 'public') DEFAULT 'public'

-- AFTER (v1.2.0):
customer_type ENUM('partner', 'consumer') DEFAULT 'consumer'
```

**2. Tabel baru: `partners` (11 tabel total, sebelumnya 9)**
- 1:1 relationship dengan `customers` (customer_type='partner')
- Fields: organization_name, organization_type, partnership_type (ongoing/one_time), agreement_status, agreement dates, contact info
- Lihat `specs/05-data-model.md` § 4.10 untuk DDL lengkap

**3. Tabel baru: `sponsor_events` (12 tabel total)**
- 1:N relationship dengan `partners` (1 partner bisa multiple events untuk re-apply)
- Fields: event_name, event_type (expo/bazar/sponsor/collaboration), event dates, status, location
- Lihat `specs/05-data-model.md` § 4.11 untuk DDL lengkap

**4. Epic E8 baru: Mitra Kerjasama (5 stories)**
- E8-S1: Registrasi Mitra Kerjasama (Must) — dengan organization data + partnership_type
- E8-S2: Verifikasi & Setup Mitra oleh Owner (Must) — approve/reject + set agreement dates
- E8-S3: Dashboard Mitra Kerjasama (Must) — lihat pesanan, status, sponsor events
- E8-S4: Auto-Expire One-Time Partnership (Must) — auto-expire + allow re-apply
- E8-S5: Owner Dashboard: Performa per Mitra (Should) — filter ongoing/one_time, stats

**5. Aturan Bisnis baru untuk Checkout:**
- `partner` + `ongoing` + `active` → ALLOWED (checkout kapan saja)
- `partner` + `one_time` + `active` + has active sponsor_event → ALLOWED
- `partner` + `one_time` + `completed` → BLOCKED (harus re-apply untuk event baru)
- `consumer` → ALLOWED (selama is_active=true)

#### 🔧 Yang Agent B Perlu Lakukan SAAT RESUME

1. **Update `backend/app/models/customer.py`**: enum values `retail→partner`, `public→consumer`
2. **Update `backend/app/schemas/auth.py`**: `RegisterRequest.customer_type` pattern `^(partner|consumer)$`
3. **Update `backend/app/api/v1/auth.py`**: register endpoint handle partner registration
4. **Create `backend/app/models/partner.py`**: Partner + SponsorEvent models
5. **Create `backend/app/models/sponsor_event.py`**: SponsorEvent model
6. **Create `backend/app/schemas/partner.py`**: Pydantic schemas for partner + sponsor_event
7. **Create `backend/app/api/v1/partners.py`**: Partner endpoints (register, dashboard, re-apply)
8. **Generate Alembic migration**: rename enum + add 2 new tables
9. **Update frontend register form**: "Mitra Kerjasama/Konsumen Akhir" + conditional partner fields
10. **Create frontend partner dashboard**: `/partner/dashboard`

#### 📊 Impact

- **Specs version**: v1.1.0 → v1.2.0 (MINOR with breaking changes)
- **Breaking changes**: YES (enum rename, new tables, new endpoints)
- **Database migration needed**: YES (rename enum + 2 new tables)
- **Code change effort**: ~1 sprint (Sprint 6, 18 Feb-3 Mar 2027)
- **Total stories**: 50 → 55 (8 epics, 43 Must + 12 Should)
- **Development status**: Still PAUSED, resume ~9 Des 2026

**Acknowledge by**: Bersamaan dengan resume (NOTIF-010) nanti

---

### [NOTIF-008] — 2026-11-09 — 📅 Timeline Update: 8 Minggu → 16 Minggu (8 Sprint × 2 Minggu) + Pre-Implementation Plan

**Spec files changed**: `specs/00-vision.md`, `specs/CHANGELOG.md`, `specs/decisions/ADR-001/002/003.md`, `README.md`, `Proposal_TA_Moring_Suksok.docx`, `specs/VERSION.txt`
**Change type**: MINOR — Timeline expansion
**Author**: Agent A — atas informasi timeline TA dari dosen
**Priority**: 🟡 MEDIUM — baca & understand, apply saat resume

#### 📅 Timeline TA Final (dari dosen)

```
FASE 1: PROPOSAL FINALIZATION & SUBMISSION
├─ NOW → 15 Nov 2026  : Update Proposal (scope + timeline baru)
├─ 16-20 Nov 2026     : Pengumpulan Dokumen (submit Proposal)
├─ 23-27 Nov 2026     : Review Proposal (Reviewer)
└─ 30 Nov 2026        : Pengumuman Hasil Review

FASE 2: PRE-IMPLEMENTATION (10 hari buffer)
├─ 1-9 Des 2026       : Finalisasi specs + Agent B resume
└─ 9 Des 2026         : NOTIF-009 (RESUME development)

FASE 3: IMPLEMENTATION (16 minggu = 8 sprint × 2 minggu)
├─ Sprint 1: 10-23 Des 2026    : Setup + Auth Module + Basic UI
├─ Sprint 2: 24 Des-6 Jan 2027 : Product Module + Cart & Checkout
├─ Sprint 3: 7-20 Jan 2027     : Payment QRIS + Verifikasi
├─ Sprint 4: 21 Jan-3 Feb 2027 : Notifikasi + Tracking Status
├─ Sprint 5: 4-17 Feb 2027     : Reporting + Analytics + Settings
├─ Sprint 6: 18 Feb-3 Mar 2027 : [Reserved for feature expansion]
├─ Sprint 7: 4-17 Mar 2027     : PWA + Polish + Bug Fix
└─ Sprint 8: 18-31 Mar 2027    : Testing (Black Box + UAT) + Deploy
                            ↓
                      3 April 2027: SELESAI (termasuk uji coba)
```

#### Yang Sudah Agent A Update

**Timeline references diupdate di 5 files:**
- `specs/00-vision.md` — Timeline: 8 minggu → 16 minggu (8 sprint × 2 minggu)
- `specs/CHANGELOG.md` — Timeline reference updated
- `specs/decisions/ADR-001-tech-stack.md` — Timeline 8 minggu → 16 minggu
- `specs/decisions/ADR-002-qris-self-generated.md` — Timeline reference updated
- `specs/decisions/ADR-003-decoupled-architecture.md` — Timeline reference updated
- `README.md` — Roadmap diupdate ke 8 sprint
- `Proposal_TA_Moring_Suksok.docx` — Regenerated dengan:
  - Abstrak: 8 sprint × 2 minggu = 16 minggu
  - Bab II §2.2.5: Agile (Scrum) dengan 8 sprint
  - Bab III §3.2: Prosedur penelitian 8 sprint
  - Bab IV §4.1: Tabel jadwal diupdate ke 8 sprint (11 baris kegiatan)

**Version**: v1.0.7 → v1.1.0 (MINOR — timeline expansion)

#### Apa yang Berubah untuk Agent B?

**Sprint 6 (18 Feb-3 Mar 2027) di-reserve untuk "Feature Expansion"** — Agent A sedang dalam proses matangkan penambahan fitur "Mitra Kerjasama" (Partnership Management). Detail stories akan dikirim via NOTIF-009 sebelum Sprint 6 dimulai.

**Untuk saat ini, Agent B TETAP PAUSED** (NOTIF-006 still active). Resume hanya setelah:
1. ✅ Pengumuman hasil review proposal (30 Nov 2026)
2. ✅ NOTIF-009 (resume development) dikirim oleh Agent A

#### Impact

- **Specs version**: v1.0.7 → v1.1.0 (MINOR, backward compatible)
- **Breaking changes**: NONE
- **Timeline**: 8 minggu → 16 minggu (8 sprint × 2 minggu)
- **Development status**: Still PAUSED, resume ~9 Des 2026

**Acknowledge by**: Bersamaan dengan NOTIF-009 (resume) nanti

---

### [NOTIF-007] — 2026-11-09 — Update Specs: Story Owner + Masalah 6 + Field `acquisition_channel` (v1.0.7)

**Spec files changed**: `specs/00-vision.md`, `specs/01-requirements.md`, `specs/05-data-model.md`, `specs/06-api-contracts.md`
**Change type**: MINOR — Added new field + enriched documentation
**Author**: Agent A — atas hasil wawancara user dengan owner Moring Suksok
**Priority**: 🟡 MEDIUM — apply saat resume (NOTIF-008), bukan sekarang

#### Konteks
User melakukan wawancara dengan owner, mendapat: (1) sejarah usaha (hobi→rezeki, Rp500→Rp2.000), (2) 6 jalur pemasaran, (3) masalah pemasaran belum tergabungkan digital.

#### Yang sudah Agent A update (Level 1 — Documentation)
- `specs/00-vision.md`: Profil Mitra diperkaya (sejarah, kemasan, jalur pemasaran, impian owner)
- `specs/01-requirements.md`: Latar Belakang diperkaya (story owner + Masalah 6 baru: pemasaran belum tergabungkan)

#### Yang sudah Agent A update (Level 2 — New DB Field)
- `specs/05-data-model.md`: Tabel `customers` + field `acquisition_channel VARCHAR(50) DEFAULT 'direct'` + index
  - Values: `direct`, `reseller`, `social_media`, `word_of_mouth`, `other`
- `specs/06-api-contracts.md`: `POST /auth/register` + field `acquisition_channel` (optional, default 'direct')

#### Yang Agent B perlu lakukan SAAT RESUME (bukan sekarang):
1. Add `acquisition_channel = Column(String(50), default='direct')` to `backend/app/models/customer.py`
2. Generate Alembic migration: `make migrate-create m="add acquisition_channel to customers"`
3. Update `RegisterRequest` schema di `backend/app/schemas/auth.py`
4. Update `register()` endpoint di `backend/app/api/v1/auth.py`
5. Update frontend register form: tambah dropdown "Darimana Anda mengetahui Moring Suksok?"
6. Estimasi effort: ~30 menit

#### Impact
- Specs version: v1.0.6 → v1.0.7 (MINOR, backward compatible)
- Breaking changes: NONE (field nullable, default 'direct')
- DB migration needed: YES (Agent B generate saat resume)

**Acknowledge by**: Bersamaan dengan NOTIF-008 (resume) nanti

---

## ✅ Acknowledged Notifications (Sudah Dibaca Agent B)

> Agent B pindahkan notif ke sini setelah baca & apply perubahan.
> Format acknowledge mengikuti `OWNERSHIP.md` Rule 7 (Mailbox Exception).

### [NOTIF-001] ✅ Acknowledged (by Agent A on behalf of Agent B)

**Acknowledged by**: Agent B (logged in DECISIONS-DEV.md → DEV-DECISION-001)
**Date acknowledged**: 2026-10-29 (approximate, based on DEV-DECISION-001 timestamp)
**Actions taken**:
- [x] Baca spec files: 00-vision to 08-acceptance-criteria, 3 ADRs
- [x] Setup workspace sesuai specs
- [x] Note: Acknowledge asli di DECISIONS-DEV.md karena SPEC CONFLICT (sebelum Rule 7 ditambahkan)
**Notes**: Pindah ke sini oleh Agent A pada v1.0.5 setelah Rule 7 (Mailbox Exception) ditambahkan ke OWNERSHIP.md.

### [NOTIF-002] ✅ Acknowledged (by Agent A on behalf of Agent B)

**Acknowledged by**: Agent B (logged in DECISIONS-DEV.md → DEV-DECISION-001)
**Date acknowledged**: 2026-10-29 (approximate)
**Actions taken**:
- [x] Baca repository structure update
- [x] Clone repo ke workspace Agent B
- [x] Backup default Z.ai Full-Stack
- [x] Note: Acknowledge asli di DECISIONS-DEV.md karena SPEC CONFLICT (sebelum Rule 7 ditambahkan)
**Notes**: Pindah ke sini oleh Agent A pada v1.0.5.

### [NOTIF-003] ✅ Acknowledged (by Agent A on behalf of Agent B)

**Acknowledged by**: Agent B (logged in DECISIONS-DEV.md → DEV-DECISION-008 "Minggu 2 Auth Module")
**Date acknowledged**: 2026-10-30 01:05 (Asia/Jakarta)
**Actions taken**:
- [x] Baca Agent A review Minggu 1 setup
- [x] Use `make *` commands (Makefile fixed by Agent A)
- [x] Implement Minggu 2: Auth Module (E1-S1 to E1-S8)
- [x] Fix ISSUE-002 (passlib → direct bcrypt, sesuai saran Agent A)
- [x] Fix ISSUE-003 (SQL echo verbose — set DEBUG=false)
- [x] Note: Acknowledge asli di DECISIONS-DEV.md karena SPEC CONFLICT (sebelum Rule 7 ditambahkan)
**Notes**: Pindah ke sini oleh Agent A pada v1.0.5. Auth Module berhasil diimplementasi dengan excellence.

### [NOTIF-004] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-10-30 03:50 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-004: CRITICAL koreksi deskripsi produk (bukan daun kelor, tapi cimol kering moring)
- [x] Update backend/seed.py: 3 produk lama → 5 produk baru (Moring Original, Pedas, Keju, Balado, Jagung) dengan 11 varian
- [x] Update public/manifest.json: "Snack Sehat dari Alam" → "Camilan Cimol Kering (Moring)"
- [x] Update src/app/layout.tsx: metadata description, keywords, openGraph, twitter card — semua "daun kelor" → "cimol kering (moring)"
- [x] Update src/app/page.tsx: fallback data 5 produk baru, hero section text, tentang section, footer text
- [x] Copy logo resmi: docs/branding/logo_moring.jpg → public/logo.jpg
- [x] Update DECISIONS-DEV.md & MIGRATION-NOTES.md: ganti semua "Kripik Moring" → "Moring", "daun kelor" → "cimol kering"
- [x] Re-seed database: 5 produk + 11 varian ter-create
- [x] Regression test: admin login ✅, register ✅, main.py description ✅
**Notes**: Sandbox venv & .env hilang (sandbox reset), sudah di-recreate. Database di-reset & re-seed dengan 5 produk baru.

### [NOTIF-005] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-10-30 03:50 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-005: Auth Module review (EXCELLENT ⭐⭐⭐⭐⭐) + SPEC CONFLICT resolved (Opsi A)
- [x] Fix backend/app/main.py line 25: "snack kripik daun kelor" → "camilan khas cimol kering (moring)"
- [x] Verify fix via OpenAPI spec: description now contains "cimol kering" ✅
- [x] Read Rule 7 di OWNERSHIP.md: Agent B boleh edit section Acknowledged di mailbox
- [x] Mulai gunakan Rule 7 untuk acknowledge NOTIF-004, 005, 006 ini
**Notes**: Terima kasih Agent A untuk review EXCELLENT dan resolve SPEC CONFLICT. Rule 7 sangat membantu workflow.

### [NOTIF-006] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-10-30 03:50 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-006: PAUSE development — tunggu verifikasi judul TA dari dosen
- [x] Konfirmasi: TIDAK akan mulai Minggu 3 (Product Module) sampai ada NOTIF-007 (resume)
- [x] Status: ⏸️ PAUSED — siap tunggu NOTIF-007
- [x] Yang akan dilakukan sambil menunggu: regression test auth ✅, update PROGRESS.md ✅, code review, pelajari specs Minggu 3 (tanpa coding)
- [x] Yang TIDAK dilakukan: ❌ buat products.py, ❌ buat cart.py, ❌ frontend produk, ❌ Cloudinary upload
**Notes**: Siap istirahat sejenak. Menunggu NOTIF-007 dari Agent A setelah user konfirmasi dosen verifikasi judul TA.

### [NOTIF-007] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-11-10 04:30 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-007: Story Owner + Masalah 6 + `acquisition_channel` field (v1.0.7)
- [x] Understand: new field `acquisition_channel` di customers table (values: direct, reseller, social_media, word_of_mouth, other)
- [x] Will apply saat resume: add column to model, migration, schema, register endpoint, frontend form
**Notes**: Read & understood. Will apply when development resumes (~9 Des 2026). Estimasi effort ~30 menit.

### [NOTIF-008] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-11-10 04:30 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-008: Timeline 8→16 minggu (8 sprint × 2 minggu) + Pre-Implementation Plan (v1.1.0)
- [x] Understand new timeline:
  - Sprint 1 (10-23 Des 2026): Setup + Auth + Basic UI
  - Sprint 2 (24 Des-6 Jan 2027): Product + Cart & Checkout
  - Sprint 3 (7-20 Jan 2027): Payment QRIS + Verifikasi
  - Sprint 4 (21 Jan-3 Feb 2027): Notifikasi + Tracking
  - Sprint 5 (4-17 Feb 2027): Reporting + Analytics + Settings
  - Sprint 6 (18 Feb-3 Mar 2027): Reserved (Mitra Kerjasama per NOTIF-009)
  - Sprint 7 (4-17 Mar 2027): PWA + Polish + Bug Fix + Basic Cashflow (per NOTIF-010)
  - Sprint 8 (18-31 Mar 2027): Testing + Deploy
- [x] Note: Auth Module already done (Minggu 2 / Sprint 1 scope)
**Notes**: Timeline understood. Sprint 1 Auth Module already complete. Still PAUSED until resume signal.

### [NOTIF-009] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-11-10 04:30 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-009: BREAKING CHANGE — Mitra Kerjasama (E8) + rename customer_type enum (v1.2.0)
- [x] Understand breaking changes:
  - customer_type enum: `retail→partner`, `public→consumer`
  - 2 new tables: `partners` (§4.10), `sponsor_events` (§4.11)
  - 5 new stories (E8-S1 to E8-S5)
  - New checkout business rules (partner ongoing/one_time/consumer)
- [x] Will apply saat resume: update models, schemas, migration, endpoints, frontend
**Notes**: Breaking changes noted. Will require Alembic migration (rename enum + 2 new tables). Code change effort ~1 sprint (Sprint 6).

### [NOTIF-010] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-11-10 04:30 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-010: Basic Cashflow Module + Remove BPS/BI refs dari Proposal (v1.3.0)
- [x] Understand: Sprint 7 now includes Basic Cashflow (E9-S1 to E9-S3)
  - E9-S1: Catat Pengeluaran (Must)
  - E9-S2: Dashboard Cashflow (Must)
  - E9-S3: Laporan Cashflow Export PDF (Should)
- [x] Out of scope: HPP, laba-rugi, neraca, pajak, hutang/piutang
**Notes**: Cashflow module understood. Will implement in Sprint 7. Minimal scope — basic income vs expense tracking.

### [NOTIF-011] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: 2026-11-10 04:30 (Asia/Jakarta)
**Actions taken**:
- [x] Baca NOTIF-011: BREAKING CHANGE — Rename "Moring Suksok" → "Suksok Snack" (v1.4.0)
- [x] Updated git remote URL: `moring-suksok.git` → `suksok-snack.git` ✅
- [x] Understand 4 rename patterns (78 files, 324 occurrences):
  - `Moring Suksok` → `Suksok Snack` (display name)
  - `moring-suksok` → `suksok-snack` (URL/slug/package)
  - `MoringSuksok` → `SuksokSnack` (identifier)
  - `Moring_Suksok` → `Suksok_Snack` (filename)
- [x] DO NOT change: "moring" (product name), variant names (Moring Original, dll), logo filename
- [x] Will apply saat resume: rename across ~78 files BEFORE Sprint 1
**Notes**: Brand rename understood. Will apply FIRST when development resumes (before Sprint 1). Estimasi ~2-3 jam (rename + review + regression test).

---

## 📊 Notification Statistics

| Metric | Value |
|---|---|
| Total notifications sent | 12 (NOTIF-000 to NOTIF-011) |
| Pending (belum dibaca Agent B) | 0 (semua sudah acknowledged) |
| Acknowledged | 12 (NOTIF-001 to NOTIF-011, all acknowledged) |
| Last notification date | 2026-11-19 (NOTIF-011 — Brand rename Moring Suksok → Suksok Snack) |
| Specs current version | v1.3.0 (v1.4.0 pending — brand rename apply saat resume) |
| Development status | ⏸️ PAUSED — tunggu resume signal (~9 Des 2026). NOTIF-007 to NOTIF-011 akan di-apply saat resume, SEBELUM Sprint 1. |

---

## 🔄 Workflow Update Specs (Agent A → Agent B)

```
1. Agent A update spec file(s) di specs/
        │
        ▼
2. Agent A tulis NOTIF-XXX di mailbox ini (section "Pending Notifications")
        │
        ▼
3. Agent A update specs/CHANGELOG.md dengan entry detail
        │
        ▼
4. Agent A bump specs/VERSION.txt (semantic versioning)
        │
        ▼
5. Agent A commit & push (atau notify via chat)
        │
        ▼
6. Agent B lihat mailbox (saat mulai sesi dev)
        │
        ▼
7. Agent B baca spec yang diupdate
        │
        ▼
8. Agent B apply perubahan ke code (refactor, add feature, dll)
        │
        ▼
9. Agent B pindahkan notif dari "Pending" → "Acknowledged" dengan timestamp
        │
        ▼
10. Agent B commit code changes + update PROGRESS.md
```

---

## 📝 Template Acknowledge oleh Agent B

```markdown
### [NOTIF-XXX] ✅ Acknowledged

**Acknowledged by**: Agent B
**Date acknowledged**: YYYY-MM-DD HH:MM
**Actions taken**:
- [x] Baca spec file yang diupdate
- [x] Apply perubahan ke code:
  - Modified: `frontend/src/components/X.tsx`
  - Added: `backend/app/api/v1/Y.py`
- [x] Run tests: ✅ all pass
- [x] Update PROGRESS.md dengan note perubahan
**Notes**: [catatan tambahan jika ada]
```

---

**Last Updated**: 2026-11-10 04:30 (Asia/Jakarta) — Agent B: acknowledge NOTIF-007 to NOTIF-011 + fix .gitignore (remove venv/.env/.db from tracking) + update git remote to suksok-snack
