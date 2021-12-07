"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
import my_module.classes as classes
import my_module.functions as functions

###
###

# PYTHON SCRIPT HERE
def main():
    print("Welcome to the user information based encryption system.")
    print("Please login and create encryption key by letting me know a little more about you.\n")
    
    # input user information and use it to construct data used for encryption and decryption
    user_info = classes.EncryptionInfo()
    user_info.login()
    seed = functions.compute_seed(user_info)
    table = functions.generate_table(seed)
    decrypt_table = functions.get_reversed_table(table)
    m = 256
    b = seed // m
    a = functions.find_coprime_based_on_num(seed % m, m)
    a_inverse = functions.find_inverse_a(a, m)
    
    
    
    print("Login succeed.")
    
    while(True):
        what_to_do = int(input("What do you want to do? 1 for encrypt, 2 for decryption, 3 for quit.\n"))
        
        # encrypt
        if(what_to_do == 1):
            what_to_use = int(input("Which algorithm do you want to use? 1 for substitution cipher, 2 for affine cipher.\n"))
            # substitution
            if(what_to_use == 1):
                text = input("Please input the text to be encrypted: \n")
                encrypted_text = functions.substitution_cipher(table, text)
                print(encrypted_text)
            # affine
            elif(what_to_use == 2):
                text = input("Please input the text to be encrypted: \n")
                encrypted_text = functions.affine_cipher_encrypt(text, a, b, m)
                print(encrypted_text)
            else:
                print("Please choose a valid algorithm to use.\n")
        # decrypt
        elif(what_to_do == 2):
            what_to_use = int(input("Which algorithm do you want to use? 1 for substitution cipher, 2 for affine cipher.\n"))
            # substitution
            if(what_to_use == 1):
                text = input("Please input the text to be decrypted: \n")
                decrypted_text = functions.substitution_cipher(decrypt_table, text)
                print(decrypted_text)
            # affine
            elif(what_to_use == 2):
                text = input("Please input the text to be decrypted: \n")
                decrypted_text = functions.affine_cipher_decrypt(text, a_inverse, b, m)
                print(decrypted_text)
            else:
                print("Please choose a valid algorithm to use.\n")
        # quit
        elif(what_to_do == 3):
            print("Thank you and see you next time!")
            return
        else:
            print("Please give a valid command to do.\n")
        
main()