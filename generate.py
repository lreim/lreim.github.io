import os
import shutil

template = ""

with open('template.html', 'r', encoding='utf-8') as template_file:
    template = template_file.read()

def render_template(page_content):
    return template.format(page_content)

directory_path = 'pages/'
output_dir = 'build/'
resources_dir = 'resources/'

# Delete existing output directory and create a new, empty one.
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    output_file_path = os.path.join(output_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as page_file:
            content = page_file.read()
            complete_page = render_template(content)
            with open(output_file_path, 'x', encoding='utf-8') as output_file:
                output_file.write(complete_page)
        print(f'Rendered {file_path} to {output_file_path}')
    else:
        print(f'Error: found sub-directory {file_path}')



for filename in os.listdir(resources_dir):
    res_path = os.path.join(resources_dir, filename)
    build_path = os.path.join(output_dir, filename)
    if os.path.isfile(res_path):
        shutil.copy2(res_path, build_path)
