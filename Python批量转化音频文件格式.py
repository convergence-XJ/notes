'''
要将多个.wma文件转换为.mp3文件，你可以使用pydub库来进行处理。以下是使用pydub库的示例代码，实现将指定路径下的所有.wma文件转换为.mp3格式：

首先，确保你已经安装了pydub库和ffmpeg库，可以使用以下命令来安装：

pip install moviepy
pip install ffmpeg-python
然后，使用以下Python代码来将指定路径下的所有.wma文件转换为.mp3格式：
'''

import os
from moviepy.editor import AudioFileClip

input_folder = r"D:\Music\MusicFormB站"
output_folder = r"D:\Music\MusicFormB站\mp3_output"

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历指定文件夹中的.wma文件并进行转换
for filename in os.listdir(input_folder):
    if filename.endswith(".wma"):
        wma_file_path = os.path.join(input_folder, filename)
        mp3_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

        # 使用moviepy进行格式转换
        audio_clip = AudioFileClip(wma_file_path)
        audio_clip.write_audiofile(mp3_file_path, codec='mp3')

print("转换完成！")

'''
在上述代码中，我们使用了moviepy库来处理WMA格式的音频文件。我们首先遍历指定文件夹中的文件，筛选出以.wma结尾的文件进行转换。对于每个.wma文件，我们使用AudioFileClip从.wma文件中读取音频，然后使用.write_audiofile将音频保存为.mp3文件。

运行这段代码后，所有的.wma文件将被转换为.mp3格式，并保存在指定的输出文件夹中。

'''