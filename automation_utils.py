!/usr/bin/env python3
import time
import os


def execute_command(cmd):
    os.system("tmux send-keys -t 1 '{}' 'Enter'".format(cmd))

def fill_block(id, x, y, z):
    command = '/fill {} {} {} {} {} {} {}'.format(x, y, z, x, y, z, id)
    execute_command(command)


if __name__ == "__main__":
    while True:
        execute('/weather clear')
        execute('/time set day')
        time.sleep(60)
