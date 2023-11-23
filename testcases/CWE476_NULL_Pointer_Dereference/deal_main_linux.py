import os

def contains_keywords(line, keywords):
    return any(keyword in line for keyword in keywords)

keywords = ["socket", "fscanf", "fgets"]

# 定义一个函数来删除包含 "socket" 的行
def remove_specific_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # 删除包含 "socket" 的行
    new_lines = [line for line in lines if not contains_keywords(line, keywords)]

    if 'void _start() {\n' not in new_lines:
        new_lines.append('\nvoid _start() {\n')
        new_lines.append('\tmain(0, NULL);\n')
        new_lines.append('}\n')

    with open(output_file, 'w') as outfile:
        outfile.writelines(new_lines)

# 使用函数
if __name__ == "__main__":
    # for subdir, _, _ in os.walk('.'):
    #     if subdir == '.':
    #         continue
    #     input_file = os.path.join(subdir, "main_linux.cpp")  # 替换为你的输入文件名
    #     output_file = os.path.join(subdir, "new_main_linux.cpp")  # 替换为你的输出文件名
    remove_specific_lines("main_linux.cpp", "new_main_linux.cpp")
