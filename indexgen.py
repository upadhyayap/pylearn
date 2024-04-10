import os


def get_files_sorted_by_create_time(directory: str):
    files = []

    for f in os.listdir(directory):
        if not f.endswith(".py"):
            continue
        filepath = os.path.join(directory, f)
        if os.path.isfile(filepath):
            files.append((f, os.path.getctime(f)))

    sorted(files, key=lambda d: d[1])
    return files


def create_listing_file(files, indexfile: str):
    with open(indexfile, 'w') as out:
        for f in files:
            out.write(f[0] + '\n')


if __name__ == "__main__":
    path = os.getcwd()
    files = get_files_sorted_by_create_time(path)
    out = os.path.join(path, 'index.txt')
    create_listing_file(files, out)
    print("Generated index at %s" % out)
