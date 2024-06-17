#!/usr/bin/node

// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function
module.exports.callMeMoby = callMeMoby;
