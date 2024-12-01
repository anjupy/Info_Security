import os
from app.steganography.audio_stegano import embed_data_in_audio, extract_data_from_audio

def test_audio_stegano(tmpdir):
    input_audio = "tests/test_audio.wav"
    output_audio = os.path.join(tmpdir, "output_audio.wav")
    test_data = "Secret message"
    
    embed_data_in_audio(input_audio, test_data.encode(), output_audio)
    extracted_data = extract_data_from_audio(output_audio)
    
    assert extracted_data.strip() == test_data
