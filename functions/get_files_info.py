def get_files_info(working_directory, directory="."):
    true_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(true_path, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not directory:
        return f'Error: "{directory}" is not a directory'
    
    files = os.listdir(target_dir)
    lines = []
    for filename in files:
        full_path = os.path.join(target_dir, filename)
        dir_check = os.path.isdir(full_path)
        size = os.path.getsize(full_path)
        line = f"- {filename}: file_size={size} bytes, is_dir={dir_check}"
        lines.append(line)
    
    result = "\n".join(lines)

    return result 
        

        
