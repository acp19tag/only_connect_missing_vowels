# Only Connect Missing Vowels Quiz

## Description

A simple program that asks you questions from the final round of the British TV show "Only Connect" (https://en.wikipedia.org/wiki/Only_Connect). 

The program will show you a clue category (e.g. _Dishes made using eggs_), and you will be shown a series of clues that fit the category but with their vowels removed (e.g. _MRN G_ -> _MERINGUE_). 

After each clue is shown, you will press **Enter** to buzz in, and then you will be asked to record whether you were correct, incorrect, or if you decided to abstain. 

At the end of a specified number of rounds, the program will show you how well you did. 

## Instructions

1. Install Python 3.8 or later
2. Install requirements 
> `pip install -r requirements.txt`
3. Run the program
> `python main.py`

## Client Specification 

> Ideally what I'm wanting is something like the show; the category gets revealed for the missing vowels, and then (when you want to see the first) you can press a button and the first one comes up. Repeated four times (some of the groups from the show you only see 1-3 of, so these would be excluded).
Ideally I'd like to be able to specify how many different groups of four you want to see before it stops, and gives you a time on how you did.
While typing in would show if you're right as it currently works, I'd prefer to be timed on from seeing the clue to buzzing in. After that you then press a button to show the answer, then you can say whether you were wrong or right like an honour system instead (or alternatively, time you out if you go 7 seconds without answering).
After that, it would tell you how many you got right (1 for correct, -1 for incorrect, 0 for abstention), and in what time.

## Feature Implementation Checklist

- [x] Data Reader (.csv)
- [x] Basic Question Asking Functionality
- [x] Question Timing
- [x] Argument: $n$ groups before stoppping
- [x] Round Statistics
- [x] Endless Mode 
- [ ] Better looking user interface
- [ ] Enduring Personal Statistics
- [ ] Score vs Live Team

## Resources

Vowel Clue Data Source: [prettygr.im](https://prettygr.im/smoci/only-connect/vowel_clues)