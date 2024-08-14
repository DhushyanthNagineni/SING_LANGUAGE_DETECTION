# Sign Language Detection

This project aims to detect sign language gestures using a machine learning model. The workflow involves collecting images, extracting key points, training a model, and using a live camera feed to predict sign language gestures.

## Project Structure

The project consists of the following Python files:

1. `sign_image_collection.py`
2. `function.py`
3. `data.py`
4. `train_model.py`
5. `app.py`

## Workflow

### 1. Image Collection
First, collect images for each sign using `sign_image_collection.py`. Store the images in folders named `A`, `B`, `C`, and `D` respectively.

### 2. Data Preparation
Run `data.py` to collect key points from the images using MediaPipe and store them in a NumPy array.

### 3. Model Training
Run `train_model.py` to train the model. The trained model will be saved as `model.h5` and the intents as `model.js`.

### 4. Live Prediction
Use `app.py` to open a camera pop-up, get live input data, and use `model.h5` to predict the output.

## How to Run
1.**Image Collection**:
  python sign_image_collection.py

2.**Data Preparation**:
  python data.py
 
3.**Model Training**:
  python train_model.py
   
4.**Live Prediction**:
  python app.py

## Dependencies

Python 3.x

MediaPipe

NumPy

TensorFlow

OpenCV

## Install the dependencies using 
`pip install mediapipe tensorflow numpy opencv `


