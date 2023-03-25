import string
import random

def gen():
    str1 = string.ascii_uppercase                             ## A-Z
    str2 = string.ascii_lowercase                             ## a-z
    str3 = string.digits                                      ## 0-9
    str4 = string.punctuation                                 ## @!#$%^&*()?><":}{+_|\][';/.,]}" etc.
    
    passlength = int(input("Enter the Password length\n"))    ## User Input
    combined_list = []
    combined_list.extend(list(str1))
    combined_list.extend(list(str2))
    combined_list.extend(list(str3))
    combined_list.extend(list(str4))

    random.shuffle(combined_list)                             ## Randomly shuffle the elements of combined_list.
    
    password = ("".join(combined_list[0:passlength]))         
    print(f"Your new Password is:{password}")

gen()