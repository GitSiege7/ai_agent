import os
MAX_CHARS = 10000

def get_file_content(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir)
    abs_path = os.path.join(abs_working_dir, file_path)
    
    if not os.path.exists(abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        fp = open(abs_path, mode="r")
    except:
        return f"Error: Opening '{abs_path}' for reading failed."
    
    try:
        content = fp.read(MAX_CHARS)
    except:
        return f"Error: Failed to read file pointer to '{abs_path}'"
    
    if len(content) == MAX_CHARS:
        content += f"[...File '{abs_path}' truncated at 10000 characters]"

    fp.close()

    return content