# app/utils/file_io.py
import os

def save_file(data, file_name):
    try:
        # Ensure the output directory exists
        if not os.path.exists("output"):
            os.makedirs("output")
        
        # Save the file with the given data
        file_path = os.path.join("output", file_name)
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"File saved successfully at {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
