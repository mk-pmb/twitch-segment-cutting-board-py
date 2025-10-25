# -*- coding: UTF-8, tab-width: 4 -*-

import struct

from .errors import InvalidSyncByteError
from .facts import PACKET_LENGTH
from .facts import SYNC_BYTE_CODEPOINT
from .simple_types import shybytes


def parse_raw_packet(packet):
    sync_byte = packet[0]
    if sync_byte != SYNC_BYTE_CODEPOINT:
        raise InvalidSyncByteError(sync_byte)

    tmp, = struct.unpack('>H', packet[1:3])
    info = {
        'tei': bool(tmp & 0x80),
        'pusi': bool(tmp & 0x40),
        'prio': bool(tmp & 0x20),
        'pid': tmp & 0x1FFF,
        }

    tmp = packet[3]
    info['tsc'] = (tmp & 0xC0) >> 6
    afc = (tmp & 0x30) >> 4
    info['afc'] = afc
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
