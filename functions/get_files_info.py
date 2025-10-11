import os
from config import READ_FILE_LIMIT

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        # Ensure full_path is within working_directory
        abs_working_directory = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        if not abs_full_path.startswith(abs_working_directory + os.sep) and abs_full_path != abs_working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for entry in os.listdir(abs_full_path):
            entry_path = os.path.join(abs_full_path, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path)
            entries.append(f'- {entry}: file_size={file_size} bytes, is_dir={is_dir}')
        return "\n".join(entries)
    except Exception as e:
        return f'Error: {str(e)}'
    
def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        # Ensure full_path is within working_directory
        abs_working_directory = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        if not abs_full_path.startswith(abs_working_directory + os.sep):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_full_path, "r", encoding="utf-8") as f:
            content = f.read()
            if len(content) > READ_FILE_LIMIT:
                truncated_content = content[:READ_FILE_LIMIT] + f'\n[...File "{file_path}" truncated at {READ_FILE_LIMIT} characters]'
            else:
                return content
            return truncated_content
    except Exception as e:
        return f'Error: {str(e)}'
    
def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        # Ensure full_path is within working_directory
        abs_working_directory = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        if not abs_full_path.startswith(abs_working_directory + os.sep):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        dir_name = os.path.dirname(abs_full_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(abs_full_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'