#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const myArr = args.map(Number).sort(function (a, b) {
    return b - a;
  });
  console.log(myArr[1]);
}
