#!/usr/bin/env python3

import sys


def parse(libtool_version_info: str, system: str) -> str:
    cur, rev, age = map(int, libtool_version_info.split(':'))
    if system in ['hpux', 'netbsd', 'openbsd', 'sunos']:
        components = [cur, rev]
    elif system == 'qnx':
        components = [cur]
    else:
        components = [cur - age, age, rev]
    return ".".join(map(str, components))


if __name__ == '__main__':
    libtool_version_info, system = sys.argv[1:]
    meson_version_info = parse(libtool_version_info, system)
    print(meson_version_info)
