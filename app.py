import os
from openai import OpenAI
import gradio as gr
import base64
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def analyze_images_with_gpt4o(images):
    summaries = []
    assessments = []

    for img in images:
        img_pil = Image.open(img)
        img_b64 = image_to_base64(img_pil)

        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # Updated to use gpt-4o which has vision capabilities
                messages=[
                    {"role": "system", "content": "You are a workplace safety expert specialising in UK Health & Safety compliance."},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": (
                                "Please do two things:\n"
                                "1. Describe the image as a workplace scene.\n"
                                "2. Provide a UK-style Health & Safety risk assessment based on what you see, "
                                "following HSE guidelines (e.g., HSW Act 1974, PUWER, PPE 2022)."
                            )},
                            {"type": "image_url", "image_url": {
                                "url": f"data:image/png;base64,{img_b64}"
                            }},
                        ],
                    }
                ],
                max_tokens=1000,
            )

            result = response.choices[0].message.content
            summaries.append(f"--- Analysis for {img.name} ---\n{result}")
        except Exception as e:
            summaries.append(f"--- Error analyzing {img.name} ---\nError: {str(e)}")

    full_output = "\n\n".join(summaries)
    return full_output

# Gradio UI
demo = gr.Interface(
    fn=analyze_images_with_gpt4o,
    inputs=gr.File(file_types=["image"], file_count="multiple", label="Upload Photo(s)"),
    outputs=gr.Textbox(label="Scene Analysis + H&S Risk Report", lines=30),
    title="DeanAI Photo-Based H&S Risk Assessor",
    description="Powered by GPT-4 Vision. Upload workstation or site photos and get a UK Health & Safety risk assessment instantly.",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        exit(1)
    
    # Launch the app
    demo.launch() 