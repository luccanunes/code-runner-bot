def getUserFiles(user):
    from pathlib import Path

    files = list()
    for path in Path("./files").iterdir():
        if path.stem == user and path.suffix != '.exe':
            files.append({'stem': path.stem, 'suffix': path.suffix})

    return files
