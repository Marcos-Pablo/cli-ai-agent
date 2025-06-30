import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(abs_path, file_path))

        if not target_path.startswith(abs_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found'

        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        response = subprocess.run(
            f'python3 {target_path}',
            shell=True,
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
