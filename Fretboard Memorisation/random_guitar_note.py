"""Script to randomly generate and print a note in the chromatic scale and string on the guitar."""
import msvcrt
import random
import signal
import sys
import time

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
strings = ["low E", "A", "D", "G", "B", "high E"]


def exit_program(*_):
    """Signal handler function to handle exiting with CTRL+C."""
    print("Program exiting...")
    sys.exit()


if __name__ == '__main__':
    # Set the signal handler for the program to listen for CTRL+C (SIGINT).
    signal.signal(signal.SIGINT, exit_program)

    # Prompt the user to set the time between printed notes.
    while True:
        try:
            interval = float(
                input("Please specify the time between generated notes: "))
        except ValueError:
            print("The time needs to be a number...")
            continue
        if interval < 0:
            print("The time needs to be a positive value...")
        else:
            break

    EXIT = False

    # Generate a random note/string and print.
    while not EXIT:
        note = notes[random.randrange(12)]
        string = strings[random.randrange(6)]
        print(f"{note} note - {string} string")
        start = time.time()
        end = time.time()
        while end - start < interval:
            end = time.time()

        # If a valid number is entered, update the interval time.
        # If an input is entered that isn't a valid number, exit the program.
        # msvcrt.khbit() returns 1 if there has been a keypress.
        if msvcrt.kbhit():
            try:
                interval = float(msvcrt.getch())
            except ValueError:
                EXIT = True

    # A key has been pressed (that isn't a valid number) and the loop has been exited.
    print("Program exiting...")
