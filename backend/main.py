from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware 
from io import BytesIO
import base64
from PIL import Image, ImageDraw, ImageFont
import torch
from diffusers import StableDiffusionPipeline

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

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
    # Parse image size
    try:
        width, height = map(int, image_size.lower().split("x"))
    except:
        width, height = 512, 512

    # Load images
    logo = Image.open(BytesIO(await brand_logo.read())).convert("RGBA")
    background = Image.open(BytesIO(await bg_image.read())).convert("RGBA")
    background = background.resize((width, height))

    prompt = (
        f"Modern and clean promotional poster for {brand_text}, "
        f"professional layout, brand elements, minimal design, studio lighting, high quality"
    )

    with torch.no_grad():
        gen_image = pipe(prompt, height=height, width=width, guidance_scale=8.5).images[0]
    gen_image = gen_image.convert("RGBA")

    # Composite the background image
    combined = Image.alpha_composite(gen_image, background)

    # Resize and paste logo
    logo_ratio = 0.2
    logo_width = int(width * logo_ratio)
    logo.thumbnail((logo_width, logo_width), Image.ANTIALIAS)
    logo_position = (width - logo.size[0] - 20, height - logo.size[1] - 20)
    combined.paste(logo, logo_position, logo
                   
    draw = ImageDraw.Draw(combined)
    try:
        font = ImageFont.truetype("arial.ttf", size=32)
    except:
        font = ImageFont.load_default()

    draw.text((30, 30), brand_text, font=font, fill=(255, 255, 255, 255))

    # Convert output to base64
    buffer = BytesIO()
    combined.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return {"image_base64": img_str}
