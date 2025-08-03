from modal import App, Image, asgi_app

app = App("cat-dog-classifier")

image_dep = (
    Image.debian_slim()
    .pip_install(
        "fastapi", 
        "numpy", 
        "pillow", 
        "tensorflow",
        "python-multipart"  
    )
    .add_local_file("cat_dog_classifier.keras", remote_path="/app/cat_dog_model.keras")
)

@app.function(image=image_dep)
@asgi_app()
def fastapi_app():
    from fastapi import FastAPI, UploadFile, File
    from io import BytesIO
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
    import numpy as np
    from PIL import Image as PILImage
    
    web_app = FastAPI()
    
    model = load_model("/app/cat_dog_model.keras")

    @web_app.post("/predict")
    async def predict(file: UploadFile = File(...)):
        contents = await file.read()
        img = PILImage.open(BytesIO(contents)).convert("RGB")
        img = img.resize((150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array)[0][0]
        label = "Dog" if prediction > 0.5 else "Cat"
        confidence = float(prediction) if prediction > 0.5 else 1 - float(prediction)
        return {"class": label, "confidence": round(confidence, 4)}

    @web_app.get("/")
    async def root():
        return {"message": "Cat-Dog Classifier API", "endpoint": "/predict"}

    return web_app
