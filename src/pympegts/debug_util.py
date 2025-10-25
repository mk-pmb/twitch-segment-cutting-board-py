# -*- coding: UTF-8, tab-width: 4 -*-

from . import facts as _facts


def asciidump(buf):
    if not buf: return None
    return ''.join([
        (chr(b) if b >= 32 and b <= 126 else '.')
        for b in buf])


def summarize_decoded_mpegts_packet(orig_packet, payload_preview=60):
    keep = { **orig_packet }
    data = keep['pl_bytes']
    preview = ((payload_preview > 0) and
        data and asciidump(data[0:payload_preview]))
    for key, val in _facts.BORING_FIELD_VALUES.items():
        if keep.get(key) == val:
            del keep[key]
    return preview, keep
