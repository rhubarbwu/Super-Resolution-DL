import cv2
import numpy as np
import queue
import sys

sys.setrecursionlimit(1000000)


def BFS(matrix, queue=None):
    curr_indices = queue.get()
    curr_x, curr_y = curr_indices[0], curr_indices[1]

    element = matrix[curr_y, curr_x]
    if element:
        return curr_x, curr_y

    for n in range(curr_x-1, curr_x+2):
        for m in range(curr_y-1, curr_y+2):
            if not (n == curr_x and m == curr_y) \
                    and n > -1 and m > -1 \
                    and n < matrix.shape[0] and m < matrix.shape[1] \
                    and (n, m) not in queue.queue:
                queue.put((n, m))
    return BFS(matrix, queue)


def nearest_other_corner(corner_map, x, y):
    Q = queue.Queue()
    Q.put((x, y))
    bfs_x, bfs_y = BFS(corner_map, Q)

    return np.sqrt((bfs_x-x)**2 + (bfs_y-y)**2)


img0 = cv2.imread(sys.argv[1])
operatedImage = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
operatedImage = np.float32(operatedImage)
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
corners_0 = dest > 0.01 * dest.max()


img1 = cv2.imread(sys.argv[2])
operatedImage = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
operatedImage = np.float32(operatedImage)
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
corners_1 = dest > 0.01 * dest.max()


corner_distances_0, corners_count_0 = np.ndarray(corners_0.shape), 0
for i in range(corners_0.shape[0]):
    for j in range(corners_0.shape[1]):
        if not corners_0[i][j]:
            corner_distances_0[i, j] = 0
            continue
        corners_count_0 += 1
        corner_distances_0[i, j] = nearest_other_corner(corners_1, i, j)
corner_distances_1, corners_count_1 = np.ndarray(corners_1.shape), 0
for i in range(corners_1.shape[0]):
    for j in range(corners_1.shape[1]):
        if not corners_1[i][j]:
            corner_distances_1[i, j] = 0
            continue
        corners_count_1 += 1
        corner_distances_1[i, j] = nearest_other_corner(corners_0, i, j)


print("Corner Detection Evaluation for", sys.argv[2], "\n")
corner_count_diff = corners_count_1-corners_count_0
print("Corner Count Differences", corner_count_diff)
print("Nearest Corner Distances (Original to Upscaled)",
      np.average(corner_distances_0))
print("Nearest Corner Distances (Upscaled to Original)",
      np.average(corner_distances_1))
