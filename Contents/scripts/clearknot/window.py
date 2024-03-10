# -*- coding: utf-8 -*-
from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QMainWindow, QMenu, QAction, QListView

from maya.app.general import mayaMixin

from .add import add_package_from_git_url
from .main_commands import restart_command
from .const import Const


class ClearKnotMainWindow(mayaMixin.MayaQWidgetDockableMixin, QMainWindow):
    restored_instance = None
    name = Const.TOOL_NAME
    title = Const.TOOL_TITLE
    workspace_control = f'{name}WorkspaceControl'

    def __init__(self, parent=None, *args, **kwargs):
        super(ClearKnotMainWindow, self).__init__(parent, *args, **kwargs)
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
        add_form_git_action.triggered.connect(lambda *arg: add_package_from_git_url(self.string_list_model, self.list_view))
        add_menu = menu_bar.addMenu("Add")
        add_menu.addAction(add_form_git_action)

        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *arg: restart_command.clear_knot_restart_command())
        dev_menu = menu_bar.addMenu("Dev")
        dev_menu.addAction(restart_action)

    def init_list(self):
        self.string_list_model = QStringListModel(["Lion", "Monkey", "Tiger", "Cat"])
        self.list_view = QListView()
        self.list_view.setModel(self.string_list_model)
        self.setCentralWidget(self.list_view)

    def init_gui(self):
        self.setGeometry(500, 300, 400, 270)
        self.init_menu()
        self.init_list()


# TODO:
# window closeのコールバックで
# cmds.deleteUI(ClearKnotMainWindow.name + 'WorkspaceControl', control=True)
# を実行する
