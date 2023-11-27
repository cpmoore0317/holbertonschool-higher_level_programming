#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueNumbers = Array.from(new Set(args)); // Remove duplicates
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a); // Sort in descending order
  console.log(sortedNumbers[1]);
}
