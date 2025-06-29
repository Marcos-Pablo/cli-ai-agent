import os
from config import MAX_CHARS

def get_files_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(abs_path, file_path))

        if not target_path.startswith(abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path, "r") as file:
            suffix = ''
            if os.path.getsize(target_path) > MAX_CHARS:
                suffix = '\n[...File "{file_path}" truncated at 10000 characters]'
            file_content = file.read(MAX_CHARS) + suffix

        return file_content
    except Exception as error:
        return f'Error: {error}'
