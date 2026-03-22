# API Reference - Complete Endpoints Documentation

**Base URL**: `http://localhost:8000/api`

---

## Endpoint 1: Symptom Analysis

### `POST /api/diagnosis/analyze`

**Purpose**: Analyze patient symptoms and provide AI diagnosis with explainable reasoning.

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "patient_id": "string (required)",
  "age": "integer (required, 0-120)",
  "gender": "string (required, one of: male, female, other)",
  "symptoms": [
    {
      "description": "string (required, e.g., 'chest pain')",
      "severity": "integer (required, 1-10)",
      "duration_days": "integer (required, >= 0)",
      "onset_time": "string (optional, one of: morning, afternoon, evening, night)"
    }
  ],
  "medical_history": ["string (optional, array of conditions)"],
  "current_medications": ["string (optional, array of medications)"]
}
```

**Example Request:**
```json
{
  "patient_id": "DEMO-001",
  "age": 35,
  "gender": "male",
  "symptoms": [
    {
      "description": "chest pain",
      "severity": 8,
      "duration_days": 2,
      "onset_time": "morning"
    }
  ],
  "medical_history": ["high blood pressure", "diabetes"],
  "current_medications": ["lisinopril"]
}
```

**Response (200 OK):**
```json
{
  "primary_diagnosis": "Possible Chest Pain-related condition",
  "confidence": 0.75,
  "reasoning": [
    "Patient presents with chest pain at severity 8/10",
    "Duration of 2 days suggests acute condition",
    "Age and medical history considered",
    "Differential diagnoses ruled out based on symptom pattern"
  ],
  "recommendations": [
    "Monitor symptoms for next 24-48 hours",
    "Stay hydrated and get adequate rest",
    "Consult healthcare provider if symptoms worsen",
    "Consider over-the-counter symptom relief if appropriate"
  ],
  "timestamp": "2026-02-15T22:30:00.000000"
}
```

**Error Response (422 Validation Error):**
```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "detail": "Analysis failed: [error message]"
}
```

---

## Endpoint 2: Adversarial Diagnosis

### `POST /api/adversarial/debate`

**Purpose**: Run a three-AI debate system where Prosecutor argues FOR a diagnosis, Defense argues AGAINST, and Judge synthesizes the final verdict.

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
Same structure as `/api/diagnosis/analyze`

**Example Request:**
```json
{
  "patient_id": "DEMO-001",
  "age": 45,
  "gender": "male",
  "symptoms": [
    {
      "description": "chest pain",
      "severity": 8,
      "duration_days": 2
    }
  ],
  "medical_history": ["high blood pressure"],
  "current_medications": ["lisinopril"]
}
```

**Response (200 OK):**
```json
{
  "prosecutor": {
    "diagnosis": "Acute Viral Infection",
    "confidence": 0.85,
    "supporting_evidence": [
      "High fever consistent with viral infection pattern",
      "Timeline of 2-3 days matches typical viral onset",
      "Age group commonly affected by seasonal viruses",
      "Symptom combination highly specific to viral etiology"
    ],
    "rebuttals_to_alternatives": [
      "Bacterial infection unlikely due to absence of localized symptoms",
      "Chronic condition ruled out by acute onset"
    ]
  },
  "defense": {
    "alternative_diagnosis": "Allergic Reaction",
    "confidence": 0.68,
    "contradictory_evidence": [
      "Fever pattern inconsistent with typical viral progression",
      "Patient reports environmental triggers (potential allergens)",
      "Rapid onset more consistent with allergic response",
      "Absence of typical viral prodrome symptoms"
    ],
    "why_more_likely": "Environmental exposure combined with symptom onset timing suggests allergic etiology over viral infection"
  },
  "verdict": {
    "final_diagnosis": "Likely Viral Infection with possible allergic component",
    "confidence": 0.78,
    "synthesis": "After reviewing both arguments, the primary evidence supports a viral infection as the most likely cause. However, the defense raises valid points about environmental triggers that warrant consideration...",
    "recommended_tests": [
      "Complete Blood Count (CBC) to differentiate viral vs bacterial",
      "Allergy panel if symptoms persist",
      "Chest X-ray if respiratory symptoms worsen"
    ],
    "debate_summary": "Prosecutor presented strong evidence for viral infection based on symptom timeline and pattern. Defense effectively challenged this with environmental exposure data..."
  },
  "timestamp": "2026-02-15T22:30:00.000000"
}
```

---

## Endpoint 3: Health Trajectory Forecast

### `POST /api/trajectory/forecast?diagnosis={diagnosis_name}`

**Purpose**: Calculate 6-month health risk trajectory with baseline (no intervention) vs intervention scenarios.

**Query Parameters:**
- `diagnosis` (optional, string): Diagnosis name (default: "General Health Risk")

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
Same structure as `/api/diagnosis/analyze`

**Example Request:**
```
POST /api/trajectory/forecast?diagnosis=Cardiovascular Risk

