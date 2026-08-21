#!/usr/bin/env python3

# Import libraries
import json, os
from compute import load_data, summarize
from plot import make_plot

# Main function
def main():
    values = load_data()
    print(json.dumps(summarize(values), indent = 2))
    os.makedirs("output", exist_ok = True)
    make_plot(values)

if __name__ == "__main__":
    main()
