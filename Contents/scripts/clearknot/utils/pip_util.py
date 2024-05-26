# -*- coding: utf-8 -*-
from typing import Dict

try:
    from PySide6.QtCore import QStringListModel
except ImportError:
    from PySide2.QtCore import QStringListModel


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
        for xx in split_newline:
            split_equal = xx.split('==')
            package_name, success0 = try_get_item(split_equal, 0)
            version, success1 = try_get_item(split_equal, 1)
            if success0 and success1:
                parsed_dict[package_name] = version
        return parsed_dict

    freeze_cmd = [Const.mayapy_exe_path, m, pip, 'freeze']
    output, success = SubprocessWrapper.run(freeze_cmd)
    if success:
        return parse_dict(output)


def set_installed(string_list_model :QStringListModel):
    installed = freeze()
    combined_installed = [f'{k} - {v}' for k, v in installed.items()]
    string_list_model.setStringList(combined_installed)


def show_installed():
    installed_packages = freeze()
    for package in installed_packages.items():
        print(package)
