# -*- coding: utf-8 -*-
from .utils.readonly_meta import ReadonlyMeta

from maya import cmds

class Const(metaclass=ReadonlyMeta):
    TOOL_NAME: str = 'ClearKnot'
    TOOL_TITLE: str = 'Clear Knot'
    TOOL_VERSION: str = '0.1.0'

    maya_major_ver = int(cmds.about(version=True))
    mayapy_exe_path = rf'C:\Program Files\Autodesk\Maya{maya_major_ver}\bin\mayapy.exe'
