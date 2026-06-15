EXTRACTION_MODEL = "qwen2.5:7b"
GENERATOR_MODEL = "llama3.1:8b"


#ollama model deployment, allows for parameters finetuning and setting standarad values
#low temperatures make the models strict and less creative and vice versa
#setting keep_alive to 0, removes the model after use from local envrinoment
def ollama_chat(
    model: str,
    system: str,
    user: str,
    images=None,
    format: str = "",
    keep_alive: str = "4m",
    temperature: float = 0.0,
    max_tokens: int = 2048,
    num_ctx: int = 8192,
) -> str:
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "keep_alive": keep_alive,  # Keeps model in GPU for 5 mins for faster back-to-back calls
        "options": {  # Correct place for parameters
            "temperature": temperature,
            "num_predict": max_tokens,
            "num_ctx": num_ctx,
        },
    }

    if format:
        payload["format"] = format

    if images and isinstance(images, list) and len(images) > 0:
        encoded_images = []
        for img_path in images:
            if img_path and os.path.exists(img_path):
                with open(img_path, "rb") as f:
                    encoded_images.append(base64.b64encode(f.read()).decode("utf-8"))
        if encoded_images:
            payload["messages"][-1]["images"] = encoded_images

    try:
        resp = requests.post(url, json=payload, timeout=90)  # Added timeout
        resp.raise_for_status()
        return resp.json()["message"]["content"].strip()
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"


#extractor model
def extract_relevant_passages(text: str, query: str) -> str:

    system_msg = (
        "You are a Website Summariser. Your goal is to prepare this summary for another model to answer the query.\n\n"
        "Rules:\n"
        "1. EXTRACT: Capture all relevant facts, qualitative descriptions, characteristics, and attributes related to the subject.\n"
        "2. STRIP: Remove all 'Suggested content', navigation menus, and ads.\n"
        "3. FORMAT: Return all extracted information in a structured manner.\n"
        "4. STRICTNESS: If the text is unrelated to the subject, do not include it in the summaries"
    )

    # Pass the full text now that you're using Qwen2.5
    user_msg = f"USER QUERY: {query}\n\nSOURCE TEXT:\n{text}"

    print(f"Extracting relevant information from the summarised text")

    return ollama_chat(
        EXTRACTION_MODEL,
        system_msg,
        user_msg,
        keep_alive="30m",
        temperature=0.0,
        max_tokens=768,
        num_ctx=16384,
    )

#generator model
def generate_answer(final_prompt: str, model: str) -> str:
    system_msg = (
        "You are a response generator.\n"
        "GOAL: Answer the user query using the provided RESEARCH DATA.\n\n"
        "Rules:\n"
        "- The provided data are summaries of the referenced links, you need to filter the information directly related to the subject.\n"
        "- Extract every data and statements found about the query in the sources.\n"
        "- Include the name of the website in brackets near each statement."
        "- the response must be infromative, descriptive and rich in context.\n"
    )
    print("\n Generating answer...")

    return ollama_chat(
        model,
        system_msg,
        final_prompt,
        keep_alive="30m",
        temperature=0.2,
        max_tokens=3072,
        num_ctx=8192,  # 12288 might be better for larger sources and summaries
    )
