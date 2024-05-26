# -*- coding: utf-8 -*-
import json
import os
import shutil
import subprocess
from typing import Optional

from maya import cmds

try:
    from PySide6.QtCore import QStringListModel
    from PySide6.QtWidgets import QInputDialog
except ImportError:
    from PySide2.QtCore import QStringListModel
    from PySide2.QtWidgets import QInputDialog

from .const import Const
from .utils import pip_util, str_util
from .utils.clearknot_error import ClearKnotError
from .utils.subprocess_wrapper import SubprocessWrapper


m = '-m'
pip = 'pip'
freeze = 'freeze'
user = '--user'
numpy = 'numpy'
target = '--target'
yes = '--yes'
path1 = r'C:\Users\jiang\OneDrive'
path2 = rf'maya\{Const.maya_major_ver}\ja_JP\scripts\site-packages'
document = 'ドキュメント'
path = f'{path1}/{document}/{path2}'

clearknot_temp = 'clearknot-temp'
path_ = rf'C:\{clearknot_temp}'


@ClearKnotError.catch
def add(string_list_model :QStringListModel):
    input_text, success = QInputDialog.getText(
        None,
        'Input Dialog',
        'Please enter the PyPI package name.'
    )
    if success is False:
        return
    if input_text == str_util.EMPTY:
        return

    installed = pip_util.freeze()
    if input_text in installed:
        raise ClearKnotError('すでにインストールされています')

    install_cmd = [Const.mayapy_exe_path, m, pip, 'install', user, input_text]
    _, success = SubprocessWrapper.run(install_cmd)
    if success:
        print(f'{input_text}をインストールしました')
    else:
        print(f'{input_text}のインストールに失敗しました')

    pip_util.set_installed(string_list_model)

    # 基本的にユーザスペースにpipでインストールする方針
    # 現状はpip(PyPI)とGitリポジトリの両方に対応している
    # 管理しやすくするために両者のディレクトリを分けたいが、
    # mayapy.exeのシンタックスハイライトが効かなくなるため、両者ともユーザスペースに入れている
    # 直接Explorerで操作せずにGUIで操作する前提なら、これでも良いと思う

    # TODO: ユーザスペースにgitリポジトリを入れる処理を書く
    # TODO: pipでgitでインストールできるらしい
    # TODO: clearknot.pthの自動生成処理

@ClearKnotError.catch
def remove(string_list_model :QStringListModel):
    input_text, success = QInputDialog.getText(
        None,
        'Input Dialog',
        'Please enter the PyPI package name to uninstall'
    )
    if success is False:
        return
    if input_text == str_util.EMPTY:
        return

    installed = pip_util.freeze()
    if (input_text in installed) is False:
        raise ClearKnotError(f'{input_text}がインストールされていません')

    uninstall_cmd = [Const.mayapy_exe_path, m, pip, 'uninstall', yes, input_text]
    _, success = SubprocessWrapper.run(uninstall_cmd)
    if success:
        print(f'{input_text}をアンインストールしました')
    else:
        print(f'{input_text}のアンインストールに失敗しました')

    pip_util.set_installed(string_list_model)
