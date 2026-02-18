import os
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image
import base64

#Load API Key

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image(prompt):
    try:
        print("\n🎨 Generating image... Please wait...")

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )


        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        file_name = "generated_image.png"

        with open(file_name, "wb") as f:
            f.write(image_bytes)

        print(f"\n✅ Image saved as {file_name}")

    except Exception as e:
          print("❌ Error:", e)

if __name__== "__main__":
     while True:
          user_prompt = input("\nEnter image description (or type 'exit'): ")

          if user_prompt.lower()== "exit":
               print("Exiting application...")
               break
          
          generate_image(user_prompt)
    
     
