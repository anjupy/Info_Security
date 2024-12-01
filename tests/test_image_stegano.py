import os
from app.steganography.image_stegano import embed_data_in_image, extract_data_from_image

def test_image_stegano(tmpdir):
    input_image = "tests/test_image.png"
    output_image = os.path.join(tmpdir, "output_image.png")
    test_data = "Hidden data"
    
    embed_data_in_image(input_image, test_data, output_image)
    extracted_data = extract_data_from_image(output_image)
    
    assert extracted_data.strip() == test_data
