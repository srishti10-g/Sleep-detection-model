import cv2
import numpy as np
import tensorflow as tf
from datapipeline import create_generators

IMG_SIZE = (128, 128)

if __name__ == "__main__":
    # Load model
    model = tf.keras.models.load_model("../models/watchman_model.keras")

    train_gen, _ = create_generators()
    idx_to_class = {v: k for k, v in train_gen.class_indices.items()}

    cap = cv2.VideoCapture(0)

    print(" Launching live detection... Press 'q' to quit.")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break

            img = cv2.resize(frame, IMG_SIZE)
            img = np.expand_dims(img, axis=0) / 255.0

            pred = model.predict(img, verbose=0)[0][0]
            label_idx = int(round(pred))
            label = idx_to_class[label_idx]

            if label.lower() == "sleeping":
                color = (0, 0, 255)
                cv2.putText(frame, "SLEEPING", (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
                try:
                    import winsound
                    winsound.Beep(2500, 500)
                except:
                    pass
            else:
                color = (0, 255, 0)
                cv2.putText(frame, "AWAKE", (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)

            cv2.imshow("Watchman Monitor", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except Exception as e:
        print("Error in live detection:", e)

    finally:
        cap.release()
        cv2.destroyAllWindows()
