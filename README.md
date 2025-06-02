# 🖼️ Product Poster Generator

This repository contains a client-server web application for generating brand-specific posters using generative AI and basic layout logic. The system is designed with a modular architecture to enable interpretable and controllable image synthesis tailored for real-world marketing applications.

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

**Note:**  
No external layout generation framework (e.g., PlanNet, LayoutTransformer) is used at this stage.  
All layout-related decisions (e.g., positioning of logo and text) are handled through **direct logic coded in [`main.py`](./backend/main.py)**.

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
- Inputs are parsed and processed in `main.py` without an external layout engine

### 2. Direct Layout Logic in `main.py`
- A simple **rule-based layout logic** has been implemented in `main.py`
- Calculates bounding boxes for the logo and text manually
- Ensures **non-overlapping**, **visually balanced** placements for initial prototyping

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

The application is evolving into a **Planning + Rendering** framework for structured generative design. Future plans include:
- Integration of layout-aware models like **PlanNet**
- Interpretable and modular layout-to-image pipelines
- Better spatial reasoning and content placement
- Improved layout diversity and branding fidelity

These features are currently in the **prototyping phase**.

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
