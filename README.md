<div align="center">

<img src="Billforge_Project_Code/data/images/logo5.png" alt="BillForge Logo" width="180">

# BillForge — KUET Teachers' Edition

### An Automatic Bill Management & Generation System

*Automated, bilingual (Bangla/English) examination-bill generation for the teachers of Khulna University of Engineering & Technology (KUET).*

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](#system-requirements)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-3776AB)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](Billforge_Project_Code/License.txt)
[![Status](https://img.shields.io/badge/Status-Academic%20Project-success)](#authors--acknowledgements)

</div>

---

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [How It Works](#how-it-works)
4. [The Input Document & Bill Categories](#the-input-document--bill-categories)
5. [System Requirements](#system-requirements)
6. [Tech Stack](#tech-stack)
7. [Project Structure](#project-structure)
8. [Installation](#installation)
9. [Usage Guide](#usage-guide)
10. [Authentication & Security](#authentication--security)
11. [Configuration Files](#configuration-files)
12. [Packaging as an Executable](#packaging-as-an-executable)
13. [Contributing](#contributing)
14. [Authors & Acknowledgements](#authors--acknowledgements)
15. [License](#license)

---

## Overview

**BillForge** is a desktop-based automation tool that drastically reduces the manual effort involved in preparing examination remuneration bills for teachers. Every semester and during backlog examinations, KUET's departments must compute individual payments for dozens of teaching staff based on a wide variety of examination duties (question setting, script examining, tabulation, viva-voce, and many more).

Manually extracting this data from consolidated duty sheets and calculating the exact amount owed to each teacher — in **Bengali**, with numbers converted to words — is tedious and error-prone. BillForge reads a structured Microsoft Word (`.docx`) duty document, parses every relevant table, applies the official rate logic, and produces a **ready-to-print individual Excel bill (`.xlsx`) for each teacher** in Bengali. It can even dispatch those bills by email automatically.

### Two Editions

BillForge ships with two specialised pipelines, selectable from the welcome screen:

| Edition | Use Case | Theme |
| --- | --- | --- |
| **General Version** | Regular semester examinations | Green |
| **Backlog Version** | Backlog / supplementary examinations | Red |

---

## Key Features

- **Fully automated bill generation** — reads a `.docx` duty document and outputs one bilingual Excel bill per teacher.
- **Two processing pipelines** — dedicated logic for *General* and *Backlog* examinations.
- **Bilingual output** — generates bills in **Bangla**, with English department names, designations, and years translated automatically.
- **Number-to-words conversion** — converts any monetary figure into Bangla words (e.g. `১২৫০.৫০` → "এক হাজার দুইশত পঞ্চাশ টাকা পঞ্চাশ পয়সা মাত্র").
- **Automatic rate logic** — applies per-student and per-khata rates, minimum charges, and lab-credit scaling defined in the rate template.
- **Built-in authentication** — secure user sign-up and login with **SHA-256 hashed** credentials stored in an embedded SQLite database.
- **Email distribution** — automatically emails each generated bill to the corresponding teacher via SMTP (Gmail).
- **Progress & loading UI** — animated GIF welcome screen and threaded progress bars so the GUI never freezes during long operations.
- **Error reporting** — a dedicated window lists any data mismatches (e.g. an unrecognised teacher name in a table) so the document can be corrected.
- **Standalone executable** — distributable as a one-file Windows `.exe` via PyInstaller.

---

## How It Works

```text
 ┌──────────────┐     ┌─────────────────┐     ┌────────────────────┐
 │  .docx duty  │ ──▶ │  Table Parser    │ ──▶ │  Per-teacher data   │
 │  document    │     │  (python-docx)   │     │  models (Teacher)   │
 └──────────────┘     └─────────────────┘     └─────────┬──────────┘
                                                        │
                         ┌──────────────────────────────┘
                         ▼
 ┌─────────────────┐     ┌─────────────────┐     ┌────────────────────┐
 │  Rate template  │ ──▶ │  Bill Calculator │ ──▶ │  Bangla .xlsx bill │
 │  (.xlsx)        │     │  + Bangla        │     │  per teacher       │
 └─────────────────┘     │  translator      │     └─────────┬──────────┘
                         └─────────────────┘               │
                                                           ▼
                                              ┌────────────────────────┐
                                              │  Email dispatch (SMTP) │
                                              └────────────────────────┘
```

**Step-by-step workflow:**

1. **Launch** the app and pick *General* or *Backlog* on the welcome screen.
2. **Log in** (or sign up the first time) with your credentials.
3. On the **dashboard**, select three inputs:
   - the `.docx` duty document,
   - the `.xlsx` email/contact file,
   - the destination folder for the generated bills.
4. Click **Generate** — BillForge parses the document's tables, builds a `Teacher` object per staff member, applies the rate logic, writes a personalised Bangla bill, and saves it as `<Teacher Name>.xlsx`.
5. (Optional) Click **Send Email** to dispatch each bill to the teacher's email address automatically.

---

## The Input Document & Bill Categories

BillForge expects a single `.docx` file whose body contains a sequence of **underlined-heading tables**. Each table corresponds to one examination duty category. The parser maps table-by-table to the following bill categories:

| # | Category (Table) | Description |
| --- | --- | --- |
| 1 | Teacher Information | Name, designation, department |
| 2 | Question Paper Moderation Board | Chairman / Member roles |
| 3 | Question Paper Setter & Script Examiner | Per-student script counts & rates |
| 4 | Examiners of Class Tests | Class-test counts per course |
| 5 | Examiners of Sessional Classes | Lab-credit-scaled payments |
| 6 | Script Scrutinizer | Scrutiny duties |
| 7 | Tabulation | Tabulation work |
| 8 | Typing & Drawing | Typing/drawing duties |
| 9 | Central Viva-Voce | Viva participation |
| 10 | Student Advising | Advising duties |
| 11 | Seminar | Seminar participation (group size aware) |
| 12 | Thesis Progress Defense | Thesis committee work |
| 13 | Final Grade Sheet Verification | Verification duties |
| 14 | Course Coordinator | Coordination allowance |
| 15 | List of Duty | Miscellaneous duty list |

> The parser recognises tables by their **order** and validates that every teacher name it encounters exists in Table 1. Any mismatch is surfaced in the **Error Report** window.

---

## System Requirements

- **OS:** Windows 10 / 11 (the app uses `win32com` / `xlwings` and Windows-specific resource paths).
- **Python:** 3.8 or newer.
- **Microsoft Excel** installed (required by `xlwings` for live recalculation of totals).
- **Microsoft Word** `.docx` documents as input.

---

## Tech Stack

| Area | Technology |
| --- | --- |
| Language | Python 3 |
| GUI | Tkinter + Pillow (images / animated GIFs) |
| Word parsing | `python-docx`, `docx2txt` |
| Excel I/O | `openpyxl`, `xlwings`, `pandas`, `xlrd` |
| Storage | `sqlite3` + `pickle` (credentials & app data) |
| Email | `smtplib` (MIME) |
| Windows interop | `pywin32` (`win32com.client`) |
| Translation | Custom Bangla dictionaries + `googletrans` |
| Packaging | PyInstaller |

---

## Project Structure

```text
BillForge/
├── BillForge.mp4                      # Demo video
├── BillForge - Swaraj.pptx            # Project presentation
├── User Manual.pptx                   # User manual deck
├── Dependencies.txt                   # Dependency list & driver info
├── README.md                          # This file
└── Billforge_Project_Code/
    ├── GUI_WelcomeScreen.py           # ENTRY POINT — version selection
    ├── GUI_Login_For_BacklogDataProcessing.py
    ├── GUI_Login_ForGeneralDataProceaaingDashboard.py
    ├── GUI_Dashboard_Backlog.py       # Backlog dashboard
    ├── GUI_Dashboard_For_GeneralDataProcessing.py  # General dashboard
    ├── GUI_Sign_Up.py                 # Sign-up screen
    ├── datasave.py                    # SQLite save (credentials/data)
    ├── showdata.py                    # SQLite read (credentials/data)
    ├── test.py / showdata.py
    ├── License.txt
    ├── Backend/
    │   ├── BacklogProcessing.py       # Core backlog bill engine
    │   ├── GeneralDataProcessing.py   # Core general bill engine
    │   ├── Year_Extractor_Module.py   # Extracts year/semester from .docx
    │   ├── Digit_To_BanglaTaka_ConverterApi.py  # Number → Bangla words
    │   ├── EmailProcessing.py         # Reads email list, triggers sends
    │   └── EmailSendingModule.py      # SMTP send per teacher
    └── data/
        ├── database/                  # BillForge.db, summarydb.db (SQLite)
        ├── excel-files/               # Templates & lookup tables
        │   ├── templatebill.xlsx          # General rate template
        │   ├── templatebill_backlog.xlsx  # Backlog rate template
        │   ├── bangla_teachers_name.xlsx  # English → Bangla name map
        │   └── Additional_data.xlsx       # Email credentials config
        └── images/                    # UI assets, logos, animated GIFs
```

---

## Installation

### Option A — Run from source (recommended for developers)

1. **Clone the repository**

   ```bash
   git clone https://github.com/Swaraj44/BillForge.git
   cd BillForge/Billforge_Project_Code
   ```

2. **(Recommended) Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   ```

3. **Install the dependencies**

   ```bash
   pip install openpyxl requests xlwings python-docx googletrans==4.0.0-rc1 \
               pywin32 pillow docx2txt pandas xlrd
   ```

   > `sqlite3`, `pickle`, `tkinter`, `pathlib`, `email`, `smtplib`, `threading`, `hashlib`, `webbrowser`, `os`, `sys` and `time` are part of the **Python Standard Library** and need no installation.

4. **Launch the application**

   ```bash
   python GUI_WelcomeScreen.py
   ```

### Option B — Use the pre-built installer (Windows)

A ready-to-use Windows setup executable is available on Google Drive — see the link in the original project distribution. No Python installation is required.

---

## Usage Guide

1. **Start** the app (`python GUI_WelcomeScreen.py`). The animated welcome screen appears.
2. **Choose an edition:**
   - *Button 1* → **General Version** (green login)
   - *Button 2* → **Backlog Version** (red login)
3. **Authenticate.** On first run, click **Sign Up** to create a user, then log in.
4. **Provide inputs** on the dashboard:
   - **Select Bill Docx File** → the examination duty `.docx`.
   - **Select Excel File** → the `.xlsx` containing teacher names + email addresses.
   - **Select Destination** → the output folder for generated bills.
5. **Generate.** Click the **Generate** button. A progress bar appears while bills are produced. Each teacher receives a file named `<Teacher Name>.xlsx`.
6. **(Optional) Edit Email** — opens the selected Excel file so contacts can be adjusted.
7. **(Optional) Send Email** — dispatches every generated bill to its teacher via email.
8. **Review errors** — if any table contains an unrecognised teacher or empty cell, the **Error Report** window lists the problems for correction.

---

## Authentication & Security

- Credentials are stored locally in an embedded **SQLite** database (`data/database/BillForge.db`).
- Passwords are **never stored in plain text** — they are hashed with **SHA-256** before being persisted (see `GUI_Sign_Up.py` and the login modules).
- Each record is serialised with `pickle` into a `BLOB` column, keyed by username.

---

## Configuration Files

Located under `Billforge_Project_Code/data/excel-files/`:

| File | Purpose |
| --- | --- |
| `templatebill.xlsx` | **General** rate template — per-student charges, minimum script charges, sessional per-student charge, etc. |
| `templatebill_backlog.xlsx` | **Backlog** rate template (same role, backlog rules). |
| `bangla_teachers_name.xlsx` | Lookup of English teacher names → Bangla names + salary ID. |
| `Additional_data.xlsx` | Sender **email address** and **app password** used by the email module. |

> **Tip:** To enable email sending, enter a Gmail sender address and a [Google App Password](https://support.google.com/accounts/answer/185833) into `Additional_data.xlsx` (Sheet1).

---

## Packaging as an Executable

BillForge is designed to be frozen with **PyInstaller**. The code already provides a `resource_path()` helper in every module that resolves bundled assets both in development and inside the PyInstaller `_MEIPASS` temporary folder.

Example one-file build (run from `Billforge_Project_Code/`):

```bash
pyinstaller --noconfirm --onefile --windowed ^
  --add-data "data;data" ^
  --icon "data/images/general_logo.ico" ^
  GUI_WelcomeScreen.py
```

The resulting `dist/GUI_WelcomeScreen.exe` is a standalone Windows application.


## Authors & Acknowledgements

**Developed by**

- **Swaraj Chandra Biswas**
- **Chinmoy Modak Turjo** 


*Department of Computer Science and Engineering,*
*Khulna University of Engineering & Technology (KUET), Khulna, Bangladesh.*

**Under the supervision of**

- **Dr. Sheikh Imran Hossain** — Assistant Professor, Department of Computer Science and Engineering, KUET.

---

## License

Copyright © 2024 Swaraj Chandra Biswas & Chinmoy Modak Turjo .

This project is licensed under the **MIT License**. See [`Billforge_Project_Code/License.txt`](Billforge_Project_Code/License.txt) for the full notice. The software is provided **"as is"**, without warranty of any kind.
