import os

def root_dir(*args):
    current_file_path = os.path.abspath(__file__)
    mod_dir = os.path.dirname(current_file_path)
    src_dir = os.path.dirname(mod_dir)
    root_dir_ = os.path.dirname(src_dir)
    if args:
        return os.path.join(root_dir_, *args)
    return root_dir_