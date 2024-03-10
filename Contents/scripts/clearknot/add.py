# -*- coding: utf-8 -*-
import os
import subprocess

from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QMainWindow, QMenu, QAction, QListView

from .utils import path


def add_package_from_git_url(string_list_model: QStringListModel, list_view: QListView):
    # TODO: add時にpysideのlistに追加する
    # list_view.
    string_list_model.insertRow(2)
    string_list_model.setData(string_list_model.index(2), 'test')
    return

    url = 'https://github.com/Hum9183/SampleTool01.git'
    desktop_dir = path.combine(os.path.expanduser('~/Document').split('/')[:-1])
    repository_name = url.split('/')[-1].split('.')[0]
    repository_path = path.combine([desktop_dir, r'maya/scripts', repository_name])

    print("desktop_dir::", desktop_dir)
    print("repository_name::", repository_name)
    print("repository_path::", repository_path)
    path.create_folder_recursive(repository_path)

    clone_cmd = ['git', 'clone', url, repository_path]
    cp: subprocess.CompletedProcess = subprocess.run(clone_cmd, capture_output=True)
    print("returncode: ", cp.returncode)
    print("stderr: ", cp.stderr)
    print("stdout: ", cp.stdout)

    # string_list_model.insertRow('repository_name')
