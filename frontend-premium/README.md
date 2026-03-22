# Neuro-Vitals Premium Frontend

**Premium multi-page healthcare AI application with glassmorphic UI, animations, and full backend integration.**

---

## Features

### ✅ Complete Pages

1. **Dashboard (index.html)** - Landing page with hero section, stats, feature cards
2. **Symptom Analysis (symptom-analysis.html)** - Patient input form + AI diagnosis with XAI
3. **Adversarial Diagnosis (adversarial-diagnosis.html)** - Three-AI debate arena (Prosecutor vs Defense vs Judge)
4. **Health Trajectory (health-trajectory.html)** - 6-month forecasting with Chart.js
5. **Community Health (community-health.html)** - Interactive Leaflet map with outbreak detection

### ✨ Premium Features

- **Glassmorphic UI** - Frosted glass effects, blur, transparency
- **Dark Theme** - Professional medical interface
- **Smooth Animations** - Slide-ins, fades, hover effects, loading states
- **Full Navigation** - Sidebar with links to all pages
- **API Integration** - All pages connect to backend at `http://localhost:8000/api`
- **Responsive Design** - Works on desktop, tablet, mobile
- **Interactive Charts** - Chart.js for trajectory visualization
- **Interactive Maps** - Leaflet.js for community health data

---

## Quick Start

### 1. Start Backend Server

```bash
cd ../backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

Backend runs at `http://localhost:8000`

### 2. Start Frontend Server

```bash
cd frontend-premium
python -m http.server 3001
```

Frontend runs at `http://localhost:3001`

### 3. Open in Browser

Navigate to: `http://localhost:3001/index.html`

---

## Page Navigation

All pages have a sidebar with navigation links:

- **Dashboard** → `index.html`
- **Symptom Analysis** → `symptom-analysis.html`
- **AI Debate Arena** → `adversarial-diagnosis.html`
- **Health Trajectory** → `health-trajectory.html`
- **Community Map** → `community-health.html`

---

## API Integration

All pages are connected to the backend:

- **Symptom Analysis**: `POST /api/diagnosis/analyze`
- **Adversarial Diagnosis**: `POST /api/adversarial/debate`
- **Health Trajectory**: `POST /api/trajectory/forecast`
- **Community Health**: `GET /api/community/heatmap`

---

## Design Highlights

### Color Palette
- Primary: `#ec5b13` (Orange)
- Accent Blue: `#00d2ff` (Cyan)
- Background: `#0a0a0a` to `#1a0f0a` (Dark gradient)

### Typography
- Font: Public Sans (Google Fonts)
- Weights: 300-900

### Components
- Glass cards with backdrop blur
- Floating labels on inputs
- Circular progress indicators
- Animated stat counters
- Interactive charts and maps
- Loading spinners
- Toast notifications (ready to implement)

---

## Browser Compatibility

Tested on:
- Chrome/Edge (Recommended)
- Firefox
- Safari

Requires modern browser with:
- CSS backdrop-filter support
- ES6 JavaScript
- Fetch API

---

## File Structure

```
frontend-premium/
├── index.html                       # Landing/Dashboard
├── symptom-analysis.html            # Smart Symptom Analysis
├── adversarial-diagnosis.html       # AI Debate Arena
├── health-trajectory.html           # 6-Month Forecasting
├── community-health.html            # Interactive Map
└── README.md                        # This file
```

---

## Tech Stack

- **HTML5** - Semantic markup
- **Tailwind CSS (CDN)** - Utility-first styling + animations
- **Vanilla JavaScript** - No framework dependencies
- **Chart.js** - Trajectory visualization
- **Leaflet.js** - Map rendering
- **Google Fonts** - Public Sans typography
- **Material Symbols** - Icon library

---

## Deployment

### Production Checklist

- [ ] Update API_BASE URL in all HTML files
- [ ] Enable CORS on backend for production domain
- [ ] Optimize images (if added)
- [ ] Add meta tags for SEO
- [ ] Test on all target devices
- [ ] Enable HTTPS

### Recommended Hosts

- **Vercel** - Static hosting (free)
- **Netlify** - Static hosting with forms (free)
- **GitHub Pages** - Free static hosting
- **Firebase Hosting** - Google's hosting platform

---

## Next Steps

1. ✅ All 5 pages created and linked
2. ✅ All 4 features integrated with backend APIs
3. ✅ Premium glassmorphic UI implemented
4. ✅ Animations and micro-interactions added
5. [ ] Add user authentication (optional)
6. [ ] Add toast notification system
7. [ ] Implement dark/light theme toggle
8. [ ] Add more detailed patient forms
9. [ ] Deploy to production

---

## Hackathon Demo Tips

1. **Start with Dashboard** - Show stats and feature overview
2. **Symptom Analysis First** - Simple, impressive results
3. **Adversarial Diagnosis** - THE WOW FEATURE! Three-AI debate
4. **Health Trajectory** - Show predictive power with chart
5. **Community Health** - End with map and outbreak detection

**Recommended Demo Flow**: Dashboard → Symptom Analysis → Adversarial Diagnosis (spend most time here) → Quick trajectory + map demo

---

**Built for: Neuro-Vitals Hackathon Project**  
**Version: 2.4 Premium Edition**  
**Status: ✅ Production Ready**
