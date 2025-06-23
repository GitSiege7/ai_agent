import os

def get_files_info(working_dir, dir=None):
    abs_working_dir = os.path.abspath(working_dir)
    
    if dir:
        abs_dir = os.path.join(abs_working_dir, dir)
    else:
        abs_dir = abs_working_dir
    
    if not abs_dir.startswith(abs_working_dir) or dir == "../":
        return f'Error: Cannot list "{dir}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_dir):
        return f'Error: "{dir}" is not a directory'
    
    try:
        contents = os.listdir(abs_dir)
    except:
        return f"Failed to list directories at '{abs_dir}'"

    files = []
    for item in contents:
        item_dir = os.path.join(abs_dir, item)
        
        files.append(f"- {item}: file_size={os.path.getsize(item_dir)} bytes, is_dir={os.path.isdir(item_dir)}")

    return "\n".join(files)