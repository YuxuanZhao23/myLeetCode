import os

def generate_hierarchy(directory, indent=''):
    content = ''
    for item in os.listdir(directory):
        if item == ".git":  # Skip .git directory
            continue
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            content += f"{indent}- 📁 {item}\n"
            content += generate_hierarchy(item_path, indent + '  ')
        else:
            content += f"{indent}- 📄 {item}\n"
    return content

def generate_readme(directory):
    readme_content = f"# Directory Structure\n\n{generate_hierarchy(directory)}"
    with open(os.path.join(directory, 'README.md'), 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    current_directory = os.getcwd()
    generate_readme(current_directory)
    print("README.md file generated successfully.")

