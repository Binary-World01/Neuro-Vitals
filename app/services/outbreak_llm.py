"""
Outbreak LLM Service – uses Google Gemini Flash to run
symptom analysis with optional image support.

Migrated from hackathon_project1/llm_service.py.
Uses GOOGLE_API_KEY from app.config.
"""

import logging
from app.config import settings

logger = logging.getLogger(__name__)

# Lazy-load the Gemini model (only on first call)
_model = None


def _get_model():
    global _model
    if _model is not None:
        return _model

    # Strategy 1: Google AI SDK (Gemini)
    if settings.GOOGLE_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=settings.GOOGLE_API_KEY)
            _model = genai.GenerativeModel("gemini-flash-lite-latest")
            logger.info("Outbreak LLM initialized with Google AI SDK.")
            return _model
        except ImportError:
            logger.warning("google-generativeai not installed, falling back...")
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
            # We'll wrap the OpenAI client to mimic the GenerativeModel.generate_content interface
            class GitHubGeminiWrapper:
                def __init__(self, client):
                    self.client = client
                def generate_content(self, content):
                    # For simplicity, extract just the prompt text (content[0])
                    # and ignore image data for the GitHub Models fallback unless using gpt-4o
                    prompt = content[0] if isinstance(content, list) else content
                    # If image is present, we should use a multimodal model
                    model_name = "gpt-4o" # GitHub Models Gemini equivalent or gpt-4o
                    
                    messages = [{"role": "user", "content": prompt}]
                    # If multimodal (GitHub models supports gpt-4o)
                    if isinstance(content, list) and len(content) > 1:
                        # Re-format for OpenAI Multimodal if needed
                        pass 

                    response = self.client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        temperature=0.1
                    )
                    
                    class ResponseWrapper:
                        def __init__(self, text):
                            self.text = text
                    return ResponseWrapper(response.choices[0].message.content)

            _model = GitHubGeminiWrapper(client)
            logger.info("Outbreak LLM initialized with GitHub Models (OpenAI SDK).")
            return _model
        except Exception as e:
            logger.error("Failed to init GitHub Models: %s", e)

    # Strategy 3: Error
    raise Exception("No AI provider configured (Missing GOOGLE_API_KEY and GITHUB_TOKEN)")


def analyze_symptoms_with_gemini(data: dict, image_file=None) -> dict:
    """
    Analyse patient symptoms (and optional image) with Gemini Flash.

    Parameters
    ----------
    data : dict  – must contain name, age, gender, symptoms, severity, duration
    image_file   – optional FastAPI UploadFile

    Returns
    -------
    dict  {"analysis": "<AI text>"}
    """
    try:
        prompt = f"""
        You are an AI Medical Assistant. Analyze the following patient data and the provided image (if any).

        Patient Name: {data['name']}
        Age: {data['age']}, Gender: {data['gender']}
        Symptoms: {data['symptoms']}
        Severity: {data['severity']}/10, Duration: {data['duration']} days

        Instructions:
        - If an image is provided, look for visible signs (rashes, swelling, discoloration, etc.) that match the symptoms.
        - Provide a possible condition and a simple explanation.
        - Give clear next steps.
        - DISCLAIMER: State that this is an AI analysis and not a final medical diagnosis.

        Format your response as:
        POSSIBLE CONDITION: [name of condition]
        EXPLANATION: [simple explanation]
        NEXT STEPS: [recommendations]
        DISCLAIMER: This is an AI analysis and not a medical diagnosis.
        """

        content: list = [prompt]

        # Handle optional image
        if image_file and getattr(image_file, "filename", None):
            image_file.file.seek(0)
            image_data = image_file.file.read()

            filename = image_file.filename.lower()
            mime_type = getattr(image_file, "content_type", None) or "image/jpeg"

            if mime_type == "application/octet-stream" or not mime_type:
                ext_map = {
                    ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                    ".png": "image/png", ".gif": "image/gif",
                    ".webp": "image/webp", ".bmp": "image/bmp",
                }
                for ext, mt in ext_map.items():
                    if filename.endswith(ext):
                        mime_type = mt
                        break

            if mime_type.startswith("image/"):
                content.append({"mime_type": mime_type, "data": image_data})
                logger.info("Image attached (%s, %d bytes)", mime_type, len(image_data))

        model = _get_model()
        response = model.generate_content(content)
        return {"analysis": response.text}

    except Exception as exc:
        logger.error("Outbreak LLM error: %s", exc)
        return {"analysis": f"AI service error. Please try again. Error: {exc}"}
