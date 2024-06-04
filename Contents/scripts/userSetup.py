# -*- coding: utf-8 -*-
import traceback
from textwrap import dedent

from maya import cmds


def __register_clearknot_startup():
    # TODO: Py2の場合は「Not Supported」みたいなmenuitemを追加するようにする
    cmd = dedent(
        """
        import clearknot.startup
        clearknot.startup.main()
        """)
    cmds.evalDeferred(cmd)


if __name__ == '__main__':
    try:
        __register_clearknot_startup()

    except Exception:
        traceback.print_exc()
