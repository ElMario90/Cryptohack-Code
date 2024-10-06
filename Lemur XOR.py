from PIL import Image
import numpy as np

# Load the two images
image1 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
image2 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")

# Ensure both images have the same dimensions
if image1.size != image2.size:
    raise ValueError("Images must have the same dimensions")

# Convert images to NumPy arrays (RGB values)
img1_data = np.array(image1)
img2_data = np.array(image2)

# Perform XOR on RGB channels
xor_result = np.bitwise_xor(img1_data, img2_data)

# Convert the result back to an image
result_image = Image.fromarray(xor_result)

# Save or display the result image
result_image.show()  # This will display the image
result_image.save("xor_result.png")  # This will save the image to a file
