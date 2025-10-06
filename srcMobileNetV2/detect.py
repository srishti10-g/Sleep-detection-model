import cv2
import numpy as np
import tensorflow as tf
import winsound

# Load model
MODEL_PATH = "models/mobilenet_sleep_improved.h5"
IMG_SIZE = 224
ALARM_THRESHOLD = 15
alpha = 0.3  # smoothing factor

model = tf.keras.models.load_model(MODEL_PATH)

# Camera setup
cap = cv2.VideoCapture(0)
alarm_counter = 0
smooth_pred = 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0][0]
    smooth_pred = alpha * pred + (1 - alpha) * smooth_pred

    if smooth_pred < 0.5:
        alarm_counter = 0
        label = "Awake"
        color = (0, 255, 0)
    else:
        alarm_counter += 1
        label = f"Sleeping ({alarm_counter})"
        color = (0, 0, 255)

    if alarm_counter > ALARM_THRESHOLD:
        winsound.Beep(2500, 1000)
        alarm_counter = 0

    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Sleep Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
