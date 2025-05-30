import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [brandText, setBrandText] = useState("");
  const [brandLogo, setBrandLogo] = useState(null);
  const [bgImage, setBgImage] = useState(null);
  const [imageSize, setImageSize] = useState("512x512");
  const [poster, setPoster] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!brandText || !brandLogo || !bgImage || !imageSize) {
      alert("Please fill all fields.");
      return;
    }

    const formData = new FormData();
    formData.append("brand_text", brandText);
    formData.append("brand_logo", brandLogo);
    formData.append("bg_image", bgImage);
    formData.append("image_size", imageSize);

    try {
      setLoading(true);
      const res = await axios.post("http://localhost:8000/generate", formData);
      setPoster(`data:image/png;base64,${res.data.image_base64}`);
    } catch (err) {
      console.error("Poster generation failed:", err);
      alert("Error generating poster.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="form-box">
        <h1 className="form-title">Poster Generator</h1>

        <input
          type="text"
          placeholder="Brand Text"
          value={brandText}
          onChange={(e) => setBrandText(e.target.value)}
          className="input-field"
        />

        <div className="file-group">
          <label>Brand Logo:</label>
          <input
            type="file"
            accept="image/*"
            onChange={(e) => setBrandLogo(e.target.files[0])}
          />
        </div>

        <div className="file-group">
          <label>Background Image:</label>
          <input
            type="file"
            accept="image/*"
            onChange={(e) => setBgImage(e.target.files[0])}
          />
        </div>

        <input
          type="text"
          placeholder="Image Size (e.g., 512x512)"
          value={imageSize}
          onChange={(e) => setImageSize(e.target.value)}
          className="input-field"
        />

        <button
          onClick={handleGenerate}
          className="submit-button"
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Poster"}
        </button>

        {poster && (
          <div className="poster-preview">
            <h2>Generated Poster</h2>
            <img src={poster} alt="Generated poster" className="poster-image" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
