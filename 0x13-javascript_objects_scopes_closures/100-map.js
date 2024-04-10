#!/usr/bin/node

const data = require('./100-data.js');
const list = data.list;

const newList = list.map((element, index) => element * index);

console.log(list);
console.log(newList);
