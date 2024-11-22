from skimage import io, feature
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def compute_lbp_histogram(image, radius=1, n_points=8 * 1, block_size=(40, 40), bins=256):
    """
    Compute the 256-bin LBP histogram for each block in the image.
    Args:
    - image: Grayscale image for which to compute the LBP.
    - radius: Radius of LBP pattern.
    - n_points: Number of points in LBP pattern.
    - block_size: Size of the blocks (height, width) for histogram calculation.
    - bins: Number of bins for the histogram (256 for full range).
    Returns:
    - histograms: Concatenated histograms for all blocks in the image.
    """
    # Compute LBP
    lbp_image = feature.local_binary_pattern(image, n_points, radius, method="uniform")
    
    # Initialize an empty list to store histograms
    histograms = []
    
    # Divide image into blocks and calculate histograms
    for y in range(0, image.shape[0], block_size[0]):
        for x in range(0, image.shape[1], block_size[1]):
            # Define the block
            block = lbp_image[y:y + block_size[0], x:x + block_size[1]]
            
            # Compute histogram for the block and normalize it
            hist, _ = np.histogram(block.ravel(), bins=bins, range=(0, bins), density=True)
            histograms.extend(hist)  # Append the histogram to the list
    
    return np.array(histograms)

# Load the images
image1 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-1.png', as_gray=True)
image2 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-2.png', as_gray=True)
image3 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-3.png', as_gray=True)

# Compute histograms for each image
histogram1 = compute_lbp_histogram(image1)
histogram2 = compute_lbp_histogram(image2)
histogram3 = compute_lbp_histogram(image3)

# Create a DataFrame with the histograms for better visualization
histograms_df = pd.DataFrame({
    'Histogram Image 1': histogram1,
    'Histogram Image 2': histogram2,
    'Histogram Image 3': histogram3
})

# Display the histogram data
print(histograms_df)

# Optional: plot the histogram for each image
plt.figure(figsize=(10, 6))
plt.plot(histogram1, label='Histogram Image 1')
plt.plot(histogram2, label='Histogram Image 2')
plt.plot(histogram3, label='Histogram Image 3')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('256-bin LBP Histogram for Each Image')
plt.legend()
plt.show()