Body:
{
  "patient_id": "DEMO-001",
  "age": 45,
  "gender": "male",
  "symptoms": [
    {
      "description": "chest pain",
      "severity": 7,
      "duration_days": 3
    }
  ],
  "medical_history": ["hypertension", "diabetes"]
}
```

**Response (200 OK):**
```json
{
  "current_risk": 0.45,
  "baseline_projection": {
    "month_1": 0.50,
    "month_2": 0.55,
    "month_3": 0.63,
    "month_4": 0.73,
    "month_5": 0.85,
    "month_6": 0.98
  },
  "intervention_projection": {
    "month_1": 0.43,
    "month_2": 0.37,
    "month_3": 0.30,
    "month_4": 0.23,
    "month_5": 0.15,
    "month_6": 0.05
  },
  "diagnosis": "Cardiovascular Risk",
  "key_interventions": [
    "Lifestyle modification (diet and exercise)",
    "Medication adherence as prescribed",
    "Regular health monitoring and check-ups",
    "Stress management techniques",
    "Sleep hygiene improvement"
  ],
  "risk_reduction": 93.0
}
```

**Field Explanations:**
- `current_risk`: Float (0-1) representing current health risk level
- `baseline_projection`: Object with monthly risk values WITHOUT intervention
- `intervention_projection`: Object with monthly risk values WITH intervention
- `risk_reduction`: Percentage improvement (baseline month_6 - intervention month_6)

---

## Endpoint 4: Community Health Intelligence

### `GET /api/community/heatmap`

**Purpose**: Get community health data including outbreak detection, symptom trends, and geographic distribution.

**Request Headers:** None required

**Query Parameters:** None

**Example Request:**
```
GET /api/community/heatmap
```

**Response (200 OK):**
```json
{
  "total_reports": 482,
  "recent_24h": 247,
  "transmission_velocity": 34.2,
  "trending_symptoms": [
    {
      "symptom": "fever",
      "count": 198
    },
    {
      "symptom": "cough",
      "count": 156
    },
    {
      "symptom": "headache",
      "count": 143
    },
    {
      "symptom": "fatigue",
      "count": 128
    },
    {
      "symptom": "sore throat",
      "count": 95
    }
  ],
  "area_data": [
    {
      "area": "Andheri West",
      "count": 145,
      "severity": "high"
    },
    {
      "area": "Bandra East",
      "count": 89,
      "severity": "medium"
    },
    {
      "area": "Powai",
      "count": 67,
      "severity": "medium"
    },
    {
      "area": "Dadar",
      "count": 54,
      "severity": "low"
    }
  ],
  "map_points": [
    {
      "lat": 19.1136,
      "lon": 72.8697,
      "severity": 8,
      "symptoms": ["fever", "cough", "headache"]
    },
    {
      "lat": 19.0596,
      "lon": 72.8295,
      "severity": 6,
      "symptoms": ["fever", "fatigue"]
    },
    {
      "lat": 19.0178,
      "lon": 72.8478,
      "severity": 4,
      "symptoms": ["headache", "sore throat"]
    }
    // ... more points (typically 200-500 points)
  ],
  "outbreak_detected": true,
  "alert_message": "⚠️ Outbreak Alert: Transmission velocity increased by 34.2% in last 24 hours"
}
```

**Field Explanations:**
- `total_reports`: Total symptom reports in last 48 hours
- `recent_24h`: Reports in last 24 hours specifically
- `transmission_velocity`: Percentage change (last 24h vs previous 24h)
- `trending_symptoms`: Top 5 most reported symptoms with counts
- `area_data`: Aggregated data by geographic area
  - `severity`: "high" (>100 reports), "medium" (50-100), "low" (<50)
- `map_points`: Individual report locations for mapping
  - `lat/lon`: Coordinates for marker placement
  - `severity`: 1-10 scale (determines marker color)
  - `symptoms`: Array of symptoms for popup
- `outbreak_detected`: Boolean (true if velocity > 20%)
- `alert_message`: String alert message (null if no outbreak)

---

## Health Check Endpoints

### `GET /`
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Neuro-Vitals API",
  "version": "1.0.0",
  "docs": "/docs",
  "endpoints": {
    "diagnosis": "/api/diagnosis/analyze",
    "adversarial": "/api/adversarial/debate",
    "trajectory": "/api/trajectory/forecast",
    "community": "/api/community/heatmap"
  }
}
```

