import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -- CONFIG --
DATASET_DIR = "dataset"  
IMG_SIZE = (128, 128)
BATCH_SIZE = 32

def create_generators():
    datagen = ImageDataGenerator(
        rescale=1.0/255,
        validation_split=0.2,
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode="nearest"
    )

    train_gen = datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="binary",
        subset="training"
    )

    val_gen = datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="binary",
        subset="validation"
    )

    print(" Class indices:", train_gen.class_indices)
    return train_gen, val_gen
