# 🖼️ Product Poster Generator

This repository contains a client-server web application for generating brand-specific posters using generative AI and layout-aware rendering. The system is designed with a modular architecture to enable interpretable and controllable image synthesis tailored for real-world marketing.

---

## 🔧 Key Updates

### 🖥️ Frontend (React.js)
A user-friendly web interface enables users to:
- Upload a **brand logo image**
- Upload a **background image**
- Enter **brand-related text**
- Specify **output image dimensions** (e.g., `512x512`)

Upon submission, all inputs are transmitted to the backend using an HTTP `POST` request in `multipart/form-data` format.

---

### 🧠 Backend (FastAPI + Python)
The backend is responsible for:
- Image preprocessing and layout logic
- Rendering brand assets and text
- Image generation using a modular machine learning pipeline

---

## 🎨 Prompt-Based Diffusion Approach (Previous Version)

This system originally used a **prompt-driven Stable Diffusion pipeline** with the Hugging Face `diffusers` library:

#### 🔹 Prompt Engineering
User text was converted into descriptive prompts, e.g.:
> "A modern product poster featuring the logo of BrandX, with a sleek background and stylish text."

#### 🔹 Image Generation
The `StableDiffusionPipeline` generated posters based only on the text prompt — no brand image/logo integration.

#### 🔹 Limitations
- No control over logo or text placement
- No integration of actual uploaded assets
- Text rendering was unreliable in generated images

---

## ✅ Current Updates

### 1. Structured Input Handling
- Accepts **logo**, **background image**, **brand text**, and **image dimensions** as separate inputs
- Each input is processed independently for layout generation

### 2. Intermediate Layout Generation
- Introduces a **rule-based layout generator**
- Computes bounding boxes for text and logo:
  - Ensures **non-overlapping**, **visually balanced** placements
  - Enables spatial consistency and interpretability

### 3. Integrated Asset Rendering
- Uses `Pillow` and `OpenCV` to process and render:
  - Brand logo onto the background
  - Text in precise layout positions
- Overcomes fidelity issues of native diffusion-based text rendering

### 4. Image Output & Delivery
- Final poster is encoded as a **base64 image**
- Sent back to the frontend and rendered using a standard `<img>` tag

---

## 🚀 Planned Enhancements (Ongoing Research)

The application is evolving into a **Planning + Rendering** framework for structured generative design. Current focus areas include:
- Modular layout planning
- Interpretable visual encoding
- Controllable generative rendering
- Layout diversity & brand consistency

These features are in the **prototyping and evaluation phase** with the goal of scaling to real-world marketing use cases.

---

## 📚 References

- [IJCAI 2022: Layout-Aware Design via Planning](https://www.ijcai.org/proceedings/2022/0692.pdf)
- [Diffusion-Based Document Design (2023)](https://arxiv.org/html/2312.08822v2#S)
- [FastAPI: Request Body Tutorial](https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemodel)
- [FastAPI Tutorial (YouTube)](https://www.youtube.com/watch?v=3l16wCsDglU&t=1912s)
- [Stable Diffusion v1.4 on Hugging Face](http://huggingface.co/CompVis/stable-diffusion-v1-4)

---

## ✨ Contributors

- **yonishi-13** – [GitHub](https://github.com/yonishi-13)

---

