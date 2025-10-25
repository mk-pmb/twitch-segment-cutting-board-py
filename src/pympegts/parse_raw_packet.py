# -*- coding: UTF-8, tab-width: 4 -*-

import struct

from .errors import InvalidSyncByteError
from .facts import PACKET_LENGTH
from .facts import SYNC_BYTE_CODEPOINT
from .simple_types import shybytes


def parse_raw_packet(packet):
    '''
    Parse a raw TS packet bytestring.

    The data structure information is from Wikipedia, where fortunately
    I discovered the required "excessive amount of intricate detail"
    before it was removed on 2025-08-23:
    https://en.wikipedia.org/wiki/MPEG_TS?oldid=1307033632#Elements
    '''

    sync_byte = packet[0]
    if sync_byte != SYNC_BYTE_CODEPOINT:
        raise InvalidSyncByteError(sync_byte)

    tmp, = struct.unpack('>H', packet[1:3])
    info = {
        'tei': bool(tmp & 0x80),
        # Transport error indicator:
        # A previous relay in the transmission path can set this to warn that
        # the data in this packet is damaged and the packet was relayed only
        # to preserve timings and offsets.

        'pusi': bool(tmp & 0x40),
        # Payload unit start indicator:
        #   For PES:
        :TODO:

Continuity counter

        'prio': bool(tmp & 0x20),
        # Priority packet: More urgent than others with the same PID.

        'pid': tmp & 0x1FFF, # Packet Identifier
        }

    tmp = packet[3]
    info['tsc'] = (tmp & 0xC0) >> 6
    # Transport Scrambling Control: 0 = not scrambled

    afc = (tmp & 0x30) >> 4
    # Adaptation Field Control: Whether we have an AF and/or a payload.

    # info['afc'] = afc
    # ^-- No need to expose the afc: It can be reconstructed from
    #       afc = (info['pl_offs'] and 1 or 0) + (info['af_len'] and 2 or 0)
    has_payload = bool(afc & 1)
    has_af = bool(afc & 2)
    info['cc'] = tmp & 0x0F

    af_len = has_af and packet[4] # adaptation field length
    # For af_len, the distinction between False and 0 is intentional.
    info['af_len'] = af_len
    info['af_bytes'] = has_af and shybytes(packet[5:5 + af_len])

    # Calculate payload offset:
    ploffs = has_payload and 4
    if has_payload and has_af:
        ploffs += 1 + af_len
    info['pl_offs'] = ploffs
    info['pl_len'] = PACKET_LENGTH - (ploffs or 0)
    info['pl_bytes'] = has_payload and shybytes(packet[ploffs:])

    return info








# np2
