# The Big Bang Theory Dataset Preprocessing

## Automated Filtering

- Filter photos that have a dimension < 80.
- Downsize so smallest dimension is 80.
- OpenCV centercrop to 80x80.

## Manual Discrimination

- Remove images that are not simple frontals.
  - Basic criteria is all basic facial features are visible, such as both eyes, noses, mouths, eyebrows.
  - Also nose tips should be between the cheeklines.
  - One noteworthy detail is that there are a few photos of Raj where he's holding up a glass of a beverage; the thin reflection off the edge of the glass may introduce interesting results when downsizing and upsampling.
