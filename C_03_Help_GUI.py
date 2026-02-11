from lib2to3.pygram import pattern_symbols
from tkinter import *


class Converter:
    """
    Temperature conversion tool (C to F or F to C
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady= 10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        DisplayHelp()



class DisplayHelp:

    def __init__(self):

        # setup dialogue box and background color
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"), bg=background)
        self.help_heading_label.grid(row=0)

        help_text = ("To use the program, simplt enter the temperature"
                     "you wish top convert and then choose to convert"
                     "to either degrees Celsius (centigrade) or"
                     "Fahrenheit... \n\n"
                     " Note that -273 degrees C "
                     "(-459 F) is absolute zero ( the coldest possible"
                     "temperature). If you try to convert a temperature that is less than"
                     "-273 degrees C, you will get an error message. \n\n "
                     "To see your "
                     "calculation history and export it into a text "
                     "file, please click the 'History / Export' button.")

        self.help_heading_label = Label(self.help_frame,
                                        text=help_text, wraplength=350,
                                        justify="left", bg=background)
        self.help_heading_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFFF", command=self.close_help)
        self.dismiss_button.grid(row=2, padx= 10, pady=10)

    def close_help(self):
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()