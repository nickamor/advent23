<a href="https://adventofcode.com/2023/day/1">Description</a>

* if you strip all non-digit characters, you can just get the first and last
    characters
* if afterwards the line is 1 character, the first and last are the same
    character anyway
* you can swap in the equivalent digit of each of the supported digit-words,
    but be sure to traverse the string and all substrings first - 'twone' and
    'eighthree' should be 2 and 8 respectively

## later..

- it wasn't obvious until i checked the subreddit, but

```
eightwothree
```

is correctly parsed as

```
['8', '2', '3']
```

ie. overlapping words are considered

there are lines in the input file (but not the test file) that depend on this.
i spent so much time and effort to avoid this behaviour!!

- need to extract word values in a stable way (retain order of appearance with numerals)
