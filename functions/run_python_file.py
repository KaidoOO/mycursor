import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        # Ensure full_path is within working_directory
        abs_working_directory = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        if not abs_full_path.startswith(abs_working_directory + os.sep):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check that the file exists and is a regular file
        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'
        if not os.path.isfile(abs_full_path):
            return f'Error: File "{file_path}" is not a regular file.'
        
        # Check that the file is a Python file (by extension)
        _, ext = os.path.splitext(abs_full_path)
        if ext.lower() != ".py":
            return f'Error: "{file_path}" is not a Python file.'
        
        result = subprocess.run(
            ["python3", abs_full_path] + args,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_directory
        )

        stdout = result.stdout or ""
        stderr = result.stderr or ""
        code = result.returncode

        parts = []
        if stdout:
            parts.append(f'STDOUT:\n{stdout}')
        if stderr:
            parts.append(f'STDERR:\n{stderr}')
        if code != 0:
            parts.append(f'Process exited with code {code}')

        if not parts:
            return 'No output produced.'

        return "\n\n".join(parts)
        # except subprocess.TimeoutExpired:
        # return 'Error: Execution timed out'
    except Exception as e:
        return f"Error: executing Python file: {e}"
