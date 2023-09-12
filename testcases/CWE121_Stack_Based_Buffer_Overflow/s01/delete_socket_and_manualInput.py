def contains_keywords(line, keywords):
    return any(keyword in line for keyword in keywords)

keywords = ["socket", "fscanf", "fgets"]

# 定义一个函数来删除包含 "socket" 的行
def remove_specific_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # 删除包含 "socket" 的行
    new_lines = [line for line in lines if not contains_keywords(line, keywords)]

    with open(output_file, 'w') as outfile:
        outfile.writelines(new_lines)

# 使用函数
if __name__ == "__main__":
    input_file = "main_linux.cpp"  # 替换为你的输入文件名
    output_file = "new_main_linux.cpp"  # 替换为你的输出文件名
    remove_specific_lines(input_file, output_file)
