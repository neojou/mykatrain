import heapq
import math
import os
import random
import struct
import sys
from typing import List, Tuple, TypeVar

import importlib.resources as pkg_resources

PATHS = {}

def find_package_resource(path, silent_erros=False):
    global PATHS
    if path.startswith("mylittlego"):
        if not PATHS.get("PACKAGE"):
            try:
                with pkg_resources.path("mylittlego", "gui.kv") as p:
                    PATHS["PACKAGE"] = os.path.split(str(p))[0]
            except (ModuleNotFoundError, FileNotFoundError, ValueError) as e:
                print(f"Package path not found, installation possibly broken. Error: {e}", file=sys.stderr)
        return os.path.join(PATHS["PACKAGE"], path.replace("mylittlego\\", "mylittlego/").replace("mylittlego/", ""))
    else:
        return os.path.abspath(os.path.expanduser(path))

