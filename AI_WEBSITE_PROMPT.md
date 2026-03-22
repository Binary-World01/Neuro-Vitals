# AI Prompt: Build Neuro-Vitals - Premium Healthcare AI Website

## Project Brief

Build a **world-class, hackathon-winning healthcare AI web application** called "Neuro-Vitals" with 4 revolutionary features, premium UI design, unique animations, and seamless backend integration.

---

## Technical Stack Requirements

**Framework**: Use **Next.js 14+** with React and TypeScript  
**Styling**: **Tailwind CSS** + **Framer Motion** for animations  
**Charts**: **Recharts** or **Chart.js**  
**Maps**: **Leaflet.js** or **Mapbox**  
**Backend**: FastAPI (already built) at `http://localhost:8000/api`  
**State Management**: React Context or Zustand  
**UI Components**: **shadcn/ui** for consistent, premium components

---

## Design Philosophy

### Visual Style
- **Medical + Futuristic**: Blend clinical professionalism with cutting-edge tech aesthetics
- **Color Scheme**: Primary purple/blue gradient (#667eea to #764ba2), with accent colors for different features
- **Typography**: Inter font family (clean, modern, professional)
- **Glassmorphism**: Use frosted glass effects for cards and modals
- **Neumorphism**: Subtle for buttons and interactive elements
- **Dark Mode**: Implement dark/light theme toggle

### Animation Principles
- **Smooth & Purposeful**: 60fps animations, nothing jarring
- **Micro-interactions**: Hover effects, button presses, input focus
- **Page Transitions**: Smooth fade/slide between sections
- **Data Visualization**: Animated chart rendering
- **Loading States**: Skeleton screens + smooth spinners
- **Stagger Effects**: Elements appear sequentially, not all at once

### Premium UI Features
✅ Smooth parallax scrolling  
✅ Gradient backgrounds with animated mesh  
✅ Floating elements with subtle movement  
✅ Card hover effects (lift + shadow)  
✅ Interactive cursors on hover  
✅ Progress indicators with animations  
✅ Toast notifications for feedback  
✅ Modal animations (scale + fade)  
✅ Skeleton loading screens  
✅ Particle effects in header (optional)

---

## Application Structure

### Multi-Page Layout

**Pages to Create:**

1. **Landing Page** (`/`)
   - Hero section with animated gradient background
   - Feature showcase (4 main features with icons/cards)
   - How it works section
   - Statistics/impact section
   - CTA button to app
   - Footer with links

2. **App Dashboard** (`/app`)
   - Main application interface
   - Navigation sidebar OR top tabs
   - 4 feature sections accessible
   - Patient context panel (shows current patient data)

3. **Feature Pages** (or tabs within dashboard):
   - `/app/symptom-analysis`
   - `/app/adversarial-diagnosis`
   - `/app/health-trajectory`
   - `/app/community-health`

4. **About Page** (`/about`) - Optional
   - Technology explanation
   - Team info

---

## Feature 1: Smart Symptom Analysis

### Layout
**Two-column responsive layout:**
- Left: Input form with floating labels
- Right: Results display with animated appearance

### Input Form Design
```
Patient Information Card (glassmorphic card)
├── Patient ID (text input with icon)
├── Age & Gender (side-by-side, 50/50 split)
├── Primary Symptom (text input with autocomplete suggestions)
├── Severity Slider (animated, 1-10 with color gradient)
│   └── Visual feedback: Red (high) → Yellow (mid) → Green (low)
├── Duration (number input with unit selector: days/hours)
└── Medical History (tag input with chips)
    └── Animated chips with remove button
```

**Submit Button:**
- Large, prominent gradient button
- Ripple effect on click
- Morphs to loading spinner during API call
- Success animation (checkmark) on completion

### Results Display

**Initial State:**
- Subtle pulsing placeholder with "Waiting for analysis..."
- Blurred preview of result sections

**Loaded State (Animated Entrance):**
```
Results Card (slide-in from right)
├── Diagnosis Header
│   ├── Large text with gradient
│   └── Animated typewriter effect
├── Confidence Meter
│   ├── Circular progress indicator
│   ├── Animated fill from 0% to actual value
│   └── Color changes based on confidence level
├── Reasoning Section (XAI)
│   ├── Icon: 🔍 with pulse animation
│   ├── Each reason appears with stagger effect (0.1s delay each)
│   └── Expandable accordion for detailed reasoning
└── Recommendations
    ├── Icon: 💡 with glow effect
    ├── Cards with hover lift effect
    └── Priority badges (high/medium/low)
```

### Animations
- Form inputs: Focus animation with border glow
- Slider: Value bubble appears on interaction with bounce
- Submit: Button pulse → loading ring → success scale
- Results: Fade-in + slide-up with stagger (each section 0.2s apart)

### API Integration
`POST /api/diagnosis/analyze`

---

## Feature 2: Adversarial Diagnosis Engine ⭐ THE WOW FEATURE

### Concept
Three AI models engage in a visual debate - make this CINEMATIC!

### Layout Design
**Full-screen debate arena:**
```
Top: Action button + animated title
Middle: Three debate cards arranged dynamically
Bottom: Timeline/progress indicator
```

### Start Button
- Massive centered button with pulsing ring
- Text: "⚔️ Initiate AI Debate"
- Hover: 3D tilt effect + shadow expansion
- Click: Explodes into particle effect → cards animate in

### Three AI Cards - UNIQUE DESIGNS

**Prosecutor AI Card (Red Theme):**
- Background: Deep red gradient with particle effects
- Border: Thick left border with glow pulse
- Icon: ⚖️ scales tilted to one side
- Entrance: Slides from LEFT with rotation
- Content appears with typewriter effect
- Evidence bullets: Pop in one by one with scale animation

**Defense AI Card (Blue Theme):**
- Background: Deep blue gradient with floating shields
- Border: Thick left border with different pulse pattern
- Icon: 🛡️ shield with shine effect
- Entrance: Slides from RIGHT with rotation
- Counter-arguments appear with opposing slide direction

**Judge AI Card (Green/Gold Theme):**
- Background: Green-gold gradient with balance beam
- Border: Thick glowing border (all sides)
- Icon: ⚖️ perfectly balanced scales
- Entrance: Fades in from CENTER with scale effect
- Final verdict appears with dramatic glow + sound (optional)

### Debate Animation Sequence
```
1. Button clicked (0.0s)
   └── Button explodes into particles
   
2. Arena transformation (0.3s)
   └── Background darkens, spotlights appear
   
3. Prosecutor enters (0.6s)
   └── Slide + rotate from left
   └── Arguments type out with sound
   
4. Defense enters (1.2s)
   └── Slide + rotate from right
   └── Rebuttals type out
   
5. Both cards pulse/glow (1.8s)
   └── Visual tension building
   
6. Judge appears center (2.4s)
   └── Scale animation, dramatic entrance
   └── Final verdict reveals with glow
   
7. Verdict highlight (3.0s)
   └── Gold border animation around final diagnosis
   └── Confetti or particle celebration (optional)
```

### Mobile Adaptation
- Stack cards vertically
- Reduce animation complexity
- Swipeable cards for space efficiency

### API Integration
`POST /api/adversarial/debate`

---

## Feature 3: Temporal Health Trajectory

### Layout
**Full-width chart section with stat cards:**
```
Header: "6-Month Health Forecast" with subtitle
Chart Section: Large interactive line chart
Stats Row: 3 cards (Baseline, Intervention, Reduction)
Insight Panel: AI-generated insights about trajectory
```

### Chart Design (Use Recharts)
```javascript
Two animated lines:
├── Baseline (Red line)
│   ├── Dashed or solid with danger color
│   ├── Area fill with gradient opacity
│   └── Endpoint badge showing final risk %
│
└── Intervention (Green line)
    ├── Solid with success color
    ├── Area fill with green gradient
    └── Endpoint badge with success icon
```

**Chart Animations:**
- On mount: Lines draw from left to right (1.5s duration)
- Hover on line: Tooltip with detailed info
- Hover on point: Highlight + enlarged dot
- Legend: Interactive (click to show/hide lines)
- Gradient fills animate opacity on hover

**Interactive Features:**
- Zoom controls for detailed view
- Draggable time window
- Click points to see monthly details
- Toggle between risk types (cardiovascular, diabetes, etc.)

### Stat Cards Design
```
Three cards side-by-side (stacked on mobile)

Card 1: Without Intervention (Red theme)
├── Icon: ⚠️ with shake animation
├── Large percentage (animated count-up)
├── Label: "Risk at 6 months"
└── Background: Red gradient with warning pattern

Card 2: With Intervention (Green theme)
├── Icon: ✅ with checkmark animation
├── Large percentage (animated count-up)
├── Label: "With lifestyle changes"
└── Background: Green gradient with success pattern

Card 3: Risk Reduction (Purple theme)
├── Icon: 📉 with downward animation
├── Large percentage with ↓ arrow
├── Label: "Potential improvement"
└── Background: Purple gradient with celebration sparkles
```

**Stat Card Animations:**
- Entrance: Stagger from bottom (0.2s delay each)
- Number counter: Animates from 0 to value
- Icons: Subtle continuous animation (pulse/float)
- Hover: Lift effect + enhanced glow

### Insight Panel
- AI-generated text about the trajectory
- Animated text reveal (fade-in by line)
- Highlight key numbers in different color
- Expandable for more details

### API Integration
`POST /api/trajectory/forecast?diagnosis=X`

---

## Feature 4: Community Health Intelligence

### Layout
**Dashboard-style with map focus:**
```
Stats Bar (Top): 4 metric cards in a row
Alert Banner (Conditional): Warning if outbreak detected
Main Map: Full-width interactive heat map
Trending Panel (Side): Top symptoms & affected areas
```

### Stats Cards (Top Row)
```
Each card has unique design + animation:

Card 1: Total Reports
├── Icon: 📊 with chart animation
├── Large number with pulse
└── Sparkline chart showing trend

Card 2: Last 24h
├── Icon: ⏰ with clock animation
├── Number with color based on trend
└── Percentage change badge

Card 3: Transmission Velocity
├── Icon: 🚀 with speed lines
├── Percentage with animated arrow
└── Color: Green (slow) → Red (fast)

Card 4: Status Indicator
├── Icon: ⚪/🔴 with glow
├── "NORMAL" or "OUTBREAK"
└── Animated pulse if outbreak
```

### Alert Banner (If Outbreak)
```
Full-width banner above map
├── Background: Animated red gradient with pulse
├── Icon: ⚠️ animated shake
├── Message: Bold text with urgency
├── Action: "View Details" button
└── Dismissible with animation
```

### Interactive Map
**Using Leaflet.js:**

**Map Features:**
- Custom dark theme basemap
- Cluster markers for dense areas
- Color-coded markers by severity:
  - Red: High risk (severity 8-10)
  - Orange: Medium risk (4-7)
  - Yellow: Low risk (1-3)
- Animated marker appearance (pop-in effect)
- Heat map overlay (toggle-able)
- Zoom to outbreak hotspots button

**Marker Design:**
```
Custom markers (not default pins):
├── Circular pulsing dots
├── Size based on severity
├── Glow effect around high-severity
└── Cluster count badges with animation
```

**Marker Interactions:**
```
Hover:
├── Marker scales up 1.2x
├── Glow intensifies
└── Preview tooltip appears

Click:
├── Large popup modal
├── Symptom details
├── Severity visualization
├── Nearby cases count
└── "Report Similar Symptoms" CTA
```

### Trending Panel (Right Side or Bottom)
```
Trending Symptoms
├── Top 5 symptoms with bar chart
├── Each bar animates fill on load
├── Real-time update animation
└── Percentage of total shown

Affected Areas
├── List of neighborhoods/districts
├── Severity indicator badges
├── Count animations
└── Click to zoom map to area
```

### Animations
- Stats cards: Count-up animations
- Map markers: Sequential pop-in (not all at once)
- Heat map: Pulse effect on hotspots
- Alert banner: Slide down from top
- Trends: Bar chart race style animation

### API Integration
`GET /api/community/heatmap`

---

## Shared UI Components

### Navigation
```
Options:
A) Sidebar Navigation (Desktop)
   ├── Logo + app name at top
   ├── Feature links with icons
   ├── Active state: Gradient background + left border
   ├── Hover: Slide animation
   └── Collapsible on mobile

B) Top Tab Bar
   ├── Horizontal tabs
   ├── Active: Underline animation
   ├── Smooth transition between tabs
   └── Mobile: Scrollable tabs

Recommendation: Sidebar for premium feel
```

### Patient Context Panel
```
Sticky panel showing current patient:
├── Avatar or initials badge
├── Patient ID
├── Key info (age, gender)
├── Quick stats
└── "Change Patient" button
```

### Loading States
```
Skeleton Screens:
├── Shimmer animation (left to right)
├── Mimic actual content layout
├── Smooth fade to real content
└── Different skeleton for each section

Spinners:
├── Custom animated logo spinner
├── Progress rings with percentage
├── Particle loaders for special actions
```

### Toast Notifications
```
Success, error, warning, info types:
├── Slide in from top-right
├── Icon animation (checkmark, X, etc.)
├── Auto-dismiss after 5s
├── Progress bar showing time remaining
└── Swipeable to dismiss
```

### Modals
```
├── Backdrop blur effect
├── Modal scales in from center
├── Close button with hover rotation
├── Smooth exit animation
└── Keyboard accessible (ESC to close)
```

---

## Landing Page Design

### Hero Section
```
Full viewport height:
├── Animated gradient mesh background
├── Floating 3D medical icons (subtle)
├── Large headline with gradient text
│   └── "Predict. Prevent. Protect."
├── Subheadline with typewriter animation
├── Dual CTA buttons:
│   ├── "Launch App" (primary, gradient)
│   └── "Watch Demo" (secondary, outlined)
└── Scroll indicator (animated bounce)
```

### Features Showcase
```
4 Cards (2x2 grid on desktop, stack on mobile):

Each card:
├── Icon with continuous subtle animation
├── Feature title with gradient on hover
├── Brief description (2-3 lines)
├── "Learn More" link
└── Hover effect: Lift + shadow + border glow

Special hover: Card background video preview (optional)
```

### How It Works
```
Timeline/Step visualization:
├── 3-4 steps connected by line
├── Scroll animation: Steps appear as you scroll
├── Icons animate in on view
└── Mobile: Vertical timeline
```

### Impact Statistics
```
Numbers with animated counters:
├── "X% accuracy improvement"
├── "Y outbreak detected early"
├── "Z patients helped"
└── Appear as user scrolls into view
```

### Footer
```
Multi-column footer:
├── Brand + tagline
├── Quick links
├── Social media icons
├── Copyright + legal
└── Scroll-to-top button (appears on scroll)
```

---

## Animation Library & Effects

### Framer Motion Animations to Use

**Page transitions:**
```javascript
pageVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 }
}
transition = { duration: 0.4, ease: "easeOut" }
```

**Stagger children:**
```javascript
containerVariants = {
  hidden: {},
  visible: {
    transition: {
      staggerChildren: 0.1
    }
  }
}
```

**Card hover:**
```javascript
cardVariants = {
  rest: { scale: 1, boxShadow: "0 10px 30px rgba(0,0,0,0.1)" },
  hover: { 
    scale: 1.02, 
    boxShadow: "0 20px 60px rgba(102,126,234,0.3)",
    y: -5
  }
}
```

**Number counter:**
```javascript
Use framer-motion's useSpring + useTransform for smooth counting
```

**Entrance animations:**
```javascript
fadeInUp, fadeInLeft, fadeInRight, scaleIn, etc.
```

### CSS Animations
```css
/* Gradient animation for backgrounds */
@keyframes gradientShift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

/* Pulse effect for important elements */
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.8; }
}

/* Shimmer for loading states */
@keyframes shimmer {
  0% { background-position: -1000px 0; }
  100% { background-position: 1000px 0; }
}
```

---

## Responsive Design Breakpoints

```
Mobile: < 640px
├── Single column layout
├── Stack all cards
├── Simplified animations
├── Collapsible navigation
└── Touch-optimized interactions

Tablet: 640px - 1024px
├── Two column where appropriate
├── Medium complexity animations
└── Sidebar can collapse

Desktop: > 1024px
├── Full layout with sidebar
├── All animations enabled
├── Hover effects prominent
└── Max content width: 1400px
```

---

## Performance Optimizations

✅ **Code splitting**: Lazy load feature pages  
✅ **Image optimization**: Next.js Image component  
✅ **Animation optimization**: Use `transform` and `opacity` only  
✅ **Debounce**: API calls on form inputs  
✅ **Memoization**: React.memo for expensive components  
✅ **Virtual scrolling**: For long lists  
✅ **Reduce bundle size**: Tree shaking, dynamic imports  

---

## Accessibility (A11y)

✅ **Keyboard navigation**: Tab through all interactive elements  
✅ **ARIA labels**: Proper labels for screen readers  
✅ **Color contrast**: WCAG AA compliance  
✅ **Focus indicators**: Visible focus states  
✅ **Alt text**: All images have descriptions  
✅ **Semantic HTML**: Proper heading hierarchy  
✅ **Skip links**: Skip to main content  

---

## API Integration Pattern

### Setup Axios/Fetch wrapper:
```typescript
const API_BASE = 'http://localhost:8000/api';

// Centralized API service
class NeuroVitalsAPI {
  async analyzeSymptoms(data: PatientData) {
    return await fetch(`${API_BASE}/diagnosis/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(res => res.json());
  }
  
  // ... other methods
}
```

### Error handling:
```typescript
try {
  setLoading(true);
  const result = await api.analyzeSymptoms(data);
  setResult(result);
  toast.success('Analysis complete!');
} catch (error) {
  toast.error('Analysis failed. Please try again.');
  console.error(error);
} finally {
  setLoading(false);
}
```

---

## Development Checklist

### Phase 1: Setup
- [ ] Initialize Next.js 14 project with TypeScript
- [ ] Install dependencies (Tailwind, Framer Motion, Recharts, Leaflet)
- [ ] Setup shadcn/ui component library
- [ ] Configure Tailwind with custom theme
- [ ] Create folder structure

### Phase 2: Core Components
- [ ] Navigation component (sidebar/tabs)
- [ ] Layout wrapper component
- [ ] Card component with hover effects
- [ ] Button component with loading states
- [ ] Input components with floating labels
- [ ] Toast notification system
- [ ] Modal component

### Phase 3: Landing Page
- [ ] Hero section with animations
- [ ] Features showcase grid
- [ ] How it works timeline
- [ ] Statistics counter section
- [ ] Footer

### Phase 4: Feature Pages
- [ ] Symptom Analysis page
- [ ] Adversarial Diagnosis page (most complex)
- [ ] Health Trajectory page
- [ ] Community Health page

### Phase 5: Polish
- [ ] All animations implemented
- [ ] Mobile responsive
- [ ] Dark mode (optional)
- [ ] Loading states everywhere
- [ ] Error boundaries
- [ ] SEO optimization

### Phase 6: Testing
- [ ] Test all features
- [ ] Cross-browser testing
- [ ] Mobile testing
- [ ] Performance audit (Lighthouse)
- [ ] Accessibility audit

---

## File Structure

```
neuro-vitals-frontend/
├── app/
│   ├── page.tsx (landing)
│   ├── layout.tsx
│   ├── app/
│   │   ├── layout.tsx (app shell)
│   │   ├── symptom-analysis/page.tsx
│   │   ├── adversarial-diagnosis/page.tsx
│   │   ├── health-trajectory/page.tsx
│   │   └── community-health/page.tsx
├── components/
│   ├── ui/ (shadcn components)
│   ├── features/
│   │   ├── SymptomForm.tsx
│   │   ├── AdversarialArena.tsx
│   │   ├── TrajectoryChart.tsx
│   │   └── CommunityMap.tsx
│   ├── shared/
│   │   ├── Navigation.tsx
│   │   ├── LoadingStates.tsx
│   │   └── Toast.tsx
│   └── landing/
│       ├── Hero.tsx
│       ├── Features.tsx
│       └── Footer.tsx
├── lib/
│   ├── api.ts
│   ├── types.ts
│   └── utils.ts
├── public/
│   └── images/
└── styles/
    └── globals.css
