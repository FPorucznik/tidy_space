import sys
import os
from pathlib import Path

TEXT_DOCS_FORMATS = ['.txt', '.rtf', '.doc', '.docx', '.pdf', '.csv', '.xml', '.html', '.json', '.yaml', '.md', '.tex',
                     '.log', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.epub', '.odp', '.dot', '.dotx', '.xps']

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


def organize_directory(path: str):
    pass


def validate_path(path: str):
    isDirValid = os.path.isdir(path)
    if isDirValid:
        return isDirValid
    else:
        print(
            f'Not a valid path or the directory doesn\'t exist. Given path: {path}')
    return isDirValid


def app():
    try:
        path = os.path.join(sys.argv[1], '')
        if validate_path(path):
            organize_directory(path)
    except IndexError:
        print('No directory path provided. Example: python app.py C:\\example_directory\\')


if __name__ == '__main__':
    app()
