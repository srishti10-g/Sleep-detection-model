import os
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from data_pipeline import get_train_validation_generators
from model_setup import build_model, unfreeze_last_layers

# Config
DATA_PATH = "dataset"
MODEL_PATH = "models/mobilenet_sleep_improved.h5"
EPOCHS = 70

# Load data
train_gen, val_gen = get_train_validation_generators(DATA_PATH)

# Build model
model, base_model = build_model()

# Callbacks
checkpoint = ModelCheckpoint(MODEL_PATH, monitor='val_accuracy', save_best_only=True, mode='max')
earlystop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Stage 1: Training with frozen base
print("[INFO] Training stage 1 - frozen base model")
model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    callbacks=[checkpoint, earlystop]
)

# Fine-tuning last 50 layers
print("[INFO] Fine-tuning last 50 layers")
base_model.trainable = True
unfreeze_last_layers(base_model, num_layers=50)
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS // 2,
    callbacks=[checkpoint, earlystop]
)

print(f"[INFO] Training complete. Model saved at {MODEL_PATH}")
