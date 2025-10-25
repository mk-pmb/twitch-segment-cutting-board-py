# -*- coding: UTF-8, tab-width: 4 -*-

from .facts import PACKET_LENGTH
from .parse_raw_packet import parse_raw_packet
from .read_raw_packet_stream import read_raw_packet_stream


def read_parse_packet_stream(*args, **kwargs):
    input_offs = 0
    for packet in read_raw_packet_stream(*args, **kwargs):
        packet = parse_raw_packet(packet)
        packet['input_offs'] = input_offs
        input_offs += PACKET_LENGTH
        yield packet


