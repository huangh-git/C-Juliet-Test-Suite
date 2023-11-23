import os

def replace_main_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content.replace('int main(int argc, char * argv[])', 'int main()')
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)

def main():
    for subdir, _, files in os.walk('.'):
        for filename in files:
            # print(filename)
            if filename.endswith('.c'):
                file_path = os.path.join(subdir, filename)
                replace_main_in_file(file_path)

if __name__ == '__main__':
    main()
