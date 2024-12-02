import os
import streamlit as st
from app.cryptography.encrypt import encrypt_data
from app.steganography.image_stegano import embed_data_in_image
from app.steganography.audio_stegano import embed_data_in_audio
from app.utils.file_io import save_file

def run_interface():
    st.title("Enhanced Privacy in Data Transmission Using Steganography and Cryptography")
    
    encrypted_data = None  # Initialize encrypted_data as None to handle situations where it's not set yet

    # File uploader for plain text
    uploaded_file = st.file_uploader("Choose a plain text file", type="txt")
    if uploaded_file is not None:
        # Read the content of the file
        file_content = uploaded_file.getvalue().decode("utf-8")  # Decode bytes to string

        # Encrypt the data, ensuring it's in bytes format
        encrypted_data, private_key, public_key = encrypt_data(file_content.encode("utf-8"))  # Ensure data passed is in bytes
        
        # Display file details
        st.write(f"Text file {uploaded_file.name} uploaded successfully")

        # Save the encrypted data
        if st.button("Save Encrypted Data"):
            try:
                # Save the encrypted data as binary
                with open("encrypted_data.bin", "wb") as f:
                    f.write(encrypted_data)
                st.success("Encrypted data saved successfully as encrypted_data.bin")
            except Exception as e:
                st.error(f"Error saving file: {e}")

    # Check if encrypted_data is available before proceeding with embedding
    if encrypted_data is not None:
        # File uploader for image (for image-based steganography)
        uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
        if uploaded_image is not None:
            # Display image details
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
            
            # Embed encrypted data into image
            if st.button("Embed Data in Image"):
                output_path = os.path.join("output", f"embedded_{uploaded_image.name}")
                if not os.path.exists("output"):
                    os.makedirs("output")
                try:
                    embed_data_in_image(uploaded_image, encrypted_data, output_path)
                    st.success(f"Data embedded successfully in {output_path}")
                except Exception as e:
                    st.error(f"Error embedding data in image: {e}")

        # File uploader for audio (for audio-based steganography)
        uploaded_audio = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
        if uploaded_audio is not None:
            # Display audio file details
            st.write(f"Audio file {uploaded_audio.name} uploaded successfully")
            
            # Embed encrypted data into audio
            if st.button("Embed Data in Audio"):
                output_path = os.path.join("output", f"embedded_{uploaded_audio.name}")
                if not os.path.exists("output"):
                    os.makedirs("output")
                try:
                    embed_data_in_audio(uploaded_audio, encrypted_data, output_path)
                    st.success(f"Data embedded successfully in {output_path}")
                except Exception as e:
                    st.error(f"Error embedding data in audio: {e}")
    else:
        st.warning("Please upload and encrypt a text file first before embedding data.")
