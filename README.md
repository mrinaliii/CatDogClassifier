# Cat vs Dog Classifier

A machine learning project for classifying images of cats and dogs using deep learning.

## 🚀 Live Demo
**Try it now:** [Cat vs Dog Classifier API](https://manuisliterallykirby--cat-dog-classifier-fastapi-app.modal.run/docs)

The model is deployed and ready to use! Upload an image and get instant predictions.
##Steps:
1) Click on the link
2) Click on the green button labelled **Post**
3) In parameters you'll see a button named **Try it out**
4) Then a file section will appear where you can add an image of a cat or a dog to test the model. Click on **Choose File**.
5) When done, click on the blue button labelled **Execute**.
6) Scroll down, in response body you'll see the predicted class. :)

## Project Structure
dog-cat-classifier/
├── data_split/          # Dataset splitting scripts/files
├── model_training/      # Training notebooks and model files
│   ├── model.ipynb
│   └── cat_dog_classifier.keras
├── modal_app/          # Deployment application
│   ├── app.py
│   ├── requirements.txt
│   └── (model file goes here)
├── .gitignore
└── README.md

## Setup Instructions

### Option 1: Use the Live Deployment (Recommended)
Just visit: [https://manuisliterallykirby--cat-dog-classifier-fastapi-app.modal.run/docs](https://manuisliterallykirby--cat-dog-classifier-fastapi-app.modal.run/docs)

### Option 2: Run Locally

1. Clone the Repository
```bash
git clone https://github.com/mrinaliii/CatDogClassifier.git
cd CatDogClassifier
```

2. Download the Trained Model
⚠ Important: The trained model file is required to run the application but is not included in this repository due to GitHub's file size limits.
Download the model file:

Download cat_dog_classifier.keras from Dropbox
File size: 217.87 MB
Place this file in the modal_app/ directory

3. Install Dependencies
```bash
cd modal_app
pip install -r requirements.txt
```

4. Run the Application
bashpython app.py
