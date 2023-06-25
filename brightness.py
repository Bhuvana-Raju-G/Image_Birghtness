from PIL import ImageEnhance,Image

# Open the image
image = Image.open("input2.jpg")

# Adjust brightness and contrast
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)  # Increase brightness by 50%


# Save the enhanced image
brightened_image.save("imgEnhancement/Brightened_image2.jpg")
