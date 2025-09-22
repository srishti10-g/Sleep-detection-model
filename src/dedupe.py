import os
from PIL import Image
import imagehash

def remove_perceptual_duplicates(folder, hash_size=16, threshold=5):
    seen_hashes = {}
    removed_count = 0

    for subdir, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(subdir, file)
            try:
                img = Image.open(path).convert('RGB')
                img_hash = imagehash.phash(img, hash_size=hash_size)

                found_duplicate = False
                for h in seen_hashes:
                    if abs(img_hash - h) <= threshold:
                        os.remove(path)
                        removed_count += 1
                        print(f"Removed perceptual duplicate: {path}")
                        found_duplicate = True
                        break

                if not found_duplicate:
                    seen_hashes[img_hash] = path

            except Exception as e:
                print(f"⚠️ Could not process {path}: {e}")

    print(f"\n Finished! Removed {removed_count} perceptual duplicates from '{folder}'.\n")


if __name__ == "__main__":
    
    datasets = [
        "dataset/dataset_awake/awake",
        "dataset/sleeping"
    ]

    for ds in datasets:
        print(f"[INFO] Removing perceptual duplicates from '{ds}'...")
        remove_perceptual_duplicates(ds)
