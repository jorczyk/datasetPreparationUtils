
import argparse
import os
import shutil
from glob import glob
from pathlib import Path
import time

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

def get_head(path):
    return str(Path(path).parent)

def rename_dir(old_dir_name, index):
    head = get_head(old_dir_name)
    new_name = head + "\\" + str(index)
    if not os.path.exists(new_name):
        os.rename(old_dir_name, new_name)
    return new_name

def rename_folders(src_dir):
    for index, directory in enumerate(get_all_subfoders(src_dir)):
        print("renaming folder " + rename_dir(os.path.dirname(directory), index))

def split_train_test_sets(src_dir):
    N = 5  # ratio train/test samples

    rename_folders(src_dir)
    print('~~RENAMING DONE~~')
    subfolders = get_all_subfoders(src_dir)
    parent = get_head(src_dir)

    subdir_test_name = os.path.join(parent, 'test\\')
    if not os.path.exists(subdir_test_name):
        os.mkdir(subdir_test_name)
        print(subdir_test_name + " folder created")
    subdir_train_name = os.path.join(parent, 'train\\')
    if not os.path.exists(subdir_train_name):
        os.mkdir(subdir_train_name)
        print(subdir_train_name + " folder created")

    print("~~DONE CREATING TRAIN/TEST FOLDERS")

    i = 1
    for folder in subfolders:
        # print(folder)
        files = [os.path.join(folder, f) for f in os.listdir(folder)]
        for file in files:
            f_base = os.path.basename(file)
            item = os.path.basename(get_head(file))
            if i % N == 0:
                target_dir = subdir_test_name
            else:
                target_dir = subdir_train_name

            target = target_dir + item + '\\'
            if not os.path.exists(target):
                print("creating folder: " + target)
                os.mkdir(target_dir + item + '\\')

            if not os.path.isfile(target + f_base):
                try:
                    shutil.copy(file, target + f_base)
                except:
                    raise IOError('An error occured')
                print('\"' + file + '\"' + " -> " + '\"' + target + f_base + '\"' + " copy done")
            i += 1
    print("~~DONE SUCCESFULLY~~")

def main():
    args = parse_args()
    src_dir = args.src_dir

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    split_train_test_sets(os.path.abspath(src_dir))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds elapsed ---" % (time.time() - start_time))
