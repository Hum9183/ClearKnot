# -*- coding: utf-8 -*-
from .utils.readonly_meta import ReadonlyMeta


class Const(metaclass=ReadonlyMeta):
    TOOL_NAME: str = 'ClearKnot'
    TOOL_TITLE: str = 'Clear Knot'
