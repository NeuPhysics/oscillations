import ternary
from matplotlib import pyplot

## Sample trajectory plot
figure, tax = ternary.figure(scale=1.0)
tax.boundary(color='black')
tax.gridlines(multiple=0.2, color="black")
tax.set_title("Neutrino Flavor Oscillations for x $\in$ [0,1000]", fontsize=20)
tax.left_axis_label("$\\nu_\\tau$", fontsize=fz)
tax.right_axis_label("$\\nu_\\mu$", fontsize=fz)
tax.bottom_axis_label("$\\nu_e$", fontsize=fz)
points = []
# Load some data, tuples (x,y,z)
with open("data/ternaryData1000.txt") as handle:
    for line in handle:
        points.append(map(float, line.split(',')))
# Plot the data
tax.plot(points, linewidth=2.0, label="Neutrino State")
tax.legend()
tax.clear_matplotlib_ticks()
pyplot.show()