import os
import fnmatch


def find_music(root, file_extension="emp3"):
    for path, _, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(file_extension)):
            yield os.path.join(path, file)
            # print(os.path.abspath(song))
    # yield song_name


file_list = find_music("music")

for s in file_list:
    print(s)
