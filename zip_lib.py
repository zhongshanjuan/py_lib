import zipfile
import os
import datetime

def zipdir(path, ziph):
    # 打包整个文件夹
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    # 指定要压缩的文件夹路径和zip文件名
    current_date = datetime.date.today().strftime('%Y-%m-%d')
    zipf = zipfile.ZipFile(f'venv-{current_date}.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./venv', zipf)
    zipf.close()
    