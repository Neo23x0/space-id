#!/usr/bin/env python3.6

__AUTHOR__ = 'Florian Roth'
__VERSION__ = "0.1.0 June 2018"

import sys
import os
import argparse
import traceback


def write_id(target_file, id, preamble):
    """
    Appends a space ID to the file
    :param target_file:
    :param id:
    :return:
    """
    print("Writing Space ID to file '%s'" % target_file)
    space_id = generate_space_id(id)
    try:
        with open(target_file, "a") as fh:
            fh.write(preamble)
            fh.write(space_id)
    except IOError:
        traceback.print_exc()


def read_id(source_file, preamble):
    """
    Reads a space ID from a file
    :param source_file:
    :return:
    """
    try:
        with open(source_file, "r") as fh:
            data = fh.read()
        pos = data.find(preamble)
        if pos > 0:
            print("[+] Preamble found at %d" % pos)
            space_id = data[(pos + len(preamble)):]
            id = translate_space_id(space_id)
            print("SPACE ID: %s" % id)
        else:
            print("[-] No preamble found in file")
        # Process the lines
    except IOError:
        traceback.print_exc()


def remove_id(source_file, preamble):
    """
    Reads a space ID from a file
    :param source_file:
    :return:
    """
    try:
        with open(source_file, "r") as fh:
            data = fh.read()
        pos = data.find(preamble)
        if pos > 0:
            print("[+] Preamble found at %d" % pos)
            data_clean = data[:pos]
            with open(source_file, "w") as fh:
                fh.write(data_clean)
            print("[+] Space ID successfully removed")
        else:
            print("[-] No preamble found in file")
        # Process the lines
    except IOError:
        traceback.print_exc()


def generate_space_id(id):
    """
    Generates an id encoded in space values
    :param id:
    :return space_id:
    """
    space_id = ""
    for i in id:
        num = ord(i)
        space_id += "%s\n" % (' ' * num)
    if args.debug:
        print("SPACE ID:")
        print(space_id.replace(" ", "*"))
    return space_id


def translate_space_id(space_id):
    """
    Translates a space id to an ID
    :param space_id:
    :return id:
    """
    id = ""
    lines = space_id.splitlines()
    for line in lines:
        char = chr(len(line))
        id += char
    return id


if __name__ == '__main__':
    print("     ____                    _______  ".ljust(80))
    print("    / __/__  ___ ________   /  _/ _ \ ".ljust(80))
    print("   _\ \/ _ \/ _ `/ __/ -_) _/ // // / ".ljust(80))
    print("  /___/ .__/\_,_/\__/\__/ /___/____/  ".ljust(80))
    print("     /_/                              ".ljust(80))
    print(" ".ljust(80))
    print("  Invisible Watermarks with Space Characters".ljust(80))
    print("  v0.1, June 2018, Florian Roth".ljust(80))
    print(" ".ljust(80))

    parser = argparse.ArgumentParser(description='Online Hash Checker')
    parser.add_argument('-f', help='File to ID (if used with -i it writes the ID to the file)',
                        metavar='path', default='')
    parser.add_argument('-i', help='ID (writes ID to file)', metavar='path', default='')
    parser.add_argument('-p', help='Preamble to start the space ID with', metavar='path',
                        default="\n \n  \n   \n")
    parser.add_argument('--remove', action='store_true', default=False, help='Remove space ID')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug output')

    args = parser.parse_args()

    # File not found
    if not args.f:
        print("You have to set a target file with -f")
        sys.exit(1)
    if not os.path.exists(args.f):
        print("Cannot find target file '%s" % args.f)
        sys.exit(1)

    # Remove Space ID
    if args.remove:
        remove_id(args.f, args.p)
    # Write ID to file
    elif args.i:
        write_id(args.f, args.i, args.p)
    # Read ID from file
    else:
        read_id(args.f, args.p)