
const API_KEY = "AIzaSyDkwQhCgRZnCcVvGz0zRgcUMTSGFNfMvA8";
const URL = `https://generativelanguage.googleapis.com/v1beta/models?key=${API_KEY}`;

async function listModels() {
    try {
        const response = await fetch(URL);
        const data = await response.json();

        if (data.models) {
            console.log("Available Models:");
            data.models.forEach(model => {
                if (model.supportedGenerationMethods && model.supportedGenerationMethods.includes("generateContent")) {
                    console.log(`- ${model.name}`);
                }
            });
        } else {
            console.log("No models found or error:", data);
        }
    } catch (error) {
        console.error("Error fetching models:", error);
    }
}

listModels();
