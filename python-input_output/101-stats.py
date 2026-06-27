#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(total_size, status_counts):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for key in sorted(status_counts.keys()):
        if status_counts[key] > 0:
            print("{}: {}".format(key, status_counts[key]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
                if parts[-2] in status_counts:
                    status_counts[parts[-2]] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)
