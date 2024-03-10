# -*- coding: utf-8 -*-


def clear_knot_restart_command():
    from clearknot import main, module_reloader
    module_reloader.deep_reload(main, 'clearknot')
    main.restart()


if __name__ == '__main__':
    clear_knot_restart_command()
