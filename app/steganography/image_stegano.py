# app/steganography/image_stegano.py
from PIL import Image
import io

def embed_data_in_image(uploaded_image, data, output_path):
    try:
        # Open the image file using PIL
        image = Image.open(uploaded_image)
        pixels = image.load()  # Load the image pixels

        # Convert the encrypted data into binary format (8-bit)
        binary_data = ''.join(format(byte, '08b') for byte in data)  # No need to encode

        data_index = 0
        width, height = image.size

        for y in range(height):
            for x in range(width):
                if data_index < len(binary_data):
                    pixel = pixels[x, y]
                    
                    # Handle different image modes
                    if len(pixel) == 3:  # RGB image
                        r, g, b = pixel
                    elif len(pixel) == 4:  # RGBA image
                        r, g, b, a = pixel
                    else:
                        raise ValueError("Unsupported image mode")

                    # Modify the least significant bit of each RGB channel
                    r = (r & 0xFE) | int(binary_data[data_index])  # Alter LSB of red
                    data_index += 1

                    if data_index < len(binary_data):
                        g = (g & 0xFE) | int(binary_data[data_index])  # Alter LSB of green
                        data_index += 1

                    if data_index < len(binary_data):
                        b = (b & 0xFE) | int(binary_data[data_index])  # Alter LSB of blue
                        data_index += 1

                    # Update the pixel with the modified values
                    if len(pixel) == 3:
                        pixels[x, y] = (r, g, b)
                    elif len(pixel) == 4:
                        pixels[x, y] = (r, g, b, a)

                if data_index >= len(binary_data):
                    break

            if data_index >= len(binary_data):
                break

        # Save the image with the embedded data
        image.save(output_path)
        print(f"Embedded data successfully saved to {output_path}")

    except Exception as e:
        print(f"Error embedding data in image: {e}")
