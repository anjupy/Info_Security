# app/steganography/audio_stegano.py
import wave
import os

def embed_data_in_audio(uploaded_audio, data, output_path):
    try:
        # Read the audio data from the uploaded file
        audio_data = uploaded_audio.getvalue()

        # Open the audio file (assuming it's a WAV file)
        with wave.open(uploaded_audio, 'rb') as audio_file:
            params = audio_file.getparams()
            frames = audio_file.readframes(params.nframes)

        # Convert the frames into a mutable bytearray for manipulation
        frame_bytes = bytearray(frames)

        # Convert the encrypted data into binary format (8-bit)
        binary_data = ''.join(format(byte, '08b') for byte in data)  # No need to encode

        # Embed the binary data into the least significant bits (LSBs) of the audio frames
        data_index = 0
        for i in range(len(frame_bytes)):
            if data_index < len(binary_data):
                # Change the LSB of each byte in the frame to match the binary data
                frame_bytes[i] = (frame_bytes[i] & 0xFE) | int(binary_data[data_index])
                data_index += 1
            if data_index >= len(binary_data):
                break

        # Save the modified audio back to the output path
        with wave.open(output_path, 'wb') as output_audio:
            output_audio.setparams(params)
            output_audio.writeframes(bytes(frame_bytes))

        print(f"Embedded data successfully saved to {output_path}")

    except Exception as e:
        print(f"Error embedding data in audio: {e}")
