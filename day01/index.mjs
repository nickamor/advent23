//@ts-check

import { readFile } from "fs";

/**
 * @param {string} line
 */
function replace_words(line) {
  const digit_words = {
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };

  for (let i = 0; i < line.length; i++) {
    const substr = line.substring(i);
    for (const word of Object.keys(digit_words)) {
      if (substr.indexOf(word) == 0) {
        return replace_words(
          line.substring(0, i) + substr.replace(word, digit_words[word])
        );
      }
    }
  }

  return line;
}

/**
 * @param {string} line
 */
function get_digits(line) {
  return line.replace(/[a-z]/g, "");
}

/**
 * @param {string} line
 */
function extract_value(line) {
  line = replace_words(line);
  line = get_digits(line);
  return Number(line[0] + line[-1]);
}

function read_lines(filename, callback) {
  readFile(filename, (err, data) => {
    data;
  });
}

function main(filename = "./day01/input") {
  let sum = 0;

  read_lines(filename).forEach(function (line) {});

  console.log(sum);
}

main("./day01/test1");
main("./day01/test2");
main();
