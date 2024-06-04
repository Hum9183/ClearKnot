# -*- coding: utf-8 -*-


def start_clearknot():
    # WARNING:
    # startではreloadは行わない。
    # reloadしたい場合は「Dev」=>「Restart」を実行する
    from clearknot import run
    run.startup()


if __name__ == '__main__':
    start_clearknot()
