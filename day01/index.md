<a href="https://adventofcode.com/2023/day/1">Description</a>

<ul>
  <li>
    if you strip all non-digit characters, you can just get the first and last
    characters
  </li>
  <li>
    if afterwards the line is 1 character, the first and last are the same
    character anyway
  </li>
  <li>
    you can swap in the equivalent digit of each of the supported digit-words,
    but be sure to traverse the string and all substrings first - 'twone' and
    'eighthree' should be 2 and 8 respectively
  </li>
</ul>
