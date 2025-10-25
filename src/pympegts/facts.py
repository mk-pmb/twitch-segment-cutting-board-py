# -*- coding: UTF-8, tab-width: 4 -*-

MINIMUM_PAYLOAD_OFFSET = 4
PACKET_LENGTH = 188
SYNC_BYTE_CHAR = b'G'
SYNC_BYTE_CODEPOINT = SYNC_BYTE_CHAR[0]

BORING_FIELD_VALUES = {
    'tei': False,
    'pusi': False,
    'prio': False,
    'tsc': 0,
    'af_len': False,
    'af_bytes': False,
    'pl_offs': MINIMUM_PAYLOAD_OFFSET,
    'pl_len': PACKET_LENGTH - MINIMUM_PAYLOAD_OFFSET,
    }
