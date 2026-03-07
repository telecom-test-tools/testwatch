import re

FAIL_PATTERNS = [
    "FAIL",
    "FAILED",
    "ERROR",
    "CRASH",
    "TIMEOUT"
]

def parse_line(line):
    for pattern in FAIL_PATTERNS:
        if re.search(pattern, line, re.IGNORECASE):
            return "FAIL"
    return "PASS"