import os
from config import READ_FILE_LIMIT

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
