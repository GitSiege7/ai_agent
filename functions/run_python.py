import os
import subprocess

def run_python_file(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir)
    abs_path = os.path.abspath(os.path.join(working_dir, file_path))
    
    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    split = file_path.split("/")
    if split[-1][-2:] != "py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        output = subprocess.run(["python3", f"{abs_path}"], capture_output=True, timeout=30)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if output.stdout == None:
        return "No output produced"
    elif output.returncode != 0:
        return f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}\nProcess exited with code {output.returncode}"
    else:
        return f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}"