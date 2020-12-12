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

### Evaluation

- Pixel-Wise Mean-Squared Error: `mse.py`
  - Results in `<results-set-directory>/mses.txt`.
- Pixel-Wise Gradient Mean-Squared Error `gradients.py`
  - Results in `<results-set-directory>/gradients.txt`.
- Corner Detection: `corner-detection.py`
  - Corner Counts
  - Mean-Square Error of Closest Corner Distances
  - Results in `<results-set-directory>/corners.txt`.
