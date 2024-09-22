import tkinter as tk
import tkinter.font
import tkinter.filedialog
import tkinter.messagebox

class TextEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BetaWrite")

        self.text_area = tk.Text(self.window, wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        self.font_size = 10

        self.create_menu()

        self.window.mainloop()

    def new_file(self, event=None):
        self.text_area.delete(1.0, tk.END)

    def open_file(self, event=None):
        file = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.window.title(f"BetaWrite - {file}")
            self.text_area.delete(1.0, tk.END)
            with open(file, "r") as file_handler:
                self.text_area.insert(tk.INSERT, file_handler.read())
                self.text_area.delete("end-1c linestart", "end")

    def save_file(self, event=None):
        if self.window.title() == "BetaWrite":
            self.save_as_file()
        else:
            file = self.window.title().split("-")[1].split(" ")[1]
            if file:
                with open(file, "w") as file_handler:
                    file_handler.write(self.text_area.get(1.0, tk.END))
                self.window.title(f"BetaWrite - {file}")
        
    def save_as_file(self, event=None):
        file = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text FIles", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as file_handler:
                file_handler.write(self.text_area.get(1.0, tk.END))
            self.window.title(f"BetaWrite - {file}")

    def exit(self):
        self.window.destroy()

    def zoom_in(self, event=None):
        self.font_size += 5
        font = tkinter.font.Font(family="Consolas", size=self.font_size)
        self.text_area.configure(font=font)

    def zoom_out(self, event=None):
        self.font_size -= 5
        font = tkinter.font.Font(family="Consolas", size=self.font_size)
        self.text_area.configure(font=font)

    def help(self):
        tkinter.messagebox.showinfo("hlep", "up to move up, down to move down, right to move right, left to move left, if you can't figure this out, you should probably quit")

    def create_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)
        
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)

        view_menu = tk.Menu(menu)
        zoom_menu = tk.Menu(menu)
        menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_cascade(label="Zoom", menu=zoom_menu)
        zoom_menu.add_command(label="Zoom In", accelerator="Ctrl+,", command=self.zoom_in)
        zoom_menu.add_command(label="Zoom Out", accelerator="Ctrl+.", command=self.zoom_out)

        menu.add_command(label="Help", command=self.help)

        self.window.bind_all("<Control -n>", self.new_file)
        self.window.bind_all("<Control -o>", self.open_file)
        self.window.bind_all("<Control -s>", self.save_file)
        self.window.bind_all("<Control -S>", self.save_as_file)

        self.window.bind_all("<Control -comma>", self.zoom_in)
        self.window.bind_all("<Control -period>", self.zoom_out)

if __name__ == "__main__":
    text_editor = TextEditor()
