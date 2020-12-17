# CSC420 Project (CosmicMangoes)

## Preprocessing

We wrote a script `preprocessing/preprocess.py` that scales and centre-crop datasets with given dimensions. For example, we can run on our small dataset.

```sh
python preprocessing.py small-test-set 80
```

### Downscaling

We have another script `preprocessing/reduce.py` that reduces the square images from the processed dataset to a reduced dataset.

```sh
python reduce.py small-test-set 40
```

## Methods

- Linear Interpolation
  - Function `intropolate()` in notebook `linear_inter.ipynb`.
  - Results in `linear/`.
- OpenCV
  - Function `doit()` in notebook `linear_inter.ipynb`.
  - Results in `opencv_/`.
- [Neural_Enhance](https://github.com/alexjc/neural-enhance)
  - We ran this in Docker.
  - Results in `alexjc_neural-enhance/`.
- [CNN and Autoencoders](https://towardsdatascience.com/image-super-resolution-using-convolution-neural-networks-and-auto-encoders-28c9eceadf90)
  - Notebook `cnn-autoencoders/CSC420_CNN_Autoencoders.ipynb`.
  - Results in `cnn-autoencoders/`/

### Evaluation

- Pixel-Wise Mean-Squared Error: `mse.py`
  - Results in `<results-set-directory>/mses.txt`.
- Pixel-Wise Gradient Mean-Squared Error `gradients.py`
  - Results in `<results-set-directory>/gradients.txt`.
- Corner Detection: `corner-detection.py`
  - Corner Counts
  - Mean-Square Error of Closest Corner Distances
  - Results in `<results-set-directory>/corners.txt`.
