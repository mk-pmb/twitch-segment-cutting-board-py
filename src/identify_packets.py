#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

from pympegts import read_parse_packet_stream
from pympegts.debug_util import summarize_decoded_mpegts_packet

for packet in read_parse_packet_stream():
    meta, *preview = summarize_decoded_mpegts_packet(packet)
    print(*preview, meta)





# np2
