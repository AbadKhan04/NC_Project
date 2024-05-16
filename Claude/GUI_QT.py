# only GUI trying to use QTpy not work leave this file and delete in last
import sys
from PyQt5 import QtWidgets, uic
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EquationSolver(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("equation_solver.ui", self)

        # Connect buttons to their respective functions
        self.heat_button.clicked.connect(self.heat_conduction)
        self.wave_button.clicked.connect(self.wave_equation)
        self.fluid_button.clicked.connect(self.fluid_flow)

        # Create a figure for plotting
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)

    def heat_conduction(self):
        # Implementation for Heat Conduction in a Solid
        pass

    def wave_equation(self):
        # Implementation for Wave Equation for Vibrating Structures
        pass

    def fluid_flow(self):
        # Implementation for Fluid Flow in a Domain
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EquationSolver()
    window.show()
    sys.exit(app.exec_())