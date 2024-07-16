import os


def save(text, path, name, extension):
    if not extension:
        extension = ''
    else:
        extension = '.' + extension
    with open(os.path.join(path, name + extension), 'w') as f:
        f.write(text.encode('utf-8'))

