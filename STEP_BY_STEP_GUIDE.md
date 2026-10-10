# 🛠️ TalentAI: Step-by-Step DIY Master Roadmap
*Apne project ko khud customize, live deploy aur free APK banane ki complete guide.*

---

## 📌 Index / Steps Overview
- **Step 1:** Project Files aur Code Structure Samajhna
- **Step 2:** UI & Text Khud Customize Karna (Colors, Titles, Logos)
- **Step 3:** Real Jobs Data Add/Edit Karna (`jobs.json`)
- **Step 4:** Supabase Real-Time Backend Connect Karna (Free 24/7 Auth & DB)
- **Step 5:** Free 24/7 Live Website Host Karna (Netlify / Vercel / GitHub)
- **Step 6:** Free Android .APK Build Karna (Bina FlutterFlow ko paise diye)
- **Step 7:** Teacher / Submission ke Samne Live Demo Kaise Dena Hai

---

## 🔹 STEP 1: Files aur Code Structure Samajhna

Aapke folder me 5 important files hain:
1. `index.html` → Poora frontend: Design, buttons, tabs, search, tracker logic.
2. `jobs.json` → Saari 50 jobs ka data (title, company, salary, skills, match score).
3. `manifest.json` → Mobile PWA configuration (app icon, app name).
4. `supabase_schema.sql` → Database tables (users, jobs, saved_jobs, applications).
5. `server.js` → Local preview server (`node server.js` chala ke `localhost:3000` pe dekhne ke liye).

---

## 🔹 STEP 2: UI aur Text Khud Customize Karna

Agar aapko app ka naam, colors ya koi text change karna hai, to `index.html` file open karo:

### 1. App ka Name ya Tagline badalna:
- Line 60 ke aas-paas dekho:
  ```html
  <h1 class="text-base font-bold text-slate-900 leading-none">
    Talent<span class="text-indigo-600">AI</span>
  </h1>
  ```
  Yaha `TalentAI` ki jagah apna koi bhi custom naam de sakte ho.

### 2. Colors change karna:
- Abhi primary color `indigo-600` hai.
- Agar aapko Blue chahiye, to code me `indigo-600` ko `blue-600` se replace kar do.
- Agar Purple chahiye, to `purple-600` kar do.

### 3. Demo Candidate Profile badalna:
- `index.html` ke andar JavaScript section me line ~300 ke aas-paas:
  ```js
  let userCandidateSkills = ['Python', 'React', 'SQL', 'Git', 'Node.js', 'FastAPI'];
  ```
  Yaha aap candidate ki skills apne hisaab se customize kar sakte ho.

---

## 🔹 STEP 3: Real Jobs Data Edit Karna (`jobs.json`)

Agar aapko nayi jobs add karni hain ya existing jobs ka salary/title badalna hai:
1. `jobs.json` open karo.
2. Har job ka format aisa hai:
   ```json
   {
     "id": 1,
     "title": "Junior AI Engineer",
     "company": "NeuroTech Labs",
     "logo": "💼",
     "location": "Bengaluru (Hybrid)",
     "type": "Full Time",
     "mode": "Hybrid",
     "salary": "₹8 - ₹12 LPA",
     "experience": "0-2 years",
     "matchScore": 94,
     "matchingSkills": ["Python", "TensorFlow", "NLP", "Git"],
     "missingSkills": ["Docker"],
     "whyMatch": "Demonstrated foundation in Python and applied ML pipelines.",
     "description": "Build NLP pipelines, fine-tune models, and deploy reliable APIs.",
     "applyUrl": "https://example.com/apply"
   }
   ```
3. Nayi job add karne ke liye bas is block ko copy-paste karke `id` number increase kar do.

---

## 🔹 STEP 4: Real-Time Supabase Cloud DB Connect Karna (Free 24/7)

Agar aap chahte ho ki real users ka account bane aur unka data 24/7 cloud par save ho:

1. **Supabase par account banao:**
   - [supabase.com](https://supabase.com) par jao aur free me sign up karo.
   - **"New Project"** par click karo (Project Name: `talentai-db`).
2. **Database Tables Create karo:**
   - Supabase dashboard me left side **SQL Editor** par jao.
   - Apne project ki `supabase_schema.sql` file ka poora code copy karke waha paste karo aur **Run** dabao. Saare tables (`profiles`, `jobs`, `applications`, `saved_jobs`) instant ban jayenge!
3. **API Keys Copy karo:**
   - Supabase me **Project Settings ➜ API** me jao.
   - `Project URL` aur `anon public key` copy karo.
4. **App me Link karo:**
   - TalentAI app open karo.
   - Top right me **⚙️ Settings Icon** dabao.
   - URL aur Key paste karke **Save & Connect** par click karo. Ab aapka app real cloud se connect ho gaya!

---

## 🔹 STEP 5: Free 24/7 Live Website Host Karna (30 Seconds)

Aapko apna laptop on rakhne ki zaroorat nahi hai. Free me live host karo:

### Method 1: Netlify Drop (Sabse Fast - No Code Needed)
1. Browser me open karo: **[app.netlify.com/drop](https://app.netlify.com/drop)**
2. Apna folder `c:\Users\Rohan\Downloads\AI JOB FINDER` drag karke browser screen par drop kar do.
3. 10 second me aapko live link mil jayega:
   `https://talentai-rohan.netlify.app`
4. Ye link 24/7 live rahega!

### Method 2: Vercel
1. [vercel.com](https://vercel.com) par free account banao.
2. Add New Project ➜ Upload your folder.
3. Deploy!

---

## 🔹 STEP 6: Free Android .APK Build Karna (100% Free)

FlutterFlow ke paid APK build ko bypass karke free APK banane ke 2 tareeqe:

### Option A: WebIntoApp (Direct 1-Minute APK)
1. Jao: **[webintoapp.com](https://www.webintoapp.com)**
2. **"Make App"** par click karo.
3. Apna live Netlify link daalo (e.g. `https://talentai-rohan.netlify.app`).
4. App Name: `TalentAI`
5. Icon select karo (ya default rehne do).
6. **"Get APK"** par click karo.
7. Direct `.apk` file download ho jayegi. Isko WhatsApp ya Drive se phone me bhej kar install kar lo!

### Option B: MIT App Inventor (Free Native Webview APK)
1. Jao: **[ai2.appinventor.mit.edu](https://ai2.appinventor.mit.edu)**
2. New Project: `TalentAI`.
3. Left side se **WebViewer** component ko screen ke beech me drag karo.
4. Right side me properties me **HomeUrl** me apna live link paste karo.
5. Top menu me **Build ➜ Android App (.apk)** click karo.
6. QR code scan karke ya direct file download karke phone me install kar lo!

---

## 🔹 STEP 7: Submission & Teacher Demo Tips

Teacher ko demo dete waqt ye 4 points highlight karna:
1. **Real-time Match Scoring:** Kisi bhi job par click karke dikhana ki AI applicant ki skills match karke score (e.g. 94%) aur *Matching vs Missing Skills* kaise calculate karta hai.
2. **Application Tracker:** Job me **"Apply for Position"** dabana, confetti animation chalegi aur job direct *Tracker* me chali jayegi status update ke liye (`Applied` ➜ `Interview` ➜ `Offer`).
3. **Responsive Mobile-First Architecture:** Dikhao ki ye desktop browser me bhi clean mobile frame me chalti hai aur Android phone me installed app ki tarah native perform karti hai.
4. **Cloud Database Readiness:** Supabase SQL schema dikha kar explain karna ki backend me Row Level Security (RLS) use ki gayi hai taaki users ka data secure rahe.
