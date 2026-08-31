import matplotlib.pyplot as plt
import numpy as np

# Function to apply average filter from scratch
def average_filter(image, kernel_size):
    pad = kernel_size

    # Add zero padding around the image
    padded = np.pad(image, pad, mode='constant', constant_values=0)

    # Create output image
    output = np.zeros_like(image, dtype=np.float32)

    # Average filter kernel
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
    kernel = kernel / (kernel_size * kernel_size)

    # Apply filter
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            # Get the region around the pixel
            region = padded[i:i + kernel_size,
                            j:j + kernel_size]

            # Multiply region with kernel and calculate sum
            output[i, j] = np.sum(region * kernel)

    return output.astype(np.uint8)


# Function to display images
def show_comparison(original, blur3, blur5, blur7):

    plt.figure(figsize=(12, 10))

    # Original image
    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('on')

    # 3x3 kernel
    plt.subplot(2, 2, 2)
    plt.imshow(blur3, cmap='gray')
    plt.title('Average Filter (3x3)')
    plt.axis('on')

    # 5x5 kernel
    plt.subplot(2, 2, 3)
    plt.imshow(blur5, cmap='gray')
    plt.title('Average Filter (5x5)')
    plt.axis('on')

    # 7x7 kernel
    plt.subplot(2, 2, 4)
    plt.imshow(blur7, cmap='gray')
    plt.title('Average Filter (7x7)')
    plt.axis('on')

    plt.tight_layout()
    plt.show()


# Read image WITHOUT cv2
img = plt.imread('image.jpg')

# Convert RGB image to grayscale
if len(img.shape) == 3:
    img = np.mean(img[:, :, :3], axis=2)

# Apply average filters
blur_3_3 = average_filter(img, 3)
blur_5_5 = average_filter(img, 5)
blur_7_7 = average_filter(img, 7)

# Display results
show_comparison(img, blur_3_3, blur_5_5, blur_7_7)