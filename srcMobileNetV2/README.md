# Real-Time Sleep Detection Using MobileNetV2

## About
This project implements a lightweight real-time sleep detection system using MobileNetV2 transfer learning and OpenCV for webcam input. The system classifies webcam frames as "sleeping" or "awake" and raises an alarm if sleeping is detected continuously for a specified threshold.

## Features
- Data augmentation using Keras ImageDataGenerator  
- Transfer learning with MobileNetV2 and fine-tuning of deeper layers  
- Real-time webcam detection with smoothing for stable predictions  
- Supports integration with CCTV cameras by modifying capture source for remote sleep monitoring in diverse environments

## Repository Structure
sleep_detection/
│
├── dataset/ # Dataset folders (awake/, sleeping/)
├── models/ # Saved models (e.g., mobilenet_sleep_improved.h5)
├── src/
│ ├── data_pipeline.py # Data loading and augmentation
│ ├── model_setup.py # Model building and unfreezing
│ ├── train.py # Training script
│ ├── detect.py # Real-time detection script
│
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore


## Installation

1. Clone the repository and navigate to the project directory.
2. (Optional but recommended) Create and activate a virtual environment:
   - `python3 -m venv venv`
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install required packages:
pip install -r requirements.txt
4. Prepare your dataset inside `dataset/` with two subfolders: `awake/`, `sleeping/`.

## Usage

### Training the model
python src/train.py
This trains the model in two stages: frozen base and fine-tuning of last 50 layers. The best model is saved under `models/mobilenet_sleep_improved.h5`.

### Running real-time detection
python src/detect.py
Starts webcam detection. It will display the label and sound an alarm if sleep is detected continuously. Press `q` to quit.



