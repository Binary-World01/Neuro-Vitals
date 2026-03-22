# 🚀 Quick Start Guide - Neuro-Vitals

## Simple Setup (< 5 minutes)

### Step 1: Open TWO Terminal Windows

#### Terminal 1 - Backend
```bash
cd c:\Users\Parth\OneDrive\Desktop\PuneHack\neuro-vitals\backend
pip install fastapi uvicorn pydantic pydantic-settings python-multipart
python -m app.main
```

Server will run at: **http://localhost:8000**

#### Terminal 2 - Frontend
```bash
cd c:\Users\Parth\OneDrive\Desktop\PuneHack\neuro-vitals\frontend-app
python -m http.server 5500
```

Open browser to: **http://localhost:5500**

---

## What You'll See

### 🎯 Working Features

1. **Symptom Analysis Tab**
   - Fill in patient details
   - Click "Analyze Symptoms"
   - See AI diagnosis with reasoning

2. **Adversarial Diagnosis Tab**
   - Click "Start AI Debate"
   - Watch 3 AIs debate (Prosecutor, Defense, Judge)
   - This is THE WOW feature!

3. **Health Trajectory Tab**
   - Auto-loads 6-month forecast
   - See risk with vs without intervention
   - Interactive Chart.js graph

4. **Community Health Tab**
   - Click tab to load outbreak map
   - View heat map of health reports
   - See transmission velocity alerts

---

## 📝 Demo Script (3 Minutes)

### Setup Demo Patient
- Age: 45
- Gender: Male
- Symptom: chest pain
- Severity: 8/10
- Duration: 2 days
- Medical History: high blood pressure

### Demo Flow
1. **Start** with Symptom Analysis (30 sec)
2. **Switch** to Adversarial Debate (60 sec) ← THE SHOWSTOPPER
3. **Show** Trajectory graph (30 sec)
4. **Show** Community map (30 sec)
5. **Close** with impact statement (30 sec)

---

## 🏆 Pitch Talking Points

"We're not building another symptom checker. We're building the FIRST adversarial medical AI that debates itself to eliminate bias. It predicts health 6 months into the future. And it detects outbreaks 3 days before health departments."

**Why we win:**
- ⚔️ Only team with adversarial AI
- 📈 Only team with 6-month forecasting
- 🌐 Only team with outbreak prediction
- 💯 Everything works, no mock slides

---

## 🔧 Troubleshooting

**If backend doesn't start:**
```bash
pip install --upgrade pip
pip install fastapi==0.104.1 uvicorn==0.24.0 pydantic==2.5.0
python -m app.main
```

**If frontend shows error:**
- Make sure backend is running first
- Check http://localhost:8000/docs (should show API docs)
- Open browser console (F12) to see any errors

---

## ✅ Pre-Flight Checklist

Before hackathon demo:
- [ ] Backend running (check http://localhost:8000)
- [ ] Frontend running (check http://localhost:5500)
- [ ] All 4 tabs work
- [ ] Adversarial debate runs
- [ ] Graph shows on trajectory tab
- [ ] Map loads on community tab
- [ ] Demo script rehearsed 3x

**You're ready to win! 🏆**
