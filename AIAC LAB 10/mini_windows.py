import tkinter as tk
from tkinter import messagebox
class MiniWindowsOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Windows OS")
        self.root.geometry("800x500")
        self.root.configure(bg='#008080')
        self.create_taskbar()
        self.create_desktop_icons()

    def create_taskbar(self):
        self.taskbar = tk.Frame(self.root, bg='#222', height=40)
        self.taskbar.pack(side='bottom', fill='x')
        start_btn = tk.Button(self.taskbar, text="Start", command=self.show_start_menu, bg='#444', fg='white')
        start_btn.pack(side='left', padx=5, pady=5)

    def create_desktop_icons(self):
        notepad_icon = tk.Button(self.root, text="Notepad", command=self.open_notepad, width=10, height=2)
        notepad_icon.place(x=50, y=50)
        calc_icon = tk.Button(self.root, text="Calculator", command=self.open_calculator, width=10, height=2)
        calc_icon.place(x=50, y=120)
        about_icon = tk.Button(self.root, text="About", command=self.open_about, width=10, height=2)
        about_icon.place(x=50, y=190)

    def show_start_menu(self):
        menu = tk.Toplevel(self.root)
        menu.title("Start Menu")
        menu.geometry("200x250+0+250")
        menu.resizable(False, False)
        tk.Button(menu, text="Notepad", width=20, command=self.open_notepad).pack(pady=5)
        tk.Button(menu, text="Calculator", width=20, command=self.open_calculator).pack(pady=5)
        tk.Button(menu, text="About", width=20, command=self.open_about).pack(pady=5)
        tk.Button(menu, text="Exit", width=20, command=self.root.quit).pack(pady=5)
        menu.transient(self.root)
        menu.grab_set()
    def open_calculator(self):
        calc = tk.Toplevel(self.root)
        calc.title("Calculator")
        calc.geometry("300x400")
        calc.resizable(False, False)
        entry = tk.Entry(calc, width=16, font=('Arial', 24), bd=4, relief='ridge', justify='right')
        entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
        ]
        for (text, r, c) in buttons:
            tk.Button(calc, text=text, width=5, height=2, font=('Arial', 14),
                      command=lambda t=text: self.calc_click(t, entry)).grid(row=r, column=c, padx=5, pady=5)

    def calc_click(self, char, entry):
        if char == '=':
            try:
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(eval(entry.get())))
            except Exception:
                entry.delete(0, tk.END)
                entry.insert(tk.END, 'Error')
        else:
            entry.insert(tk.END, char)

    def open_about(self):
        about = tk.Toplevel(self.root)
        about.title("About Mini Windows OS")
        about.geometry("300x150")
        tk.Label(about, text="Mini Windows OS\nPython Tkinter Demo\n2025", font=('Arial', 12)).pack(expand=True)
        tk.Button(about, text="Close", command=about.destroy).pack(pady=10)

    def open_notepad(self):
        notepad = tk.Toplevel(self.root)
        notepad.title("Notepad")
        notepad.geometry("400x300")
        text = tk.Text(notepad)
        text.pack(expand=True, fill='both')
        notepad.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniWindowsOS(root)
    root.mainloop()
