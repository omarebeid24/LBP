from skimage import io, feature
import numpy as np

def compute_uniform_lbp_histogram_blocks(image, radius=1, n_points=8, block_size=(40, 40), bins=59):
    """
    Compute the 59-bin LBP histogram for uniform patterns for each block in the image.
    Args:
    - image: Grayscale image for which to compute the LBP.
    - radius: Radius of LBP pattern.
    - n_points: Number of points in LBP pattern.
    - block_size: Size of the blocks (height, width) for histogram calculation.
    - bins: Number of bins for the histogram (59 for uniform patterns).
    Returns:
    - histograms: List of histograms for each block in the image.
    """
    lbp_image = feature.local_binary_pattern(image, n_points, radius, method="uniform")
    histograms = []
    
    # Divide the image into blocks and calculate the histogram for each block
    for y in range(0, image.shape[0], block_size[0]):
        for x in range(0, image.shape[1], block_size[1]):
            block = lbp_image[y:y + block_size[0], x:x + block_size[1]]
            hist, _ = np.histogram(block.ravel(), bins=bins, range=(0, bins), density=True)
            histograms.append(hist)
    
    return histograms

def weighted_chi_square(S_histograms, M_histograms):
    """
    Calculate the weighted Chi-Square statistic across all blocks between two sets of histograms.
    Args:
    - S_histograms, M_histograms: Lists of block histograms for the sample and model images.
    Returns:
    - chi_square_value: The total weighted Chi-Square distance.
    """
    chi_square_total = 0
    for S, M in zip(S_histograms, M_histograms):
        chi_square_block = np.sum(((S - M) ** 2) / (S + M + 1e-10))  # Sum for each block
        chi_square_total += chi_square_block

    return chi_square_total

# Load images from the specified paths
image1 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-1.png', as_gray=True)
image2 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-2.png', as_gray=True)
image3 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-3.png', as_gray=True)

# Compute 59-bin uniform LBP histograms for each block in each image
block_histograms_S = compute_uniform_lbp_histogram_blocks(image1)  # Sample (S)
block_histograms_M1 = compute_uniform_lbp_histogram_blocks(image2)  # Model (M1)
block_histograms_M2 = compute_uniform_lbp_histogram_blocks(image3)  # Model (M2)

# Calculate the weighted Chi-Square match scores for each image pair
score_S_M1 = weighted_chi_square(block_histograms_S, block_histograms_M1)
score_S_M2 = weighted_chi_square(block_histograms_S, block_histograms_M2)
score_M1_M2 = weighted_chi_square(block_histograms_M1, block_histograms_M2)

# Display the match scores
print("Weighted Chi-Square Match Scores:")
print(f"Sample (S) - Model (M1): {score_S_M1}")
print(f"Sample (S) - Model (M2): {score_S_M2}")
print(f"Model (M1) - Model (M2): {score_M1_M2}")
