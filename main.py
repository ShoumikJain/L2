import requests
from config import HF_API_KEY

model_id = "nlpconnect/vit-gpt2-image-captioning"
api_url = f"https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
print(HF_API_KEY)
headers = {"Authorization":f"Bearer {HF_API_KEY}"}
def caption_single_image():
    image_source = "test.jpg"
    try:
        with open(image_source,"rb") as f:
            image_bytes = f.read()
    except Exception as e:
        print(f"Could not load image from {image_source}.\n Error: {e}")
        return
    response = requests.post(api_url, headers=headers, data=image_bytes)
    print(response.status_code)
    print(response.content.decode("utf-8", errors="ignore"))
    try:
        result = response.json()
    except Exception as e:
        print("Could not decode response as json.")
        return
    if isinstance(result,dict) and "error" in result:
        print(f"[error]{result["error"]}")
        return
    caption = result[0].get("generated_text","No caption found.")
    print("image:",image_source)
    print("caption:",caption)

def main_model():
    caption_single_image()

if __name__ == "__main__":
    main_model()
