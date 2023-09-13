import os

def replace_main_in_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content.replace('int main(int argc, char * argv[])', 'int main()')
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.c'):
            replace_main_in_file(filename)

if __name__ == '__main__':
    main()
