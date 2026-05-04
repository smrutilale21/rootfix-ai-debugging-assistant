SAMPLE_BUGS = {
    "None": {
        "language": "Python",
        "code": "",
        "error": "",
        "expected_behavior": "",
        "context": "",
    },

    "Python TypeError": {
        "language": "Python",
        "code": """def add_numbers(a, b):
    return a + b

result = add_numbers(10, "20")
print(result)
""",
        "error": "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        "expected_behavior": "The program should add two numbers and print 30.",
        "context": "Beginner Python function example.",
    },

    "JavaScript ReferenceError": {
        "language": "JavaScript",
        "code": """function greetUser() {
  console.log(userName);
}

greetUser();
""",
        "error": "ReferenceError: userName is not defined",
        "expected_behavior": "The function should print the user's name.",
        "context": "Simple JavaScript function demo.",
    },

    "React useState Bug": {
        "language": "React",
        "code": """import React from "react";

function Counter() {
  const count = 0;

  function increment() {
    count = count + 1;
  }

  return (
    <button onClick={increment}>
      Count: {count}
    </button>
  );
}

export default Counter;
""",
        "error": "TypeError / Assignment error: Assignment to constant variable",
        "expected_behavior": "Clicking the button should increase the count.",
        "context": "React component using state incorrectly.",
    },

    "SQL Syntax Error": {
        "language": "SQL",
        "code": """SELECT name age
FROM users
WHERE age > 18
ORDER age DESC;
""",
        "error": "SQL syntax error near 'age'",
        "expected_behavior": "Fetch user names and ages where age is greater than 18.",
        "context": "Basic SQL query.",
    },

    "API Request Error": {
        "language": "Python",
        "code": """import requests

response = requests.get("https://api.example.com/users")
data = response.json()

print(data["name"])
""",
        "error": "KeyError: 'name'",
        "expected_behavior": "Fetch user data from API and print user name.",
        "context": "API may return a list of users instead of a single object.",
    },
}