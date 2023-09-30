import os
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_data = file.read()

    # 使用正则表达式替换特定文本
    new_data = re.sub(r'data\s*=\s*RAND32\(\);', 'data = RAND32()%20;', file_data)

    # 如果文件内容发生变化，则写回文件
    if new_data != file_data:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_data)

def main():
    # 遍历当前目录及其所有子目录
    for root_dir, _, files in os.walk('.'):
        for file_name in files:
            # 检查文件名是否符合条件
            if file_name.endswith('.c') and 'rand' in file_name.lower():
                file_path = os.path.join(root_dir, file_name)
                process_file(file_path)

if __name__ == '__main__':
    main()
