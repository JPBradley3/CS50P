## There is a library called "re" that uses a database of regular expressions to be able to interpret user input and allow us to get ahead of potential errors proactively.
## The module we will focus on first is search [  re.search(pattern, string, flags=0) ]
        ## So the module takes arguments inside parenthesis and allows the coder to be able to manipulate things like strings about patterns with an operator at the
        ## end that we are also able to control additional functions of the module with.
## For things like the following code commented out we are able to transition to "re" to better form our code:
#email = input(f"Whats your email: ").strip()

#username, domain = email.split("@")

#if (username) and (domain.endswith(".edu")):
  #  print("Valid")
#else:
 #   print("Invlaid")

## First we can impor the module:

import re

email = input("What's your email? ").strip()

## As we can see here this module is very pattern oriented and is more able to look through strings and detect simple repetitive things to verify or calculate or other
## things.

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

## This impementation is for all inputs that contain an email including a paragraph from a website.

## This example leverages ^ and ? to match the start and end of the string of input to the needs of the program this allows us to program rigidly or flexibly
## according to how we want the user to engage with our code.

########################  EXAMPLE ############################

##########   if re.search(r"^.+@.+\.edu$", email):
##########    print("Valid")

##############################################################


###################### Another Example #######################

########## if re.search(r"^[^@]+@[^@]+\.edu$", email):
##########    print("Valid")

#### In this example we can see that there is use of [] and [^] in order to format the string even further to
            #### [] allow you to look for characters specifically and match
                #### [^] means that you can look for characters specifically and not match
#### Remember that backslash \ is for escaping the string and starting a new one or you can use a modifier to create a new heading, line, paragraph, indent....
#### In the above code we are matching only one at sign and then looking again at the other side of the comparison to be complete because the module splits the argument and you need symetry.
####

