#!/usr/bin/env python3
import time
import os


def execute_command(cmd):
    tmux_command = "tmux send-keys -t 1 '{}' 'Enter'".format(cmd)
    #print(tmux_command)
    os.system(tmux_command)

def fill_block(id, x, y, z):
    command = '/fill {} {} {} {} {} {} {}'.format(x, y, z, x, y, z, id)
    execute_command(command)

