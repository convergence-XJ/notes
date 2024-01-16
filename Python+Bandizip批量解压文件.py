'''
下面的代码将

“D:\Compressed” 里面的压缩包批量进行解压到  “D:\Unzip file”目录下。
'''


import os
import subprocess

def unzip_file(file_path, output_folder):
    # Specify the Bandizip command-line tool path
    bandizip_path = r'C:\Program Files\Bandizip\Bandizip.exe'  # Update this path to match your system

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use Bandizip to extract the file to the specified output folder
    subprocess.run([bandizip_path, 'x', f'-o:{output_folder}', file_path])

def batch_unzip(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)
            target_folder = os.path.join(output_folder, file_name)

            if file_extension.lower() in ('.rar', '.zip', '.7z'):
                unzip_file(file_path, target_folder)

if __name__ == "__main__":
    input_folder = r"D:\Compressed"
    output_folder = r"D:\Unzip file"
    batch_unzip(input_folder, output_folder)

'''
下面提供bandizip的可执行文件，方便日后查阅（蓝奏云链接）

https://wwwr.lanzoul.com/iy02c04seeja
密码:1gmz 
'''