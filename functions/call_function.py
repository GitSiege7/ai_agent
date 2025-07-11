from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file
from google.genai import types

def call_function(function_call_part, verbose=False):
    working_dir = "./calculator"
    
    func_names = {"get_files_info" : get_files_info,
                  "get_file_content" : get_file_content,
                  "run_python_file" : run_python_file,
                  "write_file" : write_file
                  }
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_call_part.name not in func_names:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    func = func_names[function_call_part.name]

    args = function_call_part.args.copy()
    args["working_dir"] = working_dir

    result = func(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )