import os
def write_example_file(file_path,file_name):
    import os
    full_path = os.path.join(os.getcwd(), file_name)
    content = "Hello World!\nHello Python!"

    try:
        with open(full_path,'w',encoding='utf-8') as f:
            f.write(content)
        print(f"已成功创建并写入:{full_path}")
        print(f"写入：{content}")
    except Exception as e:
        print(f"创建文件时发生错误：{e}")

if __name__ == "__main__":
    current_path =os.getcwd()
    current_file_name = "example1.txt"
    write_example_file(current_path,current_file_name)