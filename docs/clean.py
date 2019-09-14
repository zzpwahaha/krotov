#!/usr/bin/env docs
"""Clean the files generated by building the documentation"""
import shutil
from pathlib import Path


ROOT = Path(__file__).parent
BUILDDIR = '_build'

FILES_TO_DELETE = [
    ROOT / BUILDDIR,
    (ROOT / 'API', '*.rst'),
    (ROOT / 'notebooks', '*.log'),
    (ROOT, '**/.DS_Store'),
    ROOT / 'notebooks' / '.ipynb_checkpoints',
    ROOT / '_README.rst',
    ROOT / 'krotvscheme.aux',
    ROOT / 'krotvscheme.log',
    ROOT / 'oct_decision_tree.aux',
    ROOT / 'oct_decision_tree.log',
]


def main():
    """Main function"""
    for entry in FILES_TO_DELETE:
        if isinstance(entry, tuple):
            path, pattern = entry
            for file in path.glob(pattern):
                print("Remove file %s" % file)
                file.unlink()
        elif entry.is_file():
            print("Remove file %s" % entry)
            entry.unlink()
        elif entry.is_dir():
            print("Remove folder %s" % entry)
            shutil.rmtree(entry)


if __name__ == "__main__":
    main()
