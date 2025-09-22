#  Real-Time Sleeping Detection System  

## Introduction
Fatigue and drowsiness are common causes of accidents and performance issues, especially in sectors like **transportation, security, and workplace safety**.  
**Watchman AI** is a deep learning–based system designed to **detect whether a person is sleeping or awake in real time** using a webcam.  

The system uses:
- **TensorFlow/Keras** for training a Convolutional Neural Network (CNN).  
- **OpenCV** for real-time webcam detection.  
- **Data preprocessing & augmentation** to improve model accuracy.  

---

## Features
- Automated **sleeping vs. awake detection** from images and video.  
- **Real-time monitoring** via webcam with on-screen labels.  
- **Audible alarm beep** if the person is detected as sleeping.  
- Easy to train with your own dataset.  
- Modular structure for scalability.  

---

## 📂 Repository Structure
│── data_sample/ # small example dataset (demo only)
│── models/ # trained models (.keras, .h5)
│── src/ # main source code
│ ├── data_collection.py #scrapes sleeping and awake images
│ ├── dedupe.py #removes duplicates
│ ├── organize.py # prepare and arrange sub folders into single folder
│ ├── datapipeline.py # handles data augmentation & preprocessing
│ ├── train.py # CNN training script
│ ├── evaluate.py # model evaluation script
│ ├── realtime.py # live webcam detection
│── requirements.txt # dependencies
│── README.md # project documentation
