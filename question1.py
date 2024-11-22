from skimage import io, feature, color
import matplotlib.pyplot as plt

# Load the images by their names in the folder
image1 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-1.png', as_gray=True)
image2 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-2.png', as_gray=True)
image3 = io.imread('C:/Users/PC/Desktop/LBP/Images/LBPimage-3.png', as_gray=True)


# Parameters for LBP
radius = 1  # Radius of LBP pattern
n_points = 8 * radius  # Number of points in LBP pattern

# Compute LBP for each image
lbp1 = feature.local_binary_pattern(image1, n_points, radius, method="uniform")
lbp2 = feature.local_binary_pattern(image2, n_points, radius, method="uniform")
lbp3 = feature.local_binary_pattern(image3, n_points, radius, method="uniform")

# Plotting the original images and their LBP representations
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
images = [image1, lbp1, image2, lbp2, image3, lbp3]
titles = ['Original Image 1', 'LBP Image 1', 'Original Image 2', 'LBP Image 2', 'Original Image 3', 'LBP Image 3']

for i, (ax, img, title) in enumerate(zip(axes.flatten(), images, titles)):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
