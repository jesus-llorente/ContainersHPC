# Import libraries
import matplotlib
matplotlib.use("Agg") # sin display dentro del container, obligatorio
import matplotlib.pyplot as plt

def make_plot(values, output_path = "output/plot.png"):
    plt.figure()
    plt.plot(values, marker = "o")
    plt.title("Sample values")
    plt.savefig(output_path)
    