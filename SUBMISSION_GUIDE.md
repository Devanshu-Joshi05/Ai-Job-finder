# TalentAI – AI-Powered Job Finder & Career Tracker
**Project Submission & Demonstration Guide**

---

## 📌 Project Overview
**TalentAI** is an AI-driven, mobile-first career acceleration platform tailored for students, fresh graduates, and tech job seekers. It analyzes candidate skillsets against real-world tech job requirements to generate real-time **AI Compatibility Match Scores (0–100%)**, explains exact skill gaps, tracks live applications through hiring stages, and optimizes candidate resumes.

---

## 📱 Core Features Built in MVP

1. **AI Match Score Engine (0–100%)**
   - Automatically cross-checks applicant skills (e.g. Python, React, SQL, TensorFlow) with job criteria.
   - Highlights **Matching Skills (✓)** and **Missing Skills to Prepare (△)**.
   - Displays clear natural language explanations (*"Why you match"*).

2. **50 Pre-loaded Tech & AI Roles**
   - Covers Junior AI Engineers, ML Interns, Fullstack React/Node, Data Analysts, DevOps, Cybersecurity, Prompt Engineers, Flutter/Android, etc.
   - Fast multi-filter system: **Remote**, **Internships**, **Full Time**, and **90%+ High Match**.
   - Real-time instant search by title, company, or tech stack.

3. **Bookmark / Saved Jobs**
   - Quick one-tap bookmarking to review and shortlist opportunities.
   - Persisted locally with instant remove / view capability.

4. **Interactive Application Tracker (Kanban-Style)**
   - Tracks 4 hiring stages: `Applied`, `Interview`, `Offer`, and `Rejected`.
   - Update interview statuses dynamically.
   - Confetti animation and celebration toast upon applying.

5. **Profile & Resume AI Analyzer**
   - Profile strength indicator (92% benchmark).
   - Core skill chip manager (add/remove skills on the fly).
   - Resume upload simulator with AI feedback tips.

---

## 🛠️ Tech Architecture & Files in Workspace

| File | Purpose |
|---|---|
| [index.html](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/index.html) | Complete Native Mobile App interface (Tailwind CSS, Phosphor Icons, Responsive Frame) |
| [jobs.json](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/jobs.json) | 50 high-quality job listings with salary, match scores, and requirements |
| [manifest.json](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/manifest.json) | PWA configuration for installing as a standalone Android app on any phone |
| [server.js](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/server.js) | Lightweight Node.js local preview server |
| [supabase_schema.sql](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/supabase_schema.sql) | Production PostgreSQL schema with Row-Level-Security (RLS) policies for Supabase |

---

## 🚀 How to Run & Present Right Now

### 1. View in Browser on your Laptop:
Open your browser and navigate to:
👉 **[http://localhost:3000](http://localhost:3000)**

*(Alternatively, you can double-click [index.html](file:///c:/Users/Rohan/Downloads/AI%20JOB%20FINDER/index.html) directly to open it).*

### 2. How to Run on your Android Phone (Install as App):
1. Connect your phone to the same Wi-Fi as your laptop.
2. In PowerShell or Command Prompt, run `ipconfig` to get your Laptop's IPv4 address (e.g. `192.168.1.15`).
3. Open Chrome on your phone and type: `http://<your-laptop-ip>:3000`.
4. Tap Chrome menu (`⋮`) ➜ **"Add to Home screen"** or **"Install App"**.
5. It will install with the **TalentAI** app icon and open full-screen like a native Android APK!
