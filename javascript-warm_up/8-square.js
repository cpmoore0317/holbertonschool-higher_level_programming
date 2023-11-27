#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isInteger(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
