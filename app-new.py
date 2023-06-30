# -*- coding: utf-8 -*-

import os
import subprocess

def convert_video_to_mp4(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-hwaccel', 'cuda',  # ʹ��CUDA����GPU����
        '-i', input_file,
        '-c:v', 'h264_nvenc',  # ʹ��NVIDIA��H.264���������м���
        '-preset', 'slow',  # ʹ�ý�����Ԥ���Ի�ȡ���õ�����
        '-crf', '18',  # ������Ƶ������ֵԽС����Խ�ߣ����ļ���СҲ������
        '-c:a', 'aac',  # ʹ��AAC��Ƶ����
        '-b:a', '192k',  # ��Ƶ������
        '-movflags', '+faststart',  # �Ż���Ƶ�����в���
        output_file
    ]

    subprocess.run(ffmpeg_cmd)

def convert_video_files_in_directory(input_directory, output_directory):
    # �ݹ����Ŀ¼�µ�������Ƶ�ļ�
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            input_file = os.path.join(root, file)

            # �������·��
            relative_path = os.path.relpath(input_file, input_directory)
            output_file = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".mp4")

            # �������Ŀ¼
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            # ִ��ת��
            convert_video_to_mp4(input_file, output_file)

# ʾ���÷�
input_directory = r'����Ŀ¼'
output_directory = r'���Ŀ¼'
convert_video_files_in_directory(input_directory, output_directory)
