#!/usr/bin/env python3

# Import librarie
import csv, statistics, json
import tensorflow as tf

# Main function
def main():

    # Read data
    with open("data/sample.csv") as f:
        rows = list(csv.DictReader(f))
    values = [float(r["value"]) for r in rows]

    # Compute summary and save json
    summary = {
        "summary": "test data",
        "n": len(values),
        "mean": round(statistics.mean(values), 3),
        "min": min(values),
        "max": max(values),
        "tf version": tf.__version__
    }
    print(json.dumps(summary, indent = 2))

if __name__ == "__main__":
    main()
