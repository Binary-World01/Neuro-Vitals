# Neuro-Vitals - Vanilla JS App

**Production-ready healthcare AI platform with auth, onboarding wizard, and 4 AI features.**

---

## ✨ What's New

### 1. **Stunning Landing Page** (`index.html`)
- Glassmorphic purple-blue gradient design
- Sign In / Sign Up authentication
- Animated feature showcase
- localStorage-based auth system

### 2. **4-Step Onboarding Wizard** (`onboarding.html`)
- **Step 1:** Personal Identity (Name, Phone, DOB, Gender)
- **Step 2:** Physical Vitals (Height, Weight, Blood Group + BMI calculator)
- **Step 3:** Medical Context (Allergies, Conditions, Medications with tag inputs)
- **Step 4:** Emergency Protocol (Mandatory emergency contact)
- Smooth slide animations
- Segmented progress bar
- Form validation
- Profile saved to localStorage

### 3. **Dashboard** (`dashboard.html`)
- Personalized welcome with user name
- BMI display
- Quick stats
- Feature cards linking to all 4 AI features

### 4. **Enhanced Features** (Coming from premium version)
- Symptom Analysis (auto-uses logged-in user name)
- AI Debate Arena (prosecutor vs defense vs judge)
- Health Trajectory (6-month forecast with Chart.js)
- Community Health Map (Leaflet.js heat map)

---

## 🚀 Quick Start

### 1. Start Backend
```bash
cd ../backend
python -m app.main
```

### 2. Start Frontend
```bash
cd frontend-app
python -m http.server 3000
```

### 3. Open Browser
```
http://localhost:3000/index.html
```

---

## 📋 User Flow

1. **Landing Page** → Sign Up (creates account)
2. **Onboarding Wizard** → Complete 4 steps (saves profile)
3. **Dashboard** → Access all 4 AI features
4. **Features** → Use symptom analysis, AI debate, trajectory, community map

---

## 🎨 Design

- **Colors:** Purple (#667eea) + Cyan (#00d2ff)
- **Theme:** Dark with glassmorphic cards
- **Animations:** Smooth CSS transitions
- **Responsive:** Mobile-friendly

---

## 💾 Data Storage

- **LocalStorage Keys:**
  - `neurovitals_users` - Array of all registered users
  - `neurovitals_currentUser` - Currently logged-in user

---

## 🔒 Auth System

- Simple email/password
- Auto-redirect based on onboarding status
- Logout functionality
- Protected routes (requires login)

---

## 📱 Pages

| Page | URL | Description |
|------|-----|-------------|
| Landing | `index.html` | Sign in/up |
| Onboarding | `onboarding.html` | 4-step wizard |
| Dashboard | `dashboard.html` | Main hub |
| Symptom Analysis | `symptom-analysis.html` | AI diagnosis |
| AI Debate | `adversarial-diagnosis.html` | 3-AI debate |
| Trajectory | `health-trajectory.html` | 6-month forecast |
| Community Map | `community-health.html` | Heat map |

---

## ⚡ Performance

- No framework = Fast loading
- Minimal dependencies (Tailwind CDN)
- Optimized animations
- Lazy loading considerations

---

## 🛠️ Tech Stack

- HTML5 + Tailwind CSS (CDN)
- Vanilla JavaScript
- LocalStorage (state)
- Chart.js (graphs)
- Le aflet.js (maps)
- Material Symbols (icons)

---

## 🎯 Next Steps

Copy enhanced feature pages from `frontend-premium/` to `frontend-app/` and update them to:
- Use `js/utils.js` for auth
- Auto-fill user name from profile
- Integrate logout button

---

**Status:** ✅ Core app ready - Auth + Onboarding complete!
