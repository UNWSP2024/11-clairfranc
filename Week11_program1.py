# Claire Francis, April 6, 2025, Week11_program1
# UNWSP-Python-Week-11
#Create a GUI window that displays your favorite saying.
import tkinter

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