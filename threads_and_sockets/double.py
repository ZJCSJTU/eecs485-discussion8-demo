#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if not line.strip():
        continue
    print(int(line.strip()) * 2)
