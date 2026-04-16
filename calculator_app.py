import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_font = font.Font(family="Arial", size=24, weight="bold")
        display = tk.Entry(
            root,
            textvar=self.display_var,
            font=display_font,
            borderwidth=2,
            relief="solid",
            justify="right",
            state="readonly"
        )
        display.pack(pady=20, padx=20, fill="both", ipady=10)
        
        # Create button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        button_font = font.Font(family="Arial", size=16, weight="bold")
        
        # Button layout
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("÷", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("×", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0), ("←", 4, 1), ("√", 4, 2), ("%", 4, 3),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(button_frame, text, row, col, button_font)
    
    def create_button(self, frame, text, row, col, font_obj):
        # Color scheme
        if text == "=":
            bg_color = "#4CAF50"
            fg_color = "white"
        elif text in ["÷", "×", "-", "+", "√", "%"]:
            bg_color = "#FF9800"
            fg_color = "white"
        elif text == "C":
            bg_color = "#f44336"
            fg_color = "white"
        elif text == "←":
            bg_color = "#2196F3"
            fg_color = "white"
        else:
            bg_color = "#f0f0f0"
            fg_color = "black"
        
        button = tk.Button(
            frame,
            text=text,
            font=font_obj,
            bg=bg_color,
            fg=fg_color,
            activebackground="#e0e0e0",
            command=lambda: self.on_button_click(text),
            relief="raised",
            borderwidth=2
        )
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure row and column weights for proper sizing
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_var.set("0")
        elif char == "←":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == "=":
            try:
                # Replace display symbols with Python operators
                calc_expression = self.expression.replace("÷", "/").replace("×", "*")
                result = eval(calc_expression)
                self.expression = str(result)
                self.display_var.set(str(result))
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif char == "√":
            try:
                result = float(self.expression) ** 0.5
                self.expression = str(result)
                self.display_var.set(str(result))
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif char == "%":
            try:
                result = float(self.expression) / 100
                self.expression = str(result)
                self.display_var.set(str(result))
            except:
                self.display_var.set("Error")
                self.expression = ""
        else:
            # Handle operator replacement for display
            if char in ["÷", "×"]:
                if self.expression and self.expression[-1] not in ["÷", "×", "-", "+"]:
                    self.expression += char
            else:
                self.expression += char
            
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
