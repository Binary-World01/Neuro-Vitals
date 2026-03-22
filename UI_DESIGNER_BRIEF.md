# UI Designer Brief - Neuro-Vitals

## Project Overview

**Name**: Neuro-Vitals - Predictive Health Intelligence System  
**Goal**: Hackathon-winning healthcare AI application  
**Your Mission**: Design a premium, world-class UI for 4 revolutionary health features

---

## What You're Designing

A **single-page web application** with **4 main features** accessible via tabs/navigation.

---

## Feature 1: Smart Symptom Analysis

### What It Does
Patient inputs symptoms → AI provides diagnosis with explainable reasoning

### Input Fields Needed
- Patient ID (text)
- Age (number)
- Gender (dropdown: male/female/other)
- Primary symptom description (text)
- Severity level (1-10 scale)
- Duration in days (number)
- Medical history (optional text/tags)

### Output to Display
- **Diagnosis name** (main heading)
- **Confidence score** (0-100%)
- **Reasoning steps** (bulleted list - this is XAI/Explainable AI)
- **Recommendations** (bulleted list)

### API Integration
`POST /api/diagnosis/analyze` - see API_REFERENCE.md for details

---

## Feature 2: Adversarial Diagnosis Engine ⭐

### What It Does
**THE WOW FEATURE** - Three AIs debate the diagnosis:
1. **Prosecutor AI** - argues FOR a primary diagnosis
2. **Defense AI** - argues AGAINST, presents alternative
3. **Judge AI** - synthesizes both arguments, final verdict

### User Action
Single button: "Start AI Debate" (or your creative take)

### Output to Display (3 Sections)

**Prosecutor AI:**
- Their diagnosis
- Confidence percentage
- Supporting evidence (list)
- Rebuttals to alternatives (list)

**Defense AI:**
- Alternative diagnosis
- Confidence percentage  
- Contradictory evidence (list)
- Why their diagnosis is more likely (paragraph)

**Judge AI (Final Verdict):**
- Final diagnosis
- Confidence percentage
- Synthesis of both arguments (paragraph)
- Recommended medical tests (list)
- Debate summary (paragraph)

### API Integration
`POST /api/adversarial/debate`

### Design Note
This is the most unique feature - make it visually stunning!

---

## Feature 3: Temporal Health Trajectory

### What It Does
Shows **6-month health risk forecast** - two scenarios compared side-by-side

### Data to Visualize

**Graph/Chart:**
- X-axis: Time (Now, Month 1, Month 2, Month 3, Month 4, Month 5, Month 6)
- Y-axis: Health risk (0-100%)
- **Line 1**: "Without Intervention" (baseline - risk increases)
- **Line 2**: "With Intervention" (risk decreases)

**Key Metrics to Highlight:**
- Current risk percentage
- Month 6 risk WITHOUT intervention
- Month 6 risk WITH intervention  
- Risk reduction percentage

### API Integration
`POST /api/trajectory/forecast?diagnosis=X`

### Creative Freedom
- Choose your chart library (Chart.js, Recharts, D3.js, etc.)
- Design the visualization style
- How to present the comparison

---

## Feature 4: Community Health Intelligence

### What It Does
Real-time **outbreak detection** through crowdsourced health data

### Data to Display

**Statistics Dashboard:**
- Total reports in last 48 hours
- Reports in last 24 hours
- Transmission velocity (% change)
- Status: "Normal" or "Outbreak Detected!"

**Alert System:**
- If outbreak detected, show prominent warning/alert
- Display alert message

**Interactive Map:**
- Geographic heat map of health reports
- Markers showing individual reports
- Marker colors based on severity (high/medium/low)
- Click markers to see symptom details

**Trending Data:**
- Top 5 most reported symptoms with counts
- Area breakdown (neighborhoods/districts with report counts)

### API Integration
`GET /api/community/heatmap`

