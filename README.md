# Local Binary Patterns (LBP) Analysis for Face Images

This task involves analyzing facial images using **Local Binary Patterns (LBP)**, a feature extraction technique widely used in image processing and pattern recognition. The assignment includes computing LBP representations, histograms, and match scores for given images using statistical measures.

---

## Steps 

### 1. **Calculate and Display the LBP Representation**
   - For the provided images **LBP1**, **LBP2**, and **LBP3**:
     - Compute the **LBP representation** for each face image.
     - Visualize and display the LBP representation of the face in each image.

### 2. **Compute the Full 256-Bin LBP Histogram**
   - For each image:
     - Divide the image into blocks of size **40x40 pixels**.
     - Compute the **256-bin histogram** for each block.
     - Generate the feature vector for the entire image by concatenating histograms from all blocks.

### 3. **Display the Histogram for the Center Region**
   - For the **center region (3,3)** of each image:
     - Display the corresponding **256-bin histogram**.

### 4. **Calculate Match Scores Using Chi-Square Statistic**
   - Using the **Chi-Square statistic**, compute the similarity match scores between:
     - **LBP1-LBP2**
     - **LBP1-LBP3**
     - **LBP2-LBP3**
   - The Chi-Square match score is computed as:
     \[
     \chi^2 = \sum \frac{(h_1 - h_2)^2}{h_1 + h_2}
     \]
     where \( h_1 \) and \( h_2 \) are the histogram bins for two images.

### 5. **Compute the 59-Bin Histogram for Uniform Patterns**
   - For each image:
     - Compute the **59-bin histogram** for uniform/fundamental LBP patterns.
     - Use the same block size (**40x40 pixels**) as in the previous steps.

### 6. **Display the 59-Bin Histogram for the Center Region**
   - For the **center region (3,3)** of each image:
     - Display the **59-bin histogram**.

### 7. **Calculate Match Scores for Uniform Patterns**
   - Using the **Chi-Square statistic**, compute the match scores for the uniform pattern histograms between:
     - **LBP1-LBP2**
     - **LBP1-LBP3**
     - **LBP2-LBP3**

---

## Key Outputs

- **LBP Representation**:
  - Visualized LBP patterns for each image.
- **256-Bin Histograms**:
  - Full histograms for all blocks.
  - Histogram for the center region (3,3).
- **Match Scores**:
  - Chi-Square scores for full histograms.
- **59-Bin Uniform Pattern Histograms**:
  - Uniform pattern histograms for all blocks.
  - Histogram for the center region (3,3).
- **Match Scores for Uniform Patterns**:
  - Chi-Square scores for uniform pattern histograms.

---

## Tools and Libraries

- **Python Libraries**:
  - `OpenCV`: For image processing and LBP computation.
  - `NumPy`: For numerical operations.
  - `Matplotlib`: For visualizing LBP representations and histograms.
- **Mathematical Computations**:
  - Use the Chi-Square formula for statistical matching.

---

## How to Run the Code

1. **Preprocess Images**:
   - Load and preprocess the images **LBP1**, **LBP2**, and **LBP3** using Python scripts.

2. **Generate LBP Representations**:
   - Apply LBP computation using OpenCV or similar image processing tools.

3. **Compute and Visualize Histograms**:
   - Calculate the full 256-bin histograms and uniform pattern 59-bin histograms.
   - Display histograms for the center region (3,3).

4. **Compute Match Scores**:
   - Use the Chi-Square statistic to calculate match scores between image pairs.

---

## Notes

- **Uniform Patterns**:
  - Uniform patterns represent LBP patterns with at most two 0-1 or 1-0 transitions.
  - These patterns reduce dimensionality from 256 bins to 59 bins, retaining key features.
- **Chi-Square Statistic**:
  - A lower match score indicates a higher similarity between the images.

---


