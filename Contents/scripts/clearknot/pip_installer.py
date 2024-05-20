# -*- coding: utf-8 -*-
import json
import os
import shutil
import subprocess
from typing import Optional

from maya import cmds

maya_major_ver = int(cmds.about(version=True))
mayapy_exe = rf'C:\Program Files\Autodesk\Maya{maya_major_ver}\bin\mayapy.exe'
m = '-m'
pip = 'pip'
user = '--user'
numpy = 'numpy'
target = '--target'
path1 = r'C:\Users\jiang\OneDrive'
path2 = rf'maya\{maya_major_ver}\ja_JP\scripts\site-packages'
document = 'ドキュメント'
path = f'{path1}/{document}/{path2}'

clearknot_temp = 'clearknot-temp'
path_ = rf'C:\{clearknot_temp}'

# def install():
#     print('GO!!!')
#     # clearknot-tempに仮でinstall
#     clone_cmd = [mayapy_exe, m, pip, 'install', numpy, target, path_]
#     print(clone_cmd)
#     cp: subprocess.CompletedProcess = subprocess.run(clone_cmd, capture_output=True)
#     print("returncode: ", cp.returncode)
#     print("stderr: ", cp.stderr)
#     print("stdout: ", cp.stdout)
#
#     # mayaのパスにコピー
#     shutil.copytree(path_, path, dirs_exist_ok=True)


def install():
    print('GO!!!')
    clone_cmd = [mayapy_exe, m, pip, 'install', user, numpy]
    print(clone_cmd)
    cp: subprocess.CompletedProcess = subprocess.run(clone_cmd, capture_output=True)
    print("returncode: ", cp.returncode)
    print("stderr: ", cp.stderr)
    print("stdout: ", cp.stdout)

    # 基本的にユーザスペースにpipでインストールする方針
    # 現状はpip(PyPI)とGitリポジトリの両方に対応している
    # 管理しやすくするために両者のディレクトリを分けたいが、
    # mayapy.exeのシンタックスハイライトが効かなくなるため、両者ともユーザスペースに入れている
    # 直接Explorerで操作せずにGUIで操作する前提なら、これでも良いと思う

    # TODO: ユーザスペースにgitリポジトリを入れる処理を書く
    # FEATURE:ApplicationPluginsにいれるようなツールの挙動は実現できないため、なんとかできないか考える
    # ApplicationPluginsは規定の位置に入れたままにしておき、インタプリタの参照するパスにApplicationPluginsを指定できないか調べる
    # (性格にはApplicationPluginsからの相対パス。これができるようになればそもそもPyPI以外のpackageはユーザスペースに置く必要がなくなる)
