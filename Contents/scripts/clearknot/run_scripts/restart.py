# -*- coding: utf-8 -*-


def restart_clearknot():
    from clearknot import run, module_reloader
    module_reloader.deep_reload(run, 'clearknot')
    run.restart()


if __name__ == '__main__':
    restart_clearknot()
