import tkinter as tk

class SimpleCalc:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Basic Calculator")
        self.main_window.geometry("320x450")
        self.main_window.resizable(False, False)
        
        self.current_input = ""

        # Frame for the input field
        input_frame = tk.Frame(self.main_window, height=60, bg="lightblue")
        input_frame.pack(fill="both")

        self.display_var = tk.StringVar()
        display_field = tk.Entry(input_frame, textvariable=self.display_var, font=('Helvetica', 24), bd=0, bg="white", justify="right")
        display_field.pack(expand=True, fill="both")

        # Frame for buttons
        button_frame = tk.Frame(self.main_window)
        button_frame.pack()

        # Button layout
        button_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for button_row in button_layout:
            row_container = tk.Frame(button_frame)
            row_container.pack(expand=True, fill="both")
            for button_label in button_row:
                btn = tk.Button(row_container, text=button_label, font=('Helvetica', 20), height=2, width=4,
                                command=lambda x=button_label: self.process_input(x))
                btn.pack(side="left", expand=True, fill="both")

    def process_input(self, input_char):
        if input_char == "C":
            self.current_input = ""
        elif input_char == "=":
            try:
                self.current_input = str(eval(self.current_input))
            except Exception:
                self.current_input = "Error"
        else:
            self.current_input += str(input_char)
        self.display_var.set(self.current_input)

# Launch the application
if __name__ == "__main__":
    main_window = tk.Tk()
    SimpleCalc(main_window)
    main_window.mainloop()