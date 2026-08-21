# Import libraries
import csv, statistics
import tensorflow as tf

def load_data(path = "data/sample.csv"):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    return [float(r["value"]) for r in rows]

def summarize(values):
    return {
        "summary": "test data",
        "n": len(values),
        "mean": round(statistics.mean(values), 3),
        "min": min(values),
        "max": max(values),
        "tensorflow": tf.__version__
    }