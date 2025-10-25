# -*- coding: UTF-8, tab-width: 4 -*-

import os

from .facts import PACKET_LENGTH


def read_raw_packet_stream(src_fd_num=0):
    '''
    Read from a file descriptor and yield proper packets.
    Yields: bytes
    '''
    partial = b''
    while True:
        hunger = PACKET_LENGTH - len(partial)
        packet = os.read(src_fd_num, hunger)
        pk_len = len(packet)
        if not pk_len:
            # EOF means the pipe ended.
            # If input is idle but alive, read will just block.
            return
        if pk_len > hunger:
            raise SystemError('os.read gave too much data! '
                'This contradicts the pydoc description '
                '"Read at most n bytes".')
        if pk_len < hunger:
            partial += packet
            continue
        if partial:
            packet = partial + packet
            partial = b''
        yield packet


