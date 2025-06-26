import os

def get_files_info(working_directory, directory=None):
    try:
        abs_work_dir = os.path.abspath(working_directory)
        target_dir = abs_work_dir

        if directory:
            target_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not target_dir.startswith(abs_work_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        files_info = []

        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            files_info.append(f'- {item}: file_size={item_size} bytes, is_dir={is_dir}')
        return "\n".join(files_info)
    except Exception as e:
        return f'Error listing files: {e}'
