# -*- coding: utf-8 -*-
import inspect
from textwrap import dedent

from maya import cmds
from maya import OpenMayaUI as omui

from PySide2.QtWidgets import QApplication, QWidget
import shiboken2

from .main_commands import restore_command
from .window import ClearKnotMainWindow


def restart() -> None:
    """開発用(再起動用)"""
    if omui.MQtUtil.findControl(ClearKnotMainWindow.name):
        cmds.deleteUI(ClearKnotMainWindow.workspace_control, control=True)

    win = __create_window()
    cmd = dedent(inspect.getsource(restore_command))
    win.show(dockable=True, uiScript=cmd)


def restore() -> None:
    ClearKnotMainWindow.restored_instance = __create_window()  # WARNING: GCに破棄されないようにクラス変数に保存しておく
    ptr = omui.MQtUtil.findControl(ClearKnotMainWindow.name)
    restored_control = omui.MQtUtil.getCurrentParent()
    omui.MQtUtil.addWidgetToMayaLayout(int(ptr), int(restored_control))


def startup() -> None:
    ptr = omui.MQtUtil.findControl(ClearKnotMainWindow.name)

    if ptr:
        win = shiboken2.wrapInstance(int(ptr), QWidget)
        if win.isVisible():
            win.show()  # NOTE: show()することで再フォーカスする
        else:
            win.setVisible(True)
    else:
        win = __create_window()
        cmd = dedent(inspect.getsource(restore_command))

        # 空のWindowが生成されてしまった場合
        if cmds.workspaceControl(ClearKnotMainWindow.workspace_control, q=True, exists=True):
            # 既存のWorkspaceControlを一旦削除する
            cmds.deleteUI(ClearKnotMainWindow.workspace_control, control=True)

        win.show(dockable=True, uiScript=cmd)


def __create_window() -> ClearKnotMainWindow:
    app = QApplication.instance()
    win = ClearKnotMainWindow()
    win.init()
    win.init_gui()
    return win
