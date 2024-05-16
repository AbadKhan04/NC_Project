import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equation Solver")
        self.geometry("400x300")
        
        self.equation_choice = tk.StringVar()
        self.equation_choice.set("Heat Conduction")
        
        self.create_widgets()
        
    def create_widgets(self):
        ttk.Label(self, text="Equation Solver", font=("Arial", 18)).pack(pady=10)
        
        equation_frame = ttk.Frame(self)
        equation_frame.pack(pady=10)
        
        ttk.Radiobutton(equation_frame, text="Heat Conduction", variable=self.equation_choice, value="Heat Conduction").grid(row=0, column=0, padx=5)
        ttk.Radiobutton(equation_frame, text="Wave Equation", variable=self.equation_choice, value="Wave Equation").grid(row=0, column=1, padx=5)
        ttk.Radiobutton(equation_frame, text="Fluid Flow", variable=self.equation_choice, value="Fluid Flow").grid(row=0, column=2, padx=5)
        
        ttk.Label(self, text="Input Values:").pack()
        self.input_entry = ttk.Entry(self)
        self.input_entry.pack()
        
        ttk.Button(self, text="Solve", command=self.solve_equation).pack(pady=10)
        
        self.output_label = ttk.Label(self, text="")
        self.output_label.pack()
        
    def solve_equation(self):
        equation = self.equation_choice.get()
        input_value = self.input_entry.get()
        
        # Code for solving equations goes here
        
        self.output_label.config(text="Output: Solution for {} with input {} is ...".format(equation, input_value))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