### `GET /health`
Simple health check.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## Interactive API Documentation

**Swagger UI**: Available at `http://localhost:8000/docs`
- Interactive API testing
- Try out endpoints directly
- View all schemas
- See example requests/responses

**ReDoc**: Available at `http://localhost:8000/redoc`
- Alternative documentation view
- Better for reading/reference
- More detailed descriptions

---

## Error Handling

All endpoints follow standard HTTP status codes:

**200 OK**: Successful request
**422 Unprocessable Entity**: Validation error (malformed request)
**500 Internal Server Error**: Server-side error

**Common Validation Errors:**
```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Frontend Error Handling Pattern:**
```javascript
try {
  const response = await fetch(url, options);
  
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Request failed');
  }
  
  return await response.json();
} catch (error) {
  console.error('API Error:', error);
  // Show user-friendly error message
}
```

---

## Rate Limiting

**Current**: No rate limiting (development mode)
**Production**: Consider implementing rate limiting for security

---

## CORS Configuration

**Current**: Allow all origins (`*`)
**Production**: Restrict to specific frontend domains

---

## Authentication

**Current**: None (open API for hackathon demo)
**Future**: Consider JWT tokens or API keys for production

---

## Mock Mode

The backend API can run in "mock mode" without OpenAI API keys:

**Environment Variable:**
```env
MODEL_PROVIDER=mock
```

**Behavior:**
- All endpoints work
- Returns realistic but pre-generated responses
- No external API calls
- Perfect for testing/demo

---

## Testing Examples

### cURL Examples

**Symptom Analysis:**
```bash
curl -X POST http://localhost:8000/api/diagnosis/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "TEST-001",
    "age": 35,
    "gender": "male",
    "symptoms": [{
      "description": "fever",
      "severity": 7,
      "duration_days": 3
    }]
  }'
```

**Community Health:**
```bash
curl http://localhost:8000/api/community/heatmap
```

### JavaScript Fetch Examples

**Diagnosis:**
```javascript
const analyzeSymptoms = async (patientData) => {
  const response = await fetch('http://localhost:8000/api/diagnosis/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(patientData)
  });
  return await response.json();
};
```

**Community Health:**
```javascript
const getCommunityData = async () => {
  const response = await fetch('http://localhost:8000/api/community/heatmap');
  return await response.json();
};
```

---

**END OF API REFERENCE**
