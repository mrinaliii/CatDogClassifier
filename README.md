# Cat vs Dog Classifier

A machine learning project for classifying images of cats and dogs using deep learning.

Try the Streamlit App: Simply run the app locally and upload your images for instant classification!
The model is deployed on Modal and the Streamlit app provides a user-friendly interface to interact with it.

## How to Use:
1) Run the Streamlit app (see setup instructions below)
2) Upload an image of a cat or dog using the file uploader
3) Click "Classify Image"
4) See the prediction results with confidence scores!

## Project Structure
<img width="517" height="277" alt="image" src="https://github.com/user-attachments/assets/5df7e113-4eb5-4776-b057-093cbf280dab" />

## Dataset
This project uses the **Dog and Cat Classification Dataset** from Kaggle:
- **Source:** https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset
- **Credit:** Dataset by Bhavik Jikadara
- **Description:** Collection of cat and dog images for binary classification training

## Setup Instructions

### Option 1: Run Locally

1. Clone the Repository
```bash
git clone https://github.com/mrinaliii/CatDogClassifier.git
cd CatDogClassifier
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

4. Use the App
- The app will open in your browser at http://localhost:8501
- Upload an image of a cat or dog
- Click "Classify Image" to get predictions
- The app connects to the deployed Modal API automatically!


### Option 2: Use the API Directly
For developers who want to use the raw API: [FastAPI Documentation](https://manuisliterallykirby--cat-dog-classifier-fastapi-app.modal.run/docs)

### Option 3: Run Locally (Advanced)

1. Clone the Repository
```bash
git clone https://github.com/mrinaliii/CatDogClassifier.git
cd CatDogClassifier
```

2. Important: The trained model file is required to run the application but is not included in this repository due to GitHub's file size limits.

- Download link: [Dropbox Link](https://www.dropbox.com/scl/fi/e34uc4499s90sx7jysj57/cat_dog_classifier.keras?rlkey=siov9wmzdj2cx4tq777i85scr&st=1g7mym0r&dl=1)
- Download cat_dog_classifier.keras from Dropbox
- File size: 217.87 MB
- Place this file in the modal_app/ directory

3. Install dependencies
```bash
cd modal_app
pip install -r requirements.txt
```

4. Deploy to Modal
```bash
modal deploy app.py
```

## Tech Stack

- Frontend: Streamlit
- Backend: FastAPI + Modal
- ML Framework: TensorFlow/Keras
- Deployment: Modal Cloud Platform
