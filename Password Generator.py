import random 
import string  
password_len = 12 
charValue = string.ascii_letters + string.punctuation +  string.digits
#list comprehension
password = "".join([random.choice(charValue) for i in range(password_len)])     
print(f"The Password is: {password}")     


