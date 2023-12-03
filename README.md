# Advent of Code - 2023
https://adventofcode.com/2023
# =============================
#
## --- Day 1: Trebuchet?! ---
Full description: [2023 Day 1](https://adventofcode.com/2023/day/1)

My solution: [day_one.js](./day_one.js)

Language: `JavaScript`

#
### --- Part One ---

What is the sum of all the calibration values in your document, where each value is determined by combining the first digit and the last digit of each line into a two-digit number?

#### Example:
- `1abc2` --------- 12
- `pqr3stu8vwx` --- 38
- `a1b2c3d4e5f` --- 15
- `treb7uchet` ---- 77

Sum: `142`
#
### --- Part Two ---

What is the sum of all calibration values in your document, where each value is determined by identifying the real first and last digit (including those spelled out as words) on each line and combining them into a two-digit number?

#### Example:
- `two1nine` ----------- 29
- `eightwothree` ------- 83
- `abcone2threexyz` ---- 13
- `xtwone3four` -------- 24
- `4nineeightseven2` --- 42
- `zoneight234` -------- 14
- `7pqrstsixteen` ------ 76

Sum: `281`

## --- Day 2: Cube Conundrum ---
Full description: [2023 Day 2](https://adventofcode.com/2023/day/2)

My solution: [day_two.py](./day_two.py)

Language: `Python`
#
### --- Part One ---

Determine which games, from a list where each game shows different sets of colored cubes, would have been possible with a bag containing only

- `12` <span style="color: red">red</span> cubes
- `13` <span style="color: green">green</span> cubes
- `14` <span style="color: blue">blue</span> cubes

For each game, check if any set of cubes shown exceeds these limits. The sum of the IDs of the games that are possible under these conditions is the answer. 

#### Example:
- <b>Game 1</b>: `3` <span style="color: blue">blue</span>, `4` <span style="color: red">red</span>; `1` <span style="color: red">red</span>, `2` <span style="color: green">green</span>, `6` <span style="color: blue">blue</span>; `2` <span style="color: green">green</span>
- <b>Game 2</b>: `1` <span style="color: blue">blue</span>, `2` <span style="color: green">green</span>; `3` <span style="color: green">green</span>, `4` <span style="color: blue">blue</span>, `1` <span style="color: red">red</span>; `1` <span style="color: green">green</span>, `1` <span style="color: blue">blue</span>
- <b>Game 3</b>: `8` <span style="color: green">green</span>, `6` <span style="color: blue">blue</span>, `20` <span style="color: red">red</span>; `5` <span style="color: blue">blue</span>, `4` <span style="color: red">red</span>, `13` <span style="color: green">green</span>; `5` <span style="color: green">green</span>, `1` <span style="color: red">red</span>
- <b>Game 4</b>: `1` <span style="color: green">green</span>, `3` <span style="color: red">red</span>, `6` <span style="color: blue">blue</span>; `3` <span style="color: green">green</span>, `6` <span style="color: red">red</span>; `3` <span style="color: green">green</span>, `15` <span style="color: blue">blue</span>, `14` <span style="color: red">red</span>
- <b>Game 5</b>: `6` <span style="color: red">red</span>, `1` <span style="color: blue">blue</span>, `3` <span style="color: green">green</span>; `2` <span style="color: blue">blue</span>, `1` <span style="color: red">red</span>, `2` <span style="color: green">green</span>

Possible games: `1`, `2`, `5`

Sum of possible game IDs: `8`

### --- Part Two ---

For each game, determine the minimum number of red, green, and blue cubes that could have been in the bag to make the game possible.

Calculate the `power` of each game's minimum set of cubes by multiplying the numbers of red, green, and blue cubes together. The final answer is the sum of these powers for all the games.

#### Example:
Using the same games as above, the minimum sets of cubes for each game are:

- <b>Game 1</b>: `4` <span style="color: red">red</span>, `2` <span style="color: green">green</span>, `6` <span style="color: blue">blue</span>
- <b>Game 2</b>: `1` <span style="color: red">red</span>, `3` <span style="color: green">green</span>, `4` <span style="color: blue">blue</span>
- <b>Game 3</b>: `20` <span style="color: red">red</span>, `13` <span style="color: green">green</span>, `6` <span style="color: blue">blue</span>
- <b>Game 4</b>: `14` <span style="color: red">red</span>, `3` <span style="color: green">green</span>, `15` <span style="color: blue">blue</span>
- <b>Game 5</b>: `6` <span style="color: red">red</span>, `3` <span style="color: green">green</span>, `2` <span style="color: blue">blue</span>

Power of
- Game 1: `48`
- Game 2: `12`
- Game 3: `1560`
- Game 4: `630`
- Game 5: `36`

Sum of powers: `2286`