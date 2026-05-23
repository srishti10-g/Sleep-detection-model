# 😴 SleepGuardAI  
### Real-Time Sleep Detection & Alert System using Deep Learning

<p align="center">
  <img src=""C:\Users\Srishti Goswami\Pictures\Screenshots\Screenshot (88).png"" width="100%" alt="SleepGuardAI dashboard"/>
  <img src=""C:\Users\Srishti Goswami\Pictures\Screenshots\Screenshot (101).png"" width="100%" alt="SleepGuardAI analysis"/>
  <img src=""E:\downloads\Untitled design.png"" width="100%" alt="SleepGuardAI live"/>
</p>

---

# 🚀 Overview

**SleepGuardAI** is an AI-powered real-time monitoring system designed to detect whether a person is **sleeping or awake** using computer vision and deep learning techniques.

The system continuously analyzes webcam video frames and instantly alerts when drowsiness or sleeping behavior is detected.

This project is especially useful in areas like:

- 🚓 Security Monitoring
- 🚚 Driver Drowsiness Detection
- 🏭 Workplace Safety
- 🛡 Watchman Monitoring Systems
- 🎓 Smart Surveillance Applications

---

# 🧠 Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

# ✨ Features

✅ Real-time sleeping vs awake detection
✅ Saves Logs $ Reports in Excel sheet with duration
✅ Deep Learning–based CNN model  
✅ Live webcam monitoring using OpenCV  
✅ Automatic alert/alarm system  
✅ Data preprocessing & augmentation pipeline  
✅ Duplicate image removal utility  
✅ Easy training with custom datasets  
✅ Modular and scalable project structure  

---

# 📸 Screenshots

## 🔹 Real-Time Dashboard

![Dashboard](C:\Users\Srishti Goswami\Pictures\Screenshots\Screenshot (88).png)

---

## 🔹 Sleeping Alert Triggered

![Alert](E:\downloads\Untitled design.png)

---

# 🏗 Project Architecture

```text
Webcam Feed
      ↓
Frame Capture using OpenCV
      ↓
Image Preprocessing
      ↓
CNN Model Prediction
      ↓
Sleeping / Awake Classification
      ↓
Alarm Trigger (if sleeping detected)
```

---

# 📂 Repository Structure

```text
SleepGuardAI/
│
├── data_sample/              # Demo dataset samples
├── models/                   # Trained deep learning models
│
├── screenshots/              # README images & screenshots
│
├── src/
│   ├── data_collection.py    # Image scraping & data collection
│   ├── dedupe.py             # Duplicate image removal
│   ├── organize.py           # Dataset organization utility
│   ├── datapipeline.py       # Data preprocessing & augmentation
│   ├── train.py              # CNN model training
│   ├── evaluate.py           # Model evaluation
│   ├── realtime.py           # Real-time webcam detection
│
├── requirements.txt          # Required dependencies
├── README.md                 # Project documentation
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SleepGuardAI.git
cd SleepGuardAI
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Real-Time Detection

```bash
python src/realtime.py
```

---

# 🧪 Model Training

To retrain the CNN model using your own dataset:

```bash
python src/train.py
```

The trained model will automatically be saved inside the `models/` directory.

---

# 📊 Future Improvements

- 🔹 Eye blinking analysis
- 🔹 Head pose estimation
- 🔹 Mobile application integration
- 🔹 Cloud-based monitoring dashboard
- 🔹 Multi-person detection support
- 🔹 Higher accuracy using advanced CNN architectures

---

# 👩‍💻 Author

### Srishti Goswami

AI & Data Science Student  
Passionate about AI, Deep Learning & Real-World Problem Solving

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

