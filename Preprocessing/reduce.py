import cv2
import os

dim = (60, 60)

paths = [
    "Howard",
    "Leonard",
    "Penny",
    "Raj",
    "Sheldon"
]
for path in paths:
    path = "./dataset_dec_3_processed/" + path
    files = os.listdir(path)
    files.sort()

    reduced_path = path+"_reduced_60x60"
    if not os.path.exists(reduced_path):
        os.mkdir(reduced_path)

    for filename in files:
        filepath = os.path.join(path, filename)
        img = cv2.imread(filepath)

        # reject non-images and images that are mis-sized
        if img is None:
            continue
        if img.shape[0] != 80 or img.shape[1] != 80:
            continue

        # resize and write
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        new_filepath = os.path.join(reduced_path, filename)
        cv2.imwrite(new_filepath, resized)
