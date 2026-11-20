# KNOWN-ISSUES.md
# Bug Tracker & Known Issues

> **Owner**: Agent B (Dev) | **Started**: 2026-10-29
> **Purpose**: Track bugs yang ditemukan, severity, dan status fix

---

## 🐛 Bug Priority Levels

| Level | Definition | SLA |
|---|---|---|
| 🔴 Critical | Sistem tidak jalan, blocking development | Fix within 24h |
| 🟠 High | Feature utama broken, ada workaround sulit | Fix within 3 days |
| 🟡 Medium | Feature broken, ada workaround mudah | Fix within 1 week |
| 🟢 Low | Cosmetic issue, minor inconvenience | Fix when possible |

---

## 📋 Open Issues

| ID | Priority | Title | Component | Date Found | Status | Assigned |
|---|---|---|---|---|---|---|
| ISSUE-001 | 🟡 Medium | Makefile recipe lines use spaces, not TABs | build/Makefile | 2026-10-29 | ✅ Resolved (2026-10-30 by Agent A) | Agent A (SHARED file) |
| ISSUE-002 | 🟢 Low | passlib + bcrypt 4.x version warning (cosmetic) | backend/auth | 2026-10-29 | ✅ Resolved (2026-10-30 — switched to direct bcrypt) | Agent B |
| ISSUE-003 | 🟢 Low | SQL echo very verbose (DEBUG=true) | backend/config | 2026-10-29 | ✅ Resolved (2026-10-30 — added SQL_ECHO env var) | Agent B |
| ISSUE-004 | 🟠 High | .gitignore recurring reset to minimal version | .gitignore | 2026-11-19 | Open (3rd occurrence) | Investigation needed |

---

## 📝 Issue Details

### [ISSUE-001] — Makefile recipe lines use spaces, not TABs

**Priority**: 🟡 Medium
**Component**: build/Makefile (SHARED — owned by Agent A)
**Date Found**: 2026-10-29
**Found By**: Agent B

**Description**: `make migrate` (and all other make commands) fail with `Makefile:35: *** missing separator (did you mean TAB instead of 8 spaces?)`. GNU Make requires TAB characters at the start of recipe lines, but the Makefile uses 8 spaces throughout.

**Steps to Reproduce**:
1. `cd /home/z/my-project`
2. `make migrate`
3. Error: `Makefile:35: *** missing separator`

**Expected Behavior**: `make migrate` runs `cd backend && venv/bin/python -m alembic upgrade head`

**Actual Behavior**: Make fails to parse the Makefile.

**Workaround**: Run alembic commands directly:
```bash
cd backend && source venv/bin/activate
alembic upgrade head      # instead of: make migrate
python seed.py            # instead of: make seed
```

**Fix**: Replace all 8-space recipe indents with TAB characters in Makefile. This is a SHARED file — needs [SHARED-EDIT-REQUEST] via DECISIONS-DEV.md (request submitted).

**Resolution**: ✅ **RESOLVED by Agent A on 2026-10-30** (commit TBD). All 8-space indents converted to TAB characters via Python script. `make help`, `make tree`, `make migrate` now parse correctly. Verified `make help` outputs full command list without "missing separator" error.

**Status**: ✅ Closed — fixed by Agent A (SHARED file owner)

---

### [ISSUE-002] — passlib + bcrypt 4.x version warning (cosmetic)

**Priority**: 🟢 Low
**Component**: backend/auth (passlib 1.7.4 + bcrypt 4.2.1)
**Date Found**: 2026-10-29
**Found By**: Agent B

**Description**: When `hash_password()` is called, passlib emits a trapped warning:
```
(trapped) error reading bcrypt version
AttributeError: module 'bcrypt' has no attribute '__about__'
```

This is a known compatibility issue: passlib 1.7.4 tries to read `bcrypt.__about__.__version__`, which was removed in bcrypt 4.x. The warning is **trapped** (caught internally by passlib) and password hashing works correctly — bcrypt hash is generated successfully (e.g., `$2b$12$...`).

**Steps to Reproduce**:
1. `cd backend && source venv/bin/activate`
2. `python -c "from app.core.security import hash_password; print(hash_password('test'))"`
3. Warning appears in stderr, but hash is generated correctly.

**Expected Behavior**: No warning.

**Actual Behavior**: Trapped warning printed, but functionality works.

**Fix options** (when time permits):
1. Upgrade passlib to a version that supports bcrypt 4.x (check if 1.7.5+ available)
2. Pin bcrypt to 3.2.2 in requirements.txt (downside: older, less secure)
3. Suppress the warning with `warnings.filterwarnings` in security.py
4. Switch from passlib to direct bcrypt usage (passlib is somewhat unmaintained)

**Status**: Open — cosmetic only, no functional impact. Will address in later cleanup phase.

---

### [ISSUE-003] — SQL echo very verbose (DEBUG=true)

**Priority**: 🟢 Low
**Component**: backend/app/core/database.py
**Date Found**: 2026-10-29
**Found By**: Agent B

