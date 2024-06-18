# -*- coding: utf-8 -*-
from maya.app.general import mayaMixin

try:
    from PySide6.QtCore import QStringListModel
    from PySide6.QtGui import QAction
    from PySide6.QtWidgets import QMainWindow, QMenu, QListView
except ImportError:
    from PySide2.QtCore import QStringListModel
    from PySide2.QtWidgets import QAction, QMainWindow, QMenu, QListView

from .package_adder import add_from_git_url
from . import pip_installer
from .run_scripts.restart import restart_clearknot
from .const import Const

from .utils import pip_util


class ClearKnotMainWindow(mayaMixin.MayaQWidgetDockableMixin, QMainWindow):
    restored_instance = None
    name = Const.TOOL_NAME
    title = Const.TOOL_TITLE
    workspace_control = f'{name}WorkspaceControl'

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.list_view = None
        self.string_list_model = None

    def init(self):
        self.setObjectName(ClearKnotMainWindow.name)
        self.setWindowTitle(ClearKnotMainWindow.title)

    def init_menu(self):
        open_menu = QMenu("Open")
        open_menu.addAction("help")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+G")
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        file_menu.addMenu(open_menu)
        file_menu.addAction(exit_action)

        add_form_git_action = QAction('Add package from git URL', self)
        add_form_git_action.triggered.connect(lambda *arg: add_from_git_url(self.string_list_model, self.list_view))
        add_form_pip_action = QAction('Add package from pip(PyPI)', self)
        add_form_pip_action.triggered.connect(lambda *arg: pip_installer.add(self.string_list_model))
        remove_form_pip_action = QAction('Remove package from pip(PyPI)', self)
        remove_form_pip_action.triggered.connect(lambda *arg: pip_installer.remove(self.string_list_model))
        test_action = QAction('show installed', self)
        test_action.triggered.connect(lambda *arg: pip_util.show_installed())
        add_menu = menu_bar.addMenu("Add")
        add_menu.addAction(add_form_git_action)
        add_menu.addAction(add_form_pip_action)
        add_menu.addAction(remove_form_pip_action)
        add_menu.addAction(test_action)

        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *arg: restart_clearknot())
        dev_menu = menu_bar.addMenu("Dev")
        dev_menu.addAction(restart_action)

        version_action = QAction('version', self)
        version_action.triggered.connect(lambda *arg: print(Const.TOOL_VERSION))
        help_menu = menu_bar.addMenu("help")
        help_menu.addAction(version_action)


    def init_list(self):
        self.string_list_model = QStringListModel()
        pip_util.set_installed(self.string_list_model)
        self.list_view = QListView()
        self.list_view.setModel(self.string_list_model)
        self.setCentralWidget(self.list_view)

    def init_gui(self):
        self.setGeometry(500, 300, 400, 270)
        self.init_menu()
        self.init_list()


    def test_debug(self):
        pip_util.freeze()

# TODO:
# window closeのコールバックで
# cmds.deleteUI(ClearKnotMainWindow.name + 'WorkspaceControl', control=True)
# を実行する
