# -*- coding: utf-8 -*-
import subprocess
from typing import List, Tuple, Any

from .readonly_meta import ReadonlyMeta


class SubprocessWrapper(metaclass=ReadonlyMeta):
    @staticmethod
    def run(cmd: List[str]) -> Tuple[Any, bool]:
        cp: subprocess.CompletedProcess = subprocess.run(cmd, capture_output=True, text=True)
        if cp.returncode == 0:
            return cp.stdout, True
        else:
            print(cp.stderr)
            return None, False