**Description**: `engine = create_engine(..., echo=settings.DEBUG)` logs every SQL statement when `DEBUG=true` (which is the current sandbox .env value). This makes output very noisy during seed.py and API calls.

**Workaround**: Set `DEBUG=false` in backend/.env to silence SQL echo.

**Fix**: Consider using `echo=False` by default and enable via a separate `SQL_ECHO` env var, OR only echo when `LOG_LEVEL=DEBUG`. Minor improvement — not blocking.

**Status**: Open — cosmetic only

---

## ✅ Resolved Issues

| ID | Priority | Title | Component | Date Found | Date Resolved | Solution |
|---|---|---|---|---|---|---|
| ISSUE-001 | 🟡 Medium | Makefile recipe lines use spaces, not TABs | build/Makefile | 2026-10-29 | 2026-10-30 | Agent A converted all 8-space indents to TAB characters in Makefile. Verified `make help` works without "missing separator" error. |

**Open Issues** (after ISSUE-001 resolved):

| ID | Priority | Title | Component | Date Found | Status | Assigned |
|---|---|---|---|---|---|---|
| ISSUE-002 | 🟢 Low | passlib + bcrypt 4.x version warning (cosmetic) | backend/auth | 2026-10-29 | Open | Agent B |
| ISSUE-003 | 🟢 Low | SQL echo very verbose (DEBUG=true) | backend/config | 2026-10-29 | Open | Agent B |

---

## 📈 Bug Statistics

| Metric | Value |
|---|---|
| Total bugs found | 4 |
| Open bugs | 1 (ISSUE-004 High priority)|
| Critical open | 0 |
| Resolved bugs | 1 (ISSUE-001 — Makefile spaces→TABs) |
| Average resolution time | 1 day (ISSUE-001: 2026-10-29 → 2026-10-30) |

---

**Last Updated**: 2026-11-19 (Asia/Jakarta) — Agent B: ISSUE-002 & 003 resolved; ISSUE-004 (.gitignore recurring reset) added — needs investigation

### [ISSUE-004] — .gitignore recurring reset to minimal version

**Priority**: 🟠 High
**Component**: .gitignore (SHARED)
**Date Found**: 2026-11-19
**Found By**: Agent B

**Description**: File `.gitignore` sudah **3 kali ter-reset** ke versi minimal (hanya `skills/` + `node_modules/`) tanpa sengaja. Comprehensive entries yang Agent B tulis (venv/, .env, .db, __pycache__/, .next/, dll) hilang berulang kali. Akibatnya, `backend/venv/` (10,000+ files), `backend/.env` (berisi JWT_SECRET!), dan `backend/*.db` ter-commit ke repo GitHub.

**Occurrences**:
1. **2026-10-30** — Pertama kali ditemukan saat pull Agent A's commit. .gitignore Agent B ditimpa versi minimal. Fixed: restore comprehensive + git rm --cached 10,526 files (commit ebc9b22)
2. **2026-11-19** — Terjadi lagi setelah brand rename sed operations. venv (10,604 files) + .env ter-commit lagi. Fixed: git rm --cached + restore .gitignore (commits 312af9b + 561e812)
3. **Risk of recurrence** — Penyebab belum dikonfirmasi. Kemungkinan: git operations (merge/reset) yang overwrite, atau Agent A's push yang tidak sengaja menimpa .gitignore

**Impact**:
- 🔴 Security: `backend/.env` (berisi JWT_SECRET) sempat ter-commit ke repo public
- 🟡 Repo bloat: 10,000+ venv files (~397MB) ter-commit, memperlambat clone/pull
- 🟡 Maintenance overhead: Agent B harus repeatedly fix .gitignore + git rm --cached

**Steps to Reproduce** (tidak sengaja):
1. Agent B menulis .gitignore comprehensive (107 lines)
2. Agent A push commit yang mengandung .gitignore versi minimal
3. Agent B pull → .gitignore tertimpa versi minimal
4. `git add -A` picks up venv/.env/.db karena tidak lagi di-ignore
5. Files ter-commit ke repo

**Workaround (current)**: Agent B monitors git status sebelum commit. Jika venv/.env muncul sebagai untracked yang akan di-add, fix .gitignore dulu sebelum commit.

**Proposed Solution** (untuk Agent A):
1. Agent A verify .gitignore di repo GitHub — pastikan comprehensive version (107 lines) yang ada, bukan minimal (2 lines)
2. Agent A JANGAN commit .gitignore tanpa coordinate dengan Agent B (SHARED file per OWNERSHIP.md)
3. Atau: pisahkan .gitignore menjadi 2 files: `.gitignore` (Agent A zone, project-level) + `.gitignore.backend` (Agent B zone, backend-specific) — tapi ini butuh git config
4. Atau: tambah pre-commit hook yang verify .gitignore tidak ter-reset

**Status**: Open — needs investigation & coordination dengan Agent A
