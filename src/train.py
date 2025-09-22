import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from datapipeline import create_generators

EPOCHS = 20
IMG_SIZE = (128, 128)

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(*IMG_SIZE, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.5),
        Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer=Adam(1e-4),
                  loss="binary_crossentropy",
                  metrics=["accuracy"])
    return model

if __name__ == "__main__":
    train_gen, val_gen = create_generators()
    model = build_model()

    history = model.fit(
        train_gen,
        epochs=EPOCHS,
        validation_data=val_gen
    )

    model.save("../models/watchman_model.keras")
    model.save("../models/watchman_model.h5")
    print("✅ Model trained and saved in models/")
