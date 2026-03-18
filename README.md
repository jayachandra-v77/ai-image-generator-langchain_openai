## 🎨 AI Image Generator using OpenAI

A simple Python-based AI Image Generator built using the OpenAI Images API.
This application generates high-quality images from text prompts and saves them locally.


## Features
---------------------------------------------------
- Generate AI images from text prompts
- 1024x1024 high-resolution image output
- Secure API key handling using .env
- Continuous prompt input mode
- Clean and simple Python implementation

## 🛠️ Tech Stack
---------------------------------------------------
- Python
- OpenAI
- dotenv
- base64
- Pillow
- VS Code

## 📂 Project Structure
---------------------------------------------------
AI-Image-Generator/
│
├── app.py
├── .env
├── requirements.txt
└── README.md


## 🔐 Security
-----------------------------------------------------
- API keys are stored securely using environment variables.
- Do NOT upload your .env file to GitHub.

## ⚙️ How It Works
-------------------------------------------------------
- The application loads your OpenAI API key from the .env file using python-dotenv.
- When you run the program, it asks you to enter an image description (prompt).
- The prompt is sent to the OpenAI Images API using the gpt-image-1 model.
- The API generates an image based on your description.
- The image is returned in Base64 format.
- The program decodes the Base64 data into image bytes.
- The image is saved locally as generated_image.png.
- The program continues running until you type exit.

## 👨‍💻 Author
  Jayachandra
