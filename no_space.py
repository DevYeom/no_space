#!/usr/bin/env python
"""
no_space is NOT The North Face
Usage: python no_space.py /Users/foo
"""

import os
import sys

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        if not os.path.exists(path):
            print("File not found: %s" % sys.argv[1])
            sys.exit(1)
    else:
        print("Invalid arguments.\nUsage: python no_space.py /Users/foo/project")
        sys.exit(1)
    no_space(path)

def no_space(path):
    print("\nPATH ::: %s" % path)
    print("\n********************Start********************\n")
    count = 0
    for path, _, files in os.walk(path):
        for f in files:
            file_name, file_extension = os.path.splitext(f)
            if file_extension == '.swift':
                path_name = os.path.join(path, f)
                with open(path_name, 'r') as fr:
                    new = [line.rstrip() for line in fr]
                with open(path_name, 'w') as fw:
                    fw.writelines((line + '\n' for line in new))
            count += 1
            print("Remove trailing whitespaces! >> %s" % file_name)
    print("\nTotal: %d" % count)
    print("\n********************End********************\n")

if __name__ == "__main__":
    main()
