import os
import glob
import re

def convert_html_to_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        full_block_regex = r'(<center>\s*<figure markdown>\s*<img[^>]+src="([^"]+)"[^>]*>\s*</figure>\s*</center>)'
        full_block_match = re.search(full_block_regex, html_content)

        if full_block_match:
            img_url = full_block_match.group(2)
            markdown_replacement = f"<figure markdown>\n  ![Logo]({img_url}){{ width=\"100\", height=\"100\" }}\n</figure>"
            html_content = re.sub(full_block_regex, markdown_replacement, html_content)

            # Rewrite the file with the converted content
            with open(file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(html_content)

            return f"Conversion successful for {file_path}."
        else:
            return f"No matching HTML block found in {file_path}."

    except FileNotFoundError:
        return f"File {file_path} not found."

def convert_all_readme_files_in_repo(start_directory):
    exclude_dirs = set(['node_modules', 'vendor'])

    for root, dirs, files in os.walk(start_directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file == '*.md':
                file_path = os.path.join(root, file)
                result = convert_html_to_markdown(file_path)
                print(result)

# Starting directory - adjust as needed
start_directory = './docs/'

convert_all_readme_files_in_repo(start_directory)
