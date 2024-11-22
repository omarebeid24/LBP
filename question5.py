from skimage import io, feature
import numpy as np
import matplotlib.pyplot as plt

def get_center_block_histogram(image, radius=1, n_points=8, block_size=(40, 40), center_block=(3, 3), bins=59):
    """
    Extracts the 59-bin LBP histogram of the specified center region (block 3,3) from the image.
    Args:
    - image: Grayscale image for which to compute the LBP.
    - radius: Radius of LBP pattern.
    - n_points: Number of points in LBP pattern.
    - block_size: Size of the blocks (height, width).
    - center_block: Coordinates of the center block (y, x) in block grid terms.
    - bins: Number of bins for the histogram (59 for uniform patterns).
    Returns:
    - histogram: The 59-bin histogram for the specified block.
    """
    # Compute LBP
    lbp_image = feature.local_binary_pattern(image, n_points, radius, method="uniform")
    
    # Calculate the coordinates of the center block
    y_start = center_block[0] * block_size[0]
    x_start = center_block[1] * block_size[1]
    block = lbp_image[y_start:y_start + block_size[0], x_start:x_start + block_size[1]]
    
    # Compute and normalize the histogram for the center block
    histogram, _ = np.histogram(block.ravel(), bins=bins, range=(0, bins), density=True)
    
    return histogram

# Load the images from your specified paths
image1 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-1.png', as_gray=True)
image2 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-2.png', as_gray=True)
image3 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-3.png', as_gray=True)

# Compute histograms for the center region (3,3) of each image
center_histogram1 = get_center_block_histogram(image1)
center_histogram2 = get_center_block_histogram(image2)
center_histogram3 = get_center_block_histogram(image3)

# Plot the 59-bin histogram for each center region
fig, axes = plt.subplots(3, 1, figsize=(10, 12))
histograms = [center_histogram1, center_histogram2, center_histogram3]
titles = ["59-bin Histogram for Center Region (3,3) - Image 1", 
          "59-bin Histogram for Center Region (3,3) - Image 2", 
          "59-bin Histogram for Center Region (3,3) - Image 3"]

for ax, hist, title in zip(axes, histograms, titles):
    ax.bar(range(59), hist, width=1)
    ax.set_title(title)
    ax.set_xlabel("LBP Pattern")
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.show()
