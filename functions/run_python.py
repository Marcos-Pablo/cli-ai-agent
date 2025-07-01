import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(abs_path, file_path))

        if not target_path.startswith(abs_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found'

        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        commands = ["python3", target_path]
        if args:
            commands.extend(args)

        response = subprocess.run(
            commands,
            cwd=working_directory,
            timeout=30,
            capture_output=True,
            text=True
        )

        if not response.stdout and not response.stderr:
            return 'No output produced.'

        output = []
        if response.stdout:
            output.append(f'STDOUT: {response.stdout}')
        if response.stderr:
            output.append(f'STDERR: {response.stderr}')
        if response.returncode != 0:
            output.append(f'Process exited with code {response.returncode}')

        return "\n".join(output)
    except Exception as error:
        return f'Error: executing Python file: {error}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
