"""
Problem #75: Average of a CSV Column (Chunked Reading)
Date: 2026-10-18

Reads iris.csv in chunks of ~8 KB, extracts the third column (index 2),
and computes its average. Works without loading the whole file into memory.
"""

with open('iris.csv', 'r') as f:
    count = 0
    sum = 0
    while True:
        lines = f.readlines(8192)
        if not lines:
            break
        for line in lines:
            values = line.split(',')
            if len(values) == 5:
                v = float(values[2].strip())
                count += 1
                sum += v
    avg = sum / count
    print(f"avr: {avg:.2f}")