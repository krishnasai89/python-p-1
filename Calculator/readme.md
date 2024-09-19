#Calculator
It prompts the user to input a mathematical expression (as a string).
It uses the eval() function to evaluate the expression.
The evaluated result is stored in the variable cal.
Finally, it prints the result with an equal sign (=) in front of it.
The input() function reads a string from the user.
The eval() function evaluates the expression (which can be any valid Python expression) and returns the result.
Using eval() can be powerful but also risky. It allows arbitrary code execution, so be cautious when using it with user input. Sanitize and validate the input thoroughly.
The int() function converts the result to an integer (if possible).
The print() statement displays the result preceded by an equal sign.