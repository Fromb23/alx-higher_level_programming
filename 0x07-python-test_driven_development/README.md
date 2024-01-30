# Project: Python - Test-driven development

## Background Context

### Important Notice on Intranet Checks for Python Projects

Starting from today:

- Write documentation (module(s) + function(s)) and tests first before coding.
- Intranet checks won't be released before the first deadline to prioritize TDD.
- Collaborate on test cases to cover all possible edge cases.
- Do not trust the user; consider all possible scenarios.

### Resources

Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html#doctest.Tester)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#interactive-and-non-interactive-tests)

## Learning Objectives

By the end of this project, you should be able to explain:

1. Why Python programming is awesome.
2. What an interactive test is.
3. The importance of tests.
4. How to write Docstrings for creating tests.
5. How to write documentation for each module and function.
6. Basic option flags to create tests.
7. How to find edge cases.

## Copyright - Plagiarism

- Develop solutions for tasks independently.
- No copying and pasting; plagiarism results in removal from the program.
- Do not publish any content of this project.

## Requirements

### Python Scripts

- Editors: vi, vim, emacs
- Interpret/compile on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files end with a new line
- First line: `#!/usr/bin/python3`
- Mandatory README.md file at the project root
- Code uses pycodestyle (version 2.8.*)
- All files must be executable
- Length of files tested using wc

### Python Test Cases

- Editors: vi, vim, emacs
- All files end with a new line
- Test files inside a folder named "tests"
- Test files are text files (extension: .txt)
- Execute tests using: `python3 -m doctest ./tests/*`
- Modules have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Functions have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation is a real sentence explaining the purpose (length verified)

### Author

Fromb23
