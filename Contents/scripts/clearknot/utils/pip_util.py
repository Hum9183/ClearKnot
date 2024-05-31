# -*- coding: utf-8 -*-
from typing import Dict, List

try:
    from PySide6.QtCore import QStringListModel
except ImportError:
    from PySide2.QtCore import QStringListModel

from maya import cmds

from ..const import Const
from .list_util import try_get_item
from .subprocess_wrapper import SubprocessWrapper

m = '-m'
pip = 'pip'


def freeze() -> Dict[str, str]:
    def parse_dict(packages_text: str):
        split_newline = packages_text.split('\n')
        del split_newline[-1] # 最後の改行は削除

        parsed_dict = {}
        for package in split_newline:
            split_equal = package.split('==')
            package_name, success0 = try_get_item(split_equal, 0)
            package_version, success1 = try_get_item(split_equal, 1)
            if success0 and success1:
                parsed_dict[package_name] = package_version
            else:
                cmds.warning(f'{package}を辞書のitemに変換できませんでした')
        return parsed_dict

    freeze_cmd = [Const.mayapy_exe_path, m, pip, 'freeze']
    output, success = SubprocessWrapper.run(freeze_cmd)
    if success:
        return parse_dict(output)


def set_installed(string_list_model :QStringListModel):
    installed_packages: Dict[str, str] = freeze()
    combined_installed: List[str] = [f'{k} - {v}' for k, v in installed_packages.items()]
    string_list_model.setStringList(combined_installed)


def show_installed():
    installed_packages: Dict[str, str] = freeze()
    for package in installed_packages.items():
        print(package)
