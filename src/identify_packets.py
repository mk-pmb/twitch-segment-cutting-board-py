#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import pympegts

for packet in pympegts.read_parse_packet_stream():
    print(*pympegts.debug_util.summarize_decoded_mpegts_packet(packet))





# np2
