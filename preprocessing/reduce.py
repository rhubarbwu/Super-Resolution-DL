import cv2
import os
import sys

dim = int(sys.argv[2])

path = sys.argv[1]+"_processed"
files = os.listdir(path)
files.sort()

reduced_path = path.replace("processed", "reduced")
if not os.path.exists(reduced_path):
    os.mkdir(reduced_path)

for filename in files:
    filepath = os.path.join(path, filename)
    img = cv2.imread(filepath)

    # reject non-images and images that are mis-sized
    if img is None:
        continue
    if img.shape[0] < dim or img.shape[1] < dim:
        continue

    # resize and write
    resized = cv2.resize(img, (dim, dim), interpolation=cv2.INTER_AREA)
    new_filepath = os.path.join(reduced_path, filename)
    cv2.imwrite(new_filepath, resized)
