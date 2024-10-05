# import re
# a=input("Enter your number")
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print("Valid Number")
# else:
#     print("Invalid Number")



# import re
# a=input("Enter email")
# if re.search('^[a-z].*@gmail.com$',a):
#     print("Valid Email")
# else:
#     print("Invalid Email")  

import re
a=input("Enter password")
if len(a)>=8 and re.search('^[A-z0-9].*[0-9@#$%&]',a) and not(a.isdigit()):
    print("valid")
else: 
    print("Invalid")