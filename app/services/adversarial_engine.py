import os
import json
import logging
from typing import Dict, Any, List
from app.config import settings

logger = logging.getLogger(__name__)

class AdversarialEngine:
    """Adversarial diagnosis system using Multi-Agent Debate"""
    
    def __init__(self):
        self._model = None

    def _get_model(self):
        if self._model is not None:
            return self._model

        # Strategy 1: Google AI SDK (Gemini)
        if settings.GOOGLE_API_KEY:
            try:
                import google.generativeai as genai
                genai.configure(api_key=settings.GOOGLE_API_KEY)
                self._model = genai.GenerativeModel("gemini-flash-lite-latest")
                logger.info("Adversarial LLM initialized with Google AI SDK.")
                return self._model
            except Exception as e:
                logger.error("Failed to init Google AI: %s", e)

        # Strategy 2: GitHub Models (OpenAI-Compatible SDK)
        if settings.GITHUB_TOKEN:
            try:
                from openai import OpenAI
                client = OpenAI(
                    base_url="https://models.inference.ai.azure.com",
                    api_key=settings.GITHUB_TOKEN
                )
                class GitHubGeminiWrapper:
                    def __init__(self, client):
                        self.client = client
                    def generate_content(self, prompt):
                        response = self.client.chat.completions.create(
                            model="gpt-4o",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.1,
                            response_format={"type": "json_object"}
                        )
                        class ResponseWrapper:
                            def __init__(self, text):
                                self.text = text
                        return ResponseWrapper(response.choices[0].message.content)

                self._model = GitHubGeminiWrapper(client)
                logger.info("Adversarial LLM initialized with GitHub Models.")
                return self._model
            except Exception as e:
                logger.error("Failed to init GitHub Models: %s", e)

        logger.warning("No AI provider configured. Using Mock fallback.")
        return None

    def prosecutor_ai(self, patient_data: dict) -> Dict[str, Any]:
        """Argues FOR the most likely diagnosis"""
        model = self._get_model()
        
        symptoms_list = patient_data.get('symptoms', [])
        symptoms_desc = ", ".join([f"{s.get('description', 'Unknown')} (severity {s.get('severity', 5)})" for s in symptoms_list])
        
        if not model:
            return {
                "diagnosis": "Acute Viral Infection",
                "confidence": 0.85,
                "supporting_evidence": [
                    "High fever consistent with viral infection pattern",
                    "Timeline of 2-3 days matches typical viral onset",
                    "Age group commonly affected by seasonal viruses"
                ],
                "rebuttals_to_alternatives": [
                    "Bacterial infection unlikely due to absence of localized symptoms",
                    "Chronic condition ruled out by acute onset"
                ]
            }
        
        prompt = f"""You are the PROSECUTOR AI in a medical debate.
Your job: Argue STRONGLY for the most likely diagnosis based on symptoms.

Patient: {patient_data.get('age')}yo {patient_data.get('gender')}
Symptoms: {symptoms_desc}
Medical history: {', '.join(patient_data.get('medical_history', []))}

Respond in JSON ONLY:
{{
    "diagnosis": "...",
    "confidence": 0.0-1.0,
    "supporting_evidence": ["Evidence 1", "Evidence 2", "Evidence 3"],
    "rebuttals_to_alternatives": ["Why X is wrong", "Why Y is wrong"]
}}
"""
        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)
        except Exception as e:
            logger.error("Prosecutor AI Error: %s", e)
            return {"diagnosis": "Error in Analysis", "confidence": 0, "supporting_evidence": [str(e)], "rebuttals_to_alternatives": []}

    def defense_ai(self, patient_data: dict, prosecutor_diagnosis: str) -> Dict[str, Any]:
        """Searches for contradictions and alternatives"""
        model = self._get_model()
        
        symptoms_list = patient_data.get('symptoms', [])
        symptoms_desc = ", ".join([f"{s.get('description', 'Unknown')} (severity {s.get('severity', 5)})" for s in symptoms_list])
        
        if not model:
            return {
                "alternative_diagnosis": "Allergic Reaction",
                "confidence": 0.68,
                "contradictory_evidence": [
                    "Fever pattern inconsistent with typical viral progression",
                    "Patient reports environmental triggers",
                    "Rapid onset more consistent with allergic response"
                ],
                "why_more_likely": "Environmental exposure combined with timing suggests allergic etiology."
            }
        
        prompt = f"""You are the DEFENSE AI in a medical debate.
The Prosecutor claims: "{prosecutor_diagnosis}"

Your job: Find CONTRADICTIONS and propose ALTERNATIVE diagnoses.

Patient: {patient_data.get('age')}yo {patient_data.get('gender')}
Symptoms: {symptoms_desc}

Respond in JSON ONLY:
{{
    "alternative_diagnosis": "...",
    "confidence": 0.0-1.0,
    "contradictory_evidence": ["Contradiction 1", "Contradiction 2"],
    "why_more_likely": "..."
}}
"""
        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)
        except Exception as e:
            logger.error("Defense AI Error: %s", e)
            return {"alternative_diagnosis": "Error in Analysis", "confidence": 0, "contradictory_evidence": [str(e)], "why_more_likely": ""}

    def judge_ai(self, patient_data: dict, prosecutor_result: dict, defense_result: dict) -> Dict[str, Any]:
        """Synthesizes both arguments"""
        model = self._get_model()
        
        if not model:
            return {
                "final_diagnosis": "Likely Viral Infection with possible allergic component",
                "confidence": 0.78,
                "synthesis": "The primary evidence supports a viral infection, but environmental triggers raised by defense are plausible.",
                "recommended_tests": ["CBC Test", "Allergy Panel"],
                "debate_summary": "Prosecutor argued viral pattern; Defense argued environmental triggers."
            }
        
        prompt = f"""You are the JUDGE AI in a medical debate.

PROSECUTOR argues: {prosecutor_result.get('diagnosis')} (Confidence: {prosecutor_result.get('confidence')})
Evidence: {prosecutor_result.get('supporting_evidence')}

DEFENSE argues: {defense_result.get('alternative_diagnosis')} (Confidence: {defense_result.get('confidence')})
Contradictions: {defense_result.get('contradictory_evidence')}

Synthesize and provide FINAL VERDICT.

Respond in JSON ONLY:
{{
    "final_diagnosis": "...",
    "confidence": 0.0-1.0,
    "synthesis": "...",
    "recommended_tests": ["Test 1", "Test 2"],
    "debate_summary": "..."
}}
"""
        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)
        except Exception as e:
            logger.error("Judge AI Error: %s", e)
            return {"final_diagnosis": "Error", "confidence": 0, "synthesis": str(e), "recommended_tests": [], "debate_summary": ""}

    def run_debate(self, patient_data: dict) -> Dict[str, Any]:
        """Run full adversarial debate"""
        prosecutor = self.prosecutor_ai(patient_data)
        defense = self.defense_ai(patient_data, prosecutor.get("diagnosis", "Unknown"))
        verdict = self.judge_ai(patient_data, prosecutor, defense)
        
        return {
            "prosecutor": prosecutor,
            "defense": defense,
            "verdict": verdict
        }

adversarial_engine = AdversarialEngine()
