# password-validator
Function to validate a given password and output the number of passed tests and the unpassed tests.

This function takes a password and decides wheather it is valid or not based on the following changeable conditions:
  (1) The password must be more than 8 characters.
  (2) The password must be less than 30 characters.
  (3) The password must contain at least one small letter.
  (4) The password must contain at least one capital letter.
  (5) The password must contain at least one number.
  (6) The password must contain at least one non-alphnumeric character.
  
The first two conditions can be changed by assigning each one's keyword argument to the preferred number.
The remaining conditions can be turned off easily by writing the condition's name and asigning it to False in the function call:
 
This function call will make the minimum characters 10. It will not check for the small letter condition.
password_validator("Sample Password", min_chars = 10, lower_char = False)

You can add more conditions as you like. This is done by writing the name of error and asigining it to the corresponding regular expression in the function call:

This function will check if the password contains "8":
password_validator("Sample Password", no_8_number = "8")
If the condition is not met it will retain the string "no 8 number" in the errors list.

The first output of the function is the number of passed tests (integer). The second output is a list containing the errors found in the password.

example
password_validator("dfjklsfad;lajs;fljaf;lfa;lsdfjas;lfjfds") == (3, ["more than 30 characters", "no capital letters", "no numbers"]

password_validator("Asf34#fdss", no_plus='[+]', no_Q='Q') == (6, ['no plus', 'no Q'])

password_validator("jsdd88$ffd", upper_char = False, no_dollar_sign = '\$') == (6,[])
When all conditions are met, the function returns an empty list. This is better than returning nothing, because if you assign a variable to the second output, the interpreter will raise an error.

I provided a file with unit tests I conducted using pytest.

If want to imporve anything in the code, feel free to create your branch and start a pull request.
