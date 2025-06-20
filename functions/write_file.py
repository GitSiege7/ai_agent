import os

def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    abs_path = os.path.join(abs_working_dir, file_path)

    if not os.path.abspath(os.path.join(working_dir, file_path)).startswith(abs_working_dir):
        return f"Error: {file_path} is outside working directory"

    try:
        fp = open(abs_path, mode="w")
    except:
        return f"Error: Failed to open '{abs_path}'"

    try:
        fp.write(content)
    except:
        return f"Failed to write to {abs_path}"

    fp.close()
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'