#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const userTaskCount = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (userTaskCount[todo.userId]) {
          userTaskCount[todo.userId]++;
        } else {
          userTaskCount[todo.userId] = 1;
        }
      }
    });
    console.log(JSON.stringify(userTaskCount, null, 2));
  } else {
    console.log(`Error: Received status code ${response.statusCode}`);
  }
});
