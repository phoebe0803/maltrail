#!/usr/bin/env python

"""
Copyright (c) 2014-2018 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content

__url__ = "http://cybersweat.shop/iprep/iprep_ramnode.txt"
__check__ = ".1"
__info__ = "known attacker"
__reference__ = "cybersweat.shop"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[line.split(';')[0].strip()] = (__info__, __reference__)

    return retval
