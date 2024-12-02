Enhanced Privacy in Data Transmission Using Steganography and Cryptography
This project demonstrates how to use steganography and cryptography together to securely transmit data, ensuring privacy during transmission. It allows embedding encrypted text data into both images and audio files. The main objective is to enhance the privacy of data transmission by leveraging both encryption and steganography techniques.

Features
Text Encryption: The project uses RSA encryption to securely encrypt text data before embedding it into other media.
Image Steganography: Encrypted text is embedded into the least significant bits (LSBs) of an image's RGB channels.
Audio Steganography: Encrypted text is embedded into the least significant bits (LSBs) of audio frames.
File Uploads: Users can upload plain text, image, and audio files for encryption and steganography processes.
Encrypted File Saving: Encrypted data can be saved as a .bin file for future use.
Requirements
The following Python packages are required to run this project:

streamlit
pycryptodome
Pillow (for image manipulation)
wave (for audio file manipulation)
You can install the dependencies using pip:


pip install -r requirements.txt
or individually:

pip install streamlit pycryptodome Pillow
Installation
Clone the repository to your local machine:


git clone https://github.com/anjupy/Info_Security.git
Navigate to the project directory:

--> cd yourrepositoryname
--> Create and activate a virtual environment:

--> python3 -m venv venv
--> source venv/bin/activate  # For macOS/Linux
Install the required dependencies:

--> pip install -r requirements.txt
Run the Streamlit app:

--> streamlit run interface.py
Usage
Upload Text File: Choose a plain text file to encrypt. Once encrypted, you can embed it into an image or audio file.
Upload Image File: Select an image file (PNG, JPG, JPEG). You can embed the encrypted text data into the image using least significant bit (LSB) steganography.
Upload Audio File: Select an audio file (WAV, MP3). The encrypted text data can be embedded into the audio file.
Save Encrypted Data: After encryption, you can save the encrypted text as a binary file (encrypted_data.bin) for future use.
Example Workflow: 
1. Upload a text file.
2. Encrypt the data.
3. Upload an image or audio file.
4. Embed the encrypted data into the image or audio file.
5. Save the modified image or audio file.

License
This project is licensed under the MIT License - see the LICENSE file for details.
