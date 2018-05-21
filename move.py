
import argparse
import os
import shutil
from glob import glob
from pathlib import Path

# N = 3  # the number of files in seach subfolder folder
N = 5  # ratio train/test samples


def move_files(abs_dirname):
    """Move files into subdirectories."""

    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]

    i = 0
    curr_subdir = None

    for f in files:
        if i % N == 0:
            subdir_name = os.path.join(abs_dirname, 'test\\')
            if not os.path.exists(subdir_name):
                os.mkdir(subdir_name)
            curr_subdir = subdir_name
        else:
            subdir_name = os.path.join(abs_dirname, 'train')
            if not os.path.exists(subdir_name):
                os.mkdir(subdir_name)
            curr_subdir = subdir_name

            # for f in files:
            #     # create new subdir if necessary
            #     if i % N == 0:
            #         subdir_name = os.path.join(abs_dirname, '{0:f}'.format(i / N + 1))
            #         os.mkdir(subdir_name)
            #         curr_subdir = subdir_name

        # move file to current dir
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(subdir_name, f_base))
        i += 1


def parse_args():
    """Parse command line arguments passed to script invocation."""
    parser = argparse.ArgumentParser(
        description='Split files into multiple subfolders.')

    parser.add_argument('src_dir', help='source directory')

    return parser.parse_args()


def get_all_subfoders(src_dir):
    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))
    list_of_dirs = glob(src_dir + "/*/")
    return list_of_dirs


# def get_basename(dir_name):
#     path = os.path.dirname(dir_name)
#     return os.path.basename(path)

def get_head(path):
    return str(Path(path).parent)

def rename_dir(old_dir_name, index):
    head = get_head(old_dir_name)
    new_name = head + "\\" + str(index)
    os.rename(old_dir_name, new_name)
    return new_name


def main():
    """Module's main entry point (zopectl.command)."""
    args = parse_args()
    src_dir = args.src_dir

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    move_files(os.path.abspath(src_dir))

def rename_folders(src_dir):
    for index, directory in enumerate(get_all_subfoders(src_dir)):
        print(rename_dir(os.path.dirname(directory), index))

if __name__ == '__main__':
    args = parse_args()
    src_dir = args.src_dir
    subfolders = get_all_subfoders(src_dir)
    parent = get_head(src_dir)

    subdir_name = os.path.join(parent, 'test\\')
    if not os.path.exists(subdir_name):
        os.mkdir(subdir_name)
    subdir_name = os.path.join(parent, 'train\\')
    if not os.path.exists(subdir_name):
        os.mkdir(subdir_name)

    for folder in subfolders:
        print(folder)
        # main()