```

---

## Color Palette

```css
/* Primary Brand Colors */
--primary-purple: #667eea;
--primary-dark-purple: #764ba2;
--primary-blue: #3b82f6;
--primary-green: #10b981;
--primary-red: #ef4444;

/* Semantic Colors */
--success: #10b981;
--warning: #f59e0b;
--error: #ef4444;
--info: #3b82f6;

/* Neutrals */
--gray-50: #f9fafb;
--gray-100: #f3f4f6;
--gray-800: #1f2937;
--gray-900: #111827;

/* Gradients */
--gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--gradient-success: linear-gradient(135deg, #10b981 0%, #059669 100%);
--gradient-danger: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
```

---

## Success Criteria

Your implementation is successful when:

✅ **Visual Excellence**: Judges say "WOW!" at first glance  
✅ **Smooth Performance**: All animations 60fps, no jank  
✅ **Complete Functionality**: All 4 features work flawlessly  
✅ **Mobile Perfect**: Excellent experience on all devices  
✅ **Professional**: Feels like a $100K+ production app  
✅ **Trust Factor**: Medical professionals would use it  
✅ **Innovation Visible**: Adversarial AI feature is stunning  
✅ **Data Clarity**: Charts and maps are instantly understandable  

---

**Build this and win first prize! Make every pixel perfect, every animation smooth, and every interaction delightful. This should be the most impressive healthcare AI interface the judges have ever seen! 🏆🚀**
