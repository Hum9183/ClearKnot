# -*- coding: utf-8 -*-
import json
import os
import subprocess
from typing import Optional

try:
    from PySide6.QtCore import QStringListModel
    from PySide6.QtGui import QAction
    from PySide6.QtWidgets import QMainWindow, QMenu, QListView
except ImportError:
    from PySide2.QtCore import QStringListModel
    from PySide2.QtWidgets import QMainWindow, QMenu, QListView, QAction

from .utils import path
from .utils import inview_message

GIT = 'git'
CLONE = 'clone'
CLEARKNOT_JSON_FILE_NAME = 'clearknot.json'
DEPENDENCIES = 'dependencies'


def add_from_git_url(string_list_model: QStringListModel, list_view: QListView):
    url = 'https://github.com/Hum9183/SampleTool01.git'
    desktop_dir = path.combine(os.path.expanduser('~/Document').split('/')[:-1])
    repository_name = url.split('/')[-1].split('.')[0]
    # TODO: OneDrive/ドキュメント/のところはちゃんとやる
    repository_path = path.combine([desktop_dir, r'OneDrive/ドキュメント/maya/scripts', repository_name])

    print("desktop_dir::", desktop_dir)
    print("repository_name::", repository_name)
    print("repository_path::", repository_path)
    __add(repository_path, repository_name, url, string_list_model)


def __add(repository_path: str, repository_name: str, url: str, string_list_model: QStringListModel) -> None:
    path.create_directory(repository_path)
    __clone(url, repository_path)
    __add_to_list_view(string_list_model, repository_name)
    dependencies: Optional[dict] = __load_dependencies(repository_path)
    if dependencies is None:
        return
    else:
        for dependency in dependencies:
            print(dependency)
            # TODO: packageの識別名・url・バージョン、をそれぞれどういう持たせるのが良いか考える
            # __add(dependency)


def __clone(url: str, repository_path: str):
    clone_cmd = [GIT, CLONE, url, repository_path]
    cp: subprocess.CompletedProcess = subprocess.run(clone_cmd, capture_output=True)
    print("returncode: ", cp.returncode)
    print("stderr: ", cp.stderr)
    print("stdout: ", cp.stdout)


def __load_dependencies(repository_path: str) -> Optional[dict]:
    # open clearknot.json
    clearknot_json_path = path.combine([repository_path, CLEARKNOT_JSON_FILE_NAME])
    if os.path.isfile(clearknot_json_path) is False:
        inview_message.show('clearknot.json does not exist.')
        return

    with open(clearknot_json_path) as text_io_wrapper:
        clearknot_json: dict = json.load(text_io_wrapper)
        # load dependencies
        dependencies: Optional[dict] = clearknot_json.get(DEPENDENCIES)
        if dependencies is None:
            inview_message.show('dependencies does not exist.')
            return
        return dependencies


def __add_to_list_view(string_list_model: QStringListModel, repository_name: str) -> None:
    string_list_model.insertRow(0)
    string_list_model.setData(string_list_model.index(0), repository_name)
    string_list_model.sort(0) # alphabet順でソートできてる？
