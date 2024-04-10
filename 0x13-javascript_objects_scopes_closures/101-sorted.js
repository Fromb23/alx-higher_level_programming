#!/usr/bin/node

const data = require('./101-data.js');
const dict = data.dict;

const newDict = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (newDict[occurrence]) {
    newDict[occurrence].push(userId);
  } else {
    newDict[occurrence] = [userId];
  }
}

console.log(newDict);
