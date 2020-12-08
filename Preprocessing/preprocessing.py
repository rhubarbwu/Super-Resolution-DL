import cv2
import os

dim = (80, 80)

paths = [
    "Howard",
    "Leonard",
    "Penny",
    "Raj",
    "Sheldon"
]
for path in paths:
    path = "./data/" + path
    files = os.listdir(path)
    files.sort()

    if not os.path.exists(path):
        os.mkdir(path)

    for filename in files:
        filepath = os.path.join(path, filename)
        img = cv2.imread(filepath)

        # reject non-images and images that are too small
        if img is None:
            continue
        if img.shape[0] < 80 or img.shape[1] < 80:
            os.remove(filepath)

        # resize and write
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        new_filepath = filepath.replace("data", "dataset_dec_3_processed")
        cv2.imwrite(new_filepath, resized)
