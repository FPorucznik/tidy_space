import sys
import os
from pathlib import Path

TEXT_DOCS_FORMATS = ['.txt', '.rtf', '.doc', '.docx', '.pdf', '.csv', '.xml', '.html', '.json', '.yaml', '.md', '.tex',
                     '.log', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.epub', '.odp', '.ods', '.dot', '.dotx', '.xps']

AUDIO_FORMATS = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.aiff',
                 '.wma', '.mid', '.midi', '.amr', '.m4a', '.ac3', '.dts']

VIDEO_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv',
                 '.webm', '.mpeg', '.3gp', '.3g2', '.vob', '.rm', '.rmvb']

IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp',
                 '.tiff', '.svg', '.psd', '.eps', '.raw', '.ico', '.tga']

CODE_FORMATS = ['.c', '.cpp', '.cs', '.h', '.java', '.py',
                '.css', '.js', '.php', '.rb', '.swift', '.go', '.pl']

DB_FORMATS = ['.sql', '.mdb', '.sqlite', '.dbf', '.db', '.mdf']

CONFIG_FORMATS = ['.ini', '.cfg', '.toml', '.hcl', '.properties', '.yml']

COMPRESSED_FORMATS = ['.zip', '.rar', '.7z', '.tar',
                      '.gz', '.bz2', '.xz', '.tgz', '.z', '.lz']

FONT_FORMATS = ['.ttf', '.otf', '.woff', '.eot',
                '.ttc', '.pfa', '.pfb', '.afm', '.fon']

EXECUTABLE_FORMATS = ['.exe', '.app', '.apk', '.dmg',
                      '.msi', '.bin', '.bat', '.sh', '.jar', '.ipa']

ALL_FORMATS = TEXT_DOCS_FORMATS + AUDIO_FORMATS + VIDEO_FORMATS + IMAGE_FORMATS + CODE_FORMATS + \
    DB_FORMATS + CONFIG_FORMATS + COMPRESSED_FORMATS + FONT_FORMATS + EXECUTABLE_FORMATS


def run():
    try:
        path = os.path.join(sys.argv[1], '')
        if validate_path(path):
            organize_directory(path)
    except IndexError:
        print('No directory path provided. Example: python app.py C:\\example_directory\\')


def validate_path(path: str):
    isDirValid = os.path.isdir(path)
    if isDirValid:
        return isDirValid
    else:
        print(
            f'Not a valid path or the directory doesn\'t exist. Given path: {path}')
    return isDirValid


def organize_directory(path: str):
    dirName = os.path.basename(os.path.dirname(path))

    for file in os.listdir(path):
        extension = os.path.splitext(file)[1]

        if extension in ALL_FORMATS:
            match extension:
                case extension if extension in TEXT_DOCS_FORMATS:
                    new_dir = f'{path}{dirName}_text_doc_files'
                    move_file(path, new_dir, file)
                case extension if extension in AUDIO_FORMATS:
                    new_dir = f'{path}{dirName}_audio_files'
                    move_file(path, new_dir, file)
                case extension if extension in VIDEO_FORMATS:
                    new_dir = f'{path}{dirName}_video_files'
                    move_file(path, new_dir, file)
                case extension if extension in IMAGE_FORMATS:
                    new_dir = f'{path}{dirName}_image_files'
                    move_file(path, new_dir, file)
                case extension if extension in CODE_FORMATS:
                    new_dir = f'{path}{dirName}_code_files'
                    move_file(path, new_dir, file)
                case extension if extension in DB_FORMATS:
                    new_dir = f'{path}{dirName}_db_files'
                    move_file(path, new_dir, file)
                case extension if extension in CONFIG_FORMATS:
                    new_dir = f'{path}{dirName}_config_files'
                    move_file(path, new_dir, file)
                case extension if extension in COMPRESSED_FORMATS:
                    new_dir = f'{path}{dirName}_compressed_files'
                    move_file(path, new_dir, file)
                case extension if extension in FONT_FORMATS:
                    new_dir = f'{path}{dirName}_font_files'
                    move_file(path, new_dir, file)
                case extension if extension in EXECUTABLE_FORMATS:
                    new_dir = f'{path}{dirName}_executable_files'
                    move_file(path, new_dir, file)
        elif extension != '':
            new_dir = f'{path}{dirName}_other_files'
            move_file(path, new_dir, file)


def move_file(path: str, newDirPath: str, file: str):
    Path(newDirPath).mkdir(parents=True, exist_ok=True)

    original_file_location = os.path.join(path, file)
    new_file_location = os.path.join(newDirPath, '', file)
    Path(original_file_location).rename(new_file_location)


if __name__ == '__main__':
    run()
