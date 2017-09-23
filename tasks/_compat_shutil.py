# -*- coding: UTF-8 -*-
# PYTHON VERSION COMPATIBILITY HELPER

try:
    from shutil import which    # -- SINCE: Python 3.3
except ImportError:
    from backports.shutil_which import which
