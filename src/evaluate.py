import tensorflow as tf
from datapipeline import create_generators

if __name__ == "__main__":
    train_gen, val_gen = create_generators()
    model = tf.keras.models.load_model("../models/watchman_model.keras")

    loss, acc = model.evaluate(val_gen)
    print(f"✅ Validation Accuracy: {acc*100:.2f}% | Loss: {loss:.4f}")
