# Claire Francis, April 6, 2025, Week11_program1
# UNWSP-Python-Week-11
#Instructions:
#Program #1:
#Create a GUI window that displays your favorite saying.

class MyGUI:
    def __init__(self):     # - initializes the object named self
                            # - known as the constructor of the object

        # Create the main window widget.
        self.main_window = tkinter.Tk()     # - is from the tkinter module
                                            # - assigned to main_window variable in the self object

        # Display a title.
        self.main_window.title('Week11Program1')

        self.label = tkinter.Label(self.main_window, text='Baka!')
        self.label.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()      # - called from tkinter module
                                # - waits for events to occur
                                # - runs until program closes

# create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()





# Claire Francis, April 6, 2025, Week11_program2
#Program #2: 
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
