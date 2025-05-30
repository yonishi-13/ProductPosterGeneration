from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware 
from io import BytesIO
import base64
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
import os

app = FastAPI()

# CORS setup for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load the Stable Diffusion model (recommended to run on GPU)
model_id = "CompVis/stable-diffusion-v1-4"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    revision="fp16",
    safety_checker=None
).to("cpu")


@app.post("/generate")
async def generate(
    brand_text: str = Form(...),
    brand_logo: UploadFile = Form(...),
    bg_image: UploadFile = Form(...),
    image_size: str = Form(...)
):
    # Parse image size (e.g. "512x512")
    try:
        width, height = map(int, image_size.lower().split("x"))
    except:
        width, height = 512, 512  # Default fallback

    # Load and analyze brand logo and background
    logo_img = Image.open(BytesIO(await brand_logo.read())).convert("RGBA")
    bg_img = Image.open(BytesIO(await bg_image.read())).convert("RGBA")

    # Generate a simple descriptive prompt
    prompt = (
        f"A high-quality promotional poster for '{brand_text}', "
        "featuring a professional layout with logo and background, "
        "modern typography, centered branding, studio lighting, clean and elegant design"
    )

    # Generate poster with Stable Diffusion
    with torch.no_grad():
        image = pipe(prompt, height=height, width=width, guidance_scale=8.5).images[0]

    # Convert output to base64
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    imgstr = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return {"image_base64": imgstr}
