import cv2
import os
import sys

dim = int(sys.argv[2])

path = sys.argv[1]
files = os.listdir(path)
files.sort()

if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path+"_processed"):
    os.mkdir(path+"_processed")

for filename in files:
    filepath = os.path.join(path, filename)
    img = cv2.imread(filepath)

    # reject non-images and images that are too small
    if img is None:
        continue
    if img.shape[0] < dim or img.shape[1] < dim:
        os.remove(filepath)
    scale_percentage = dim/min(img.shape[0:2])

    # resize
    width = int(img.shape[1] * scale_percentage)
    height = int(img.shape[0] * scale_percentage)
    resized = cv2.resize(
        img,
        (width, height),
        interpolation=cv2.INTER_AREA)

    # crop
    new_top_left = ((resized.shape[0]-dim)//2, (resized.shape[1]-dim)//2)
    centrecrop = resized[
        new_top_left[0]:new_top_left[0]+dim,
        new_top_left[1]:new_top_left[1]+dim]

    new_filepath = filepath.replace(path, path+"_processed")
    cv2.imwrite(new_filepath, centrecrop)
