"""
Adversarial Diagnosis Engine - Two AIs debate, one judges
"""
import os
import json
from typing import Dict, Any


class AdversarialEngine:
    """Adversarial diagnosis system"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.use_mock = not self.api_key
        
        if not self.use_mock:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                self.use_mock = True
    
    def prosecutor_ai(self, patient_data: dict) -> Dict[str, Any]:
        """Argues FOR the most likely diagnosis"""
        
        if self.use_mock:
            return {
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
            }
        
        symptoms_desc = ", ".join([f"{s['description']} (severity {s['severity']})" for s in patient_data.get('symptoms', [])])
        
        prompt = f"""You are the PROSECUTOR AI in a medical debate.
Your job: Argue STRONGLY for the most likely diagnosis based on symptoms.

Patient: {patient_data.get('age')}yo {patient_data.get('gender')}
Symptoms: {symptoms_desc}
Medical history: {', '.join(patient_data.get('medical_history', []))}

Provide:
1. Your diagnosis
2. Confidence (0-1)
3. 3-5 pieces of SUPPORTING evidence
4. Why alternative diagnoses are LESS likely

Respond in JSON:
{{
    "diagnosis": "...",
    "confidence": 0.0-1.0,
    "supporting_evidence": ["...", "..."],
    "rebuttals_to_alternatives": ["...", "..."]
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an aggressive prosecutor AI. Find evidence for the PRIMARY diagnosis."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Prosecutor AI Error: {e}")
            return self.prosecutor_ai(patient_data)  # Use mock
    
    def defense_ai(self, patient_data: dict, prosecutor_diagnosis: str) -> Dict[str, Any]:
        """Searches for contradictions and alternatives"""
        
        if self.use_mock:
            return {
                "alternative_diagnosis": "Allergic Reaction",
                "confidence": 0.68,
                "contradictory_evidence": [
                    "Fever pattern inconsistent with typical viral progression",
                    "Patient reports environmental triggers (potential allergens)",
                    "Rapid onset more consistent with allergic response",
                    "Absence of typical viral prodrome symptoms"
                ],
                "why_more_likely": "Environmental exposure combined with symptom onset timing suggests allergic etiology over viral infection"
            }
        
        symptoms_desc = ", ".join([f"{s['description']} (severity {s['severity']})" for s in patient_data.get('symptoms', [])])
        
        prompt = f"""You are the DEFENSE AI in a medical debate.
The Prosecutor claims: "{prosecutor_diagnosis}"

Your job: Find CONTRADICTIONS and propose ALTERNATIVE diagnoses.

Patient: {patient_data.get('age')}yo {patient_data.get('gender')}
Symptoms: {symptoms_desc}

Provide:
1. Your alternative diagnosis
2. Confidence (0-1)
3. 3-5 pieces of CONTRADICTORY evidence against prosecutor
4. Why your diagnosis is MORE likely

Respond in JSON:
{{
    "alternative_diagnosis": "...",
    "confidence": 0.0-1.0,
    "contradictory_evidence": ["...", "..."],
    "why_more_likely": "..."
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a defense AI. Find contradictions and alternatives."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Defense AI Error: {e}")
            return self.defense_ai(patient_data, prosecutor_diagnosis)
    
    def judge_ai(self, patient_data: dict, prosecutor_result: dict, defense_result: dict) -> Dict[str, Any]:
        """Synthesizes both arguments"""
        
        if self.use_mock:
            return {
                "final_diagnosis": "Likely Viral Infection with possible allergic component",
                "confidence": 0.78,
                "synthesis": "After reviewing both arguments, the primary evidence supports a viral infection as the most likely cause. However, the defense raises valid points about environmental triggers that warrant consideration. The truth likely lies in a viral infection exacerbated by allergic inflammation.",
                "recommended_tests": [
                    "Complete Blood Count (CBC) to differentiate viral vs bacterial",
                    "Allergy panel if symptoms persist",
                    "Chest X-ray if respiratory symptoms worsen"
                ],
                "debate_summary": "Prosecutor presented strong evidence for viral infection based on symptom timeline and pattern. Defense effectively challenged this with environmental exposure data. Final verdict synthesizes both perspectives."
            }
        
        prompt = f"""You are the JUDGE AI in a medical debate.

PROSECUTOR argues: {prosecutor_result['diagnosis']} (Confidence: {prosecutor_result['confidence']})
Evidence: {prosecutor_result['supporting_evidence']}

DEFENSE argues: {defense_result['alternative_diagnosis']} (Confidence: {defense_result['confidence']})
Contradictions: {defense_result['contradictory_evidence']}

Provide your FINAL VERDICT:
1. Final diagnosis (can be prosecutor's, defense's, or a third option)
2. Confidence (0-1)
3. Synthesis of both arguments
4. Next steps (tests to rule out alternatives)

Respond in JSON:
{{
    "final_diagnosis": "...",
    "confidence": 0.0-1.0,
    "synthesis": "...",
    "recommended_tests": ["...", "..."],
    "debate_summary": "..."
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an impartial judge. Synthesize both arguments."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Judge AI Error: {e}")
            return self.judge_ai(patient_data, prosecutor_result, defense_result)
    
    def run_debate(self, patient_data: dict) -> Dict[str, Any]:
        """Run full adversarial debate"""
        # Step 1: Prosecutor argues
        prosecutor = self.prosecutor_ai(patient_data)
        
        # Step 2: Defense counters
        defense = self.defense_ai(patient_data, prosecutor["diagnosis"])
        
        # Step 3: Judge synthesizes
        verdict = self.judge_ai(patient_data, prosecutor, defense)
        
        return {
            "prosecutor": prosecutor,
            "defense": defense,
            "verdict": verdict
        }


adversarial_engine = AdversarialEngine()
