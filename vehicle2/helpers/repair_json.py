import re

def repair_json(json):
    return re.sub(r'\\?x([0-9][0-9A-F])', replace_match_hex, json)


def replace_match_hex(m):
    return bytes.fromhex(m[1]).decode('utf-8')
