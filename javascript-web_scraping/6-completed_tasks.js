#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedTasks = {};
      todos.forEach(todo => {
        if (todo.completed === true) {
          // Initialize counter for this user if it doesn't exist
          if (!completedTasks[todo.userId]) {
            completedTasks[todo.userId] = 0;
          }
          completedTasks[todo.userId]++;
        }
      });
      console.log(completedTasks);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
