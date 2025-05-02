# Claire Francis, April 6, 2025, Week11_program2
#Write a GUI program that displays your name and address when a "Show Info" button is clicked.  There should also be a "Quit" button which exists the GUI.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.my_button = tkinter.Button(self.main_window, text = 'Click Me!', command = self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Claire Francis, 2642 104th CT NE, Minneapolis, Minnesota.')

if __name__ == '__main__':
    my_gui = MyGUI()