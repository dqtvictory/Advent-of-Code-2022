# Advent of Code 2022

<a href="https://adventofcode.com/">Link</a> to the official AoC

My own solutions to the challenges of AoC this year in Python.

<b>Major update to my functional programming journey:</b> In order to "force" the proper FP style to my Python code, I have spent half a day to create an utility class `Chainable` that wraps around any Python iterable (including map/filter objects, etc...) enabling function chaining. Of course one can do the same in Python using Pandas or PySpark but these are heavy libraries with great capability which would be an overkill. Starting from Day 5, this will be my coding style until the end.

_Update Day 12: BFS algorithm -> not ideal to execute the algo using FP. I tried my best to use FP wherever I can_

_Update Day 11: Interesting day. Results in part 2 wouldn't be possible without bounding the numbers to prevent numerical explosion. Once again, FP was little possible since state changes are significant and procedural_

_Update Day 7: Haven't yet found a good way to generate a filesystem's tree from a list of instructions using FP, since the FS's state changes after each line and the correct tree can only be generate procedurally from top to bottom. The solution for this Day is unfortunately classical Python_

_Update Day 5: The input file on this day was quite annoying to parse into data, so from now on I will spend some minutes of doing text formatting before actually coding to save time. My FP solution works with original input given by the author of AoC._

_Update Day 4: I decided that programming procedurally is way too cliché, so I switched to functional programming style, still in Python. Since this is not the best language to do FP using built-in functions, the indentation and bracketing is kinda eyesoring, so I'm trying my best to make the code readable._

Executing `python XX.py fname` will display the answers to all the parts of day XX's challenge whose input is read from the file named `fname`

Since this is an event where coders compete for earlies correct submission, my original code that produces the answer is not shown in this repo. Instead, variable names and perhaps a few logics are modified and shown for better readability.

And last but not least, the answers are in no way the fastest/most optimal way to solve the challenges. The key to AoC is just early correct submission, that's it.
