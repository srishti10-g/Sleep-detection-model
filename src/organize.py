import os
import shutil

def flatten_dataset(dataset_path):
    for category in ["awake", "sleeping"]:
        category_path = os.path.join(dataset_path, category)

        if not os.path.exists(category_path):
            print(f"⚠️ Folder not found: {category_path}")
            continue

        # Walk through subdirectories
        for root, dirs, files in os.walk(category_path):
            if root == category_path:
                continue  # Skip main folder, only go inside subfolders

            for file in files:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(category_path, file)

                # If file with same name exists, rename
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(dst_path):
                    dst_path = os.path.join(category_path, f"{base}_{counter}{ext}")
                    counter += 1

                # Move file
                shutil.move(src_path, dst_path)

        # Remove empty subfolders
        for root, dirs, files in os.walk(category_path, topdown=False):
            if root != category_path and not os.listdir(root):
                os.rmdir(root)

        print(f" Flattened: {category}")

# Run it
flatten_dataset("dataset")

