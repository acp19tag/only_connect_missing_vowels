import tkinter as tk
import random as rnd
 
class Counter:
    def __init__(self, value):
        self.value = value
 
    def __sub__(self, other):
        return Counter(self.value - other.value)
 
class Number:
    def __init__(self, number):
        self.number = number
 
    def __lt__(self, number):
        return self.number < number
 
    def __gt__(self, number):
        return self.number > number
 
    def __eq__(self, number):
        return self.number == number
 
class Window:
    def __init__(self, parent):
        self.parent = parent
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
 
        # Set the counter
        self.counter = Counter(3)
        self.random_number = Number(rnd.randint(1, 20))
 
        # Main container holds all other containers and widgets
        container = tk.Frame(self.parent)
        container.grid(column=0, row=0, sticky='new')
        container.grid_columnconfigure(0, weight=3)
 
        # line1 container holds widgets on the first row
        line1_container = tk.Frame(container)
        line1_container['relief'] = 'groove'
        line1_container.grid(column=0, row=1, sticky = 'new', padx=4, pady=4, ipady=4, ipadx=2)
        line1_container.grid_columnconfigure(0, weight=0)
        line1_container.grid_columnconfigure(1, weight=0)
        line1_container.grid_columnconfigure(2, weight=3)
 
        # line2 container holds field and button widgets
        line2_container = tk.Frame(container)
        line2_container['relief'] = 'groove'
        line2_container.grid(column=0, row=2, sticky='new', padx=4, pady=4, ipady=4, ipadx=2)
        line2_container.grid_columnconfigure(0, weight=0)
        line2_container.grid_columnconfigure(1, weight=3)
        line2_container.grid_columnconfigure(2, weight=3)
 
        line3 = tk.Label(container, text='Choose a number between 1 and 20')
        line3['relief'] = 'groove'
        line3['font'] = 'times 10 italic'
        line3['fg'] = 'gray'
        line3.grid(column=0, row=3, sticky='new', padx=4, pady=4)
 
        # entry_frame is padding for the text field
        # (gives the appearence of not having the text right up against the left side)
        self.entry_frame = tk.Frame(line2_container)
        self.entry_frame['relief'] = 'sunken'
        self.entry_frame['borderwidth'] = 1
        self.entry_frame['bg'] = 'white'
        self.entry_frame.grid(column=0, row=0, sticky='new', padx=4, pady=4)
 
        # The header contains the game name
        header = tk.Label(container)
        header['text'] = 'Tkinter Number Guessing Game'
        header['font'] = 'Sans 16 bold'
        header['fg'] = 'darkslateblue'
        header['relief'] = 'groove'
        header.grid(column=0, row=0, sticky='new', padx=4, pady=4, ipady=4, ipadx=2)
 
        # Label for displaying number of guesses left
        self.guess_left = tk.Label(line1_container, anchor='w')
        self.guess_left['bg'] = 'lightgray'
        self.guess_left['relief'] = 'groove'
        self.guess_left['text'] = 'Guesses Left: 3'
        self.guess_left.grid(column=0, row=0, sticky='new', ipadx=5)
 
        # Label for message header
        msgbox = tk.Label(line1_container, anchor='w')
        msgbox['text'] = 'MSG:'
        msgbox['relief'] = 'groove'
        msgbox['bg'] = 'lightgray'
        msgbox.grid(column=1, row=0, sticky='new')
 
        # Label for displaying all messages
        self.msgtext = tk.Label(line1_container, anchor='w', padx=8)
        self.msgtext['text'] = 'Choose a number between 1 and 20'
        self.msgtext['relief'] = 'groove'
        self.msgtext['bg'] = 'lightgray'
        self.msgtext.grid(column=2, row=0, sticky='new')
 
        # Entry field for entering numbers
        self.entry = tk.Entry(self.entry_frame, width=4)
        self.entry['relief'] = 'flat'
        self.entry.grid(column=0, row=0, sticky='new', padx=4)
        self.entry.focus()
        self.entry.bind('<Return>', lambda num: self.check_number(self.entry.get()))
 
 
        # Button for submitting numbers
        self.submit_button = tk.Button(line2_container, text='Submit')
        # self.submit_button['cursor'] = 'hand2'
        self.submit_button['command'] = lambda: self.check_number(self.entry.get())
        self.submit_button.grid(column=1, row=0, sticky='new', padx=2, pady=2)
 
        # Button for resetting everything to defaults
        self.reset_button = tk.Button(line2_container, text='Reset')
        self.reset_button['state'] = 'disabled'
        # self.reset_button['cursor'] = 'no'
        self.reset_button.grid(column=2, row=0, sticky='new', padx=2, pady=2)
 
    # Method for checking guess against random number
    def check_number(self, guess):
        # Set some variables
        count = self.counter.value
        fgcolor = 'red'
        bgcolor = 'lightyellow'

        # Use a try statement in check for numbers only
        try:
            guess = int(guess)

            # We want the guess number to be between 1 and 20
            if guess > 20 or guess < 1:
                msg = 'Please choose a number between 1 and 20'
                count += 1
                setattr(self.counter, 'value', count)

            # Guess number is within spec
            # Compare the numbers and set the correct message
            else:
                if guess > self.random_number:
                    msg = f'{guess} is too high'
                if guess < self.random_number:
                    msg = f'{guess} is too low'

                # Correct number was guessed. Enable reset button and disable
                # the submit button. Also set some colors and other graphic views
                if guess == self.random_number:
                    self.submit_button['state'] = 'disabled'
                    self.entry.delete(0, tk.END)
                    self.entry['state'] = 'disabled'
                    self.entry_frame['bg'] = 'gray95'
                    # self.submit_button['cursor'] = 'no'
                    self.reset_button['state'] = 'normal'
                    # self.reset_button['cursor'] = 'hand2'
                    self.reset_button['command'] = lambda: self.reset()
                    self.reset_button.bind('<Return>', lambda num: self.reset())
                    self.reset_button.focus()
                    msg = f'Great job! {guess} was the correct number'
                    fgcolor = 'lime'
                    bgcolor = 'darkgreen'
        # A character other than a number was entered.
        # Display a error message
        except ValueError:
            msg = 'Please enter only whole numbers'
            count += 1
            setattr(self.counter, 'value', count)

        # Clear entry field
        self.entry.delete(0, tk.END)

        # If the last guess has been used, enable and disable the coreect buttons.
        # Also set some graphic views such as colors and cursor
        if count == 1:
            setattr(self.counter, 'value', 0)
            count = 0
            self.entry['state'] = 'disabled'
            self.entry_frame['bg'] = 'gray95'
            self.submit_button['state'] = 'disabled'
            self.reset_button['state'] = 'normal'
            self.reset_button['command'] = lambda: self.reset()
            # self.reset_button['cursor'] = 'hand2'
            # self.submit_button['cursor'] = 'no'
            self.reset_button.focus()
            self.reset_button.bind('<Return>', lambda num: self.reset())
            msg += ' Press reset to play again.'

        else:
            count = self.counter.value - 1
        setattr(self.counter, 'value', count)
        self.guess_left['text'] = f'Guesses Left: {count}'
        self.msgtext['text'] = msg
        self.msgtext['fg'] = fgcolor
        self.msgtext['bg'] = bgcolor
 
 
    # Method for resetting game
    def reset(self):
        self.entry['state'] = 'normal'
        self.entry_frame['bg'] = 'white'
        self.entry.focus()
        self.submit_button['state'] = 'normal'
        self.reset_button['state'] = 'disabled'
        setattr(self.counter, 'value', 3)
        self.guess_left['text'] = f'Guesses Left: {self.counter.value}'
        # self.reset_button['cursor'] = 'no'
        # self.submit_button['cursor'] = 'hand2'
        self.msgtext['text'] = 'Game has been reset'
        self.msgtext['fg'] = 'red'
        self.msgtext['bg'] = 'lightyellow'
        self.random_number = Number(rnd.randint(1, 20))
 
 
def main():
    root = tk.Tk()
    root.geometry('460x160+250+250')
    root.resizable(False, False)
    Window(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()