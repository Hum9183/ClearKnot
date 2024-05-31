# -*- coding: utf-8 -*-


def clearknot_startup_command():
    # WARNING:
    # startupコマンドではreloadは行わない。
    # 開発時は「Dev」=>「Restart」で再起動する(reloadされる)
    from clearknot import main
    main.startup()


if __name__ == '__main__':
    clearknot_startup_command()
