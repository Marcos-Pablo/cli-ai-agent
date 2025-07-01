import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(abs_path, file_path))

        if not target_path.startswith(abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path, 'r') as file:
            suffix = ''
            if os.path.getsize(target_path) > MAX_CHARS:
                suffix = '\n[...File "{file_path}" truncated at 10000 characters]'
            file_content = file.read(MAX_CHARS) + suffix

        return file_content
    except Exception as error:
        return f'Error: {error}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