### Required Integration
Must use a **mapping library** - Options:
- Leaflet.js (current)
- Google Maps
- Mapbox
- Your choice

---

## Technical Requirements

### Backend API
- **Already built and running** at `http://localhost:8000`
- **Complete API docs** at `http://localhost:8000/docs`
- **Your job**: Frontend only, consume these APIs

### Must Integrate
1. **Charting library** for Feature 3 (trajectory visualization)
2. **Mapping library** for Feature 4 (heat map)
3. **Form handling** for Features 1 & 2 (patient input)

### Tech Stack - Your Choice
- ✅ Framework: React, Vue, Svelte, Angular, or vanilla JS
- ✅ Styling: Tailwind, Material UI, Ant Design, styled-components, or custom CSS
- ✅ Animation: Framer Motion, GSAP, or CSS animations
- ✅ Charts: Chart.js, Recharts, Victory, D3.js
- ✅ Maps: Leaflet, Google Maps, Mapbox

---

## Brand & Target Audience

### Brand Identity
- **Medical AI** - must feel trustworthy, professional
- **Cutting-edge** - this is revolutionary technology
- **Hackathon winner** - needs that WOW factor

### Target Audience
- Healthcare professionals (doctors, nurses)
- Patients seeking diagnosis
- Hackathon judges (technical + medical experts)

---

## Design Priorities

1. **Trust & Credibility** - This is healthcare, users must trust it
2. **Clarity** - Complex medical data must be easy to understand
3. **Visual Impact** - Must impress judges at first glance
4. **Data Visualization** - Charts and graphs are critical
5. **Mobile Responsive** - Must work on all devices

---

## What Makes This Special

### Unique Selling Points (Emphasize These!)

1. **Adversarial AI** 🏆
   - NO other health app has AI debating itself
   - This is the killer feature - make it shine!

2. **Predictive Forecasting** 📈
   - Shows FUTURE health, not just current state
   - 6-month timeline is powerful

3. **Outbreak Detection** 🌐
   - Detects disease outbreaks before health departments
   - Real-world public health impact

4. **Explainable AI (XAI)** 🔍
   - Every diagnosis shows reasoning
   - Builds trust through transparency

---

## Creative Freedom

### You Control
✅ All visual design (colors, fonts, spacing, layout)  
✅ Component frameworks and libraries  
✅ Animation style and micro-interactions  
✅ Navigation patterns (tabs, sidebar, dropdown, etc.)  
✅ How data is presented  
✅ Mobile/desktop layouts  
✅ Icon choices  
✅ Loading states and transitions  
✅ Empty states and error messages

### You Must Include
❌ All 4 features (nothing can be removed)  
❌ All input fields listed  
❌ All output data displayed  
❌ API integration to backend  
❌ Chart for trajectory  
❌ Map for community health

---

## Reference Materials Provided

1. **API_REFERENCE.md** - Complete API documentation with request/response examples
2. **frontend/index.html** - Working reference implementation (you can do MUCH better!)
3. **Backend server** - Running at `http://localhost:8000` for testing

---

## Success Criteria

Your design will be successful when:

✅ All 4 features are fully functional  
✅ UI feels premium and world-class  
✅ Medical professionals would trust it  
✅ Judges would say "WOW!" at first glance  
✅ Mobile experience is excellent  
✅ Data visualizations are clear and beautiful  
✅ Brand feels innovative yet trustworthy

---

## Deliverables

- Fully functional frontend application
- All 4 features working with backend API
- Responsive design (mobile, tablet, desktop)
- Smooth animations and interactions
- Production-ready code

---

## Questions?

**Technical/API**: See `API_REFERENCE.md`  
**Current Implementation**: See `frontend/index.html`  
**Backend Testing**: `http://localhost:8000/docs`

---

**Your Task**: Take these 4 revolutionary features and make them look absolutely STUNNING. Show us what world-class healthcare AI should look like! 🚀
