# -*- coding: utf-8 -*-

import os
import subprocess

def convert_video_to_mp4(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-hwaccel', 'cuda',  # 使用CUDA进行GPU加速
        '-i', input_file,
        '-c:v', 'h264_nvenc',  # 使用NVIDIA的H.264编码器进行加速
        '-preset', 'slow',  # 使用较慢的预设以获取更好的质量
        '-crf', '18',  # 控制视频质量，值越小质量越高，但文件大小也会增加
        '-c:a', 'aac',  # 使用AAC音频编码
        '-b:a', '192k',  # 音频比特率
        '-movflags', '+faststart',  # 优化视频以逐行播放
        output_file
    ]

    subprocess.run(ffmpeg_cmd)

def convert_video_files_in_directory(input_directory, output_directory):
    # 递归遍历目录下的所有视频文件
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            input_file = os.path.join(root, file)

            # 构建输出路径
            relative_path = os.path.relpath(input_file, input_directory)
            output_file = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".mp4")

            # 创建输出目录
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            # 执行转换
            convert_video_to_mp4(input_file, output_file)

# 示例用法
input_directory = r'输入目录'
output_directory = r'输出目录'
convert_video_files_in_directory(input_directory, output_directory)
