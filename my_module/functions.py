import random as rand

"""A collection of function for doing my project."""

def generate_table(random_seed):
    """
    Description:
    generate a table that maps from unecrypted characters from alphabet to encrypted character using the given seed

    Parameters:
        random_seed = a integer that is the random seed for generating the substitution table

    Return:
        dictionary, a table that maps from unecrypted characters from alphabet to encrypted character
    """
    rand.seed(random_seed)
    table = {}
    
    # create table that contains all 
    for i in range(0, 256):
        character = chr(i)
        table[character] = character
    
    swap_count = rand.randint(100, 200)
    
    # shuffle the table
    for i in range(0, swap_count):
        # choose two index
        char_0 = chr(rand.randint(0, 255))
        char_1 = chr(rand.randint(0, 255))
        
        # swap
        temp = table[char_0]
        table[char_0] = table[char_1]
        table[char_1] = temp
        
    return table
    

def get_reversed_table(table):
    """
    Description:
    Get the reversed table given the encryption table

    Parameters:
        table = dictionary, the table to be reversed
        
    Return:
        dictionary, a table that is a reversed version of the parameter
    """
    result = {}
    for key in table:
        result[table[key]] = key
    return result
    
def compute_seed(user_info):
    """
    Description:
    compute the random seed with the given user information and a encryption key (which is a positive integer number)

    Parameters:
        user_info = a instance that contains user informations
    """
    result = user_info.age
    for i in range(len(user_info.initials)):
        result = result + ord(user_info.initials[i]) - ord('A')
    for i in range(len(user_info.pet)):
        result = result + ord(user_info.pet[i])
    
    password_num = 1
    for i in range(len(user_info.password)):
        password_num = password_num + ord(user_info.password[i])
    
    result += password_num * user_info.age
    return result


def substitution_cipher(table, text):
    """
    Description:
    Encrypt or decrypt a text string with a encryption/decryption table using substitution

    Parameters:
        table = dictionary, map from encrypted char to decrypted char
        text = string, a text whose characters will be substituted with a table
        
    Return:
        string, a text with substituted characters
    """
    result = ""
    for i in range(0, len(text)):
        if(text[i] in table):
            result += table[text[i]]
        else:
            result += text[i]
    return result
    
    
def check_all_capital(text):
    '''
    Description:
    Check whether all the characters in a string are capital letters

    Parameters:
        str = string, the string to be checked
        info_num = string, the name of the string used for error message

    Return:
        boolean, True for yes and False for no
    '''
    for i in range(len(text)):
        if(text[i] < 'A' or text[i] > 'Z'):
            return False
    return True

def find_gcd(x, y):
    """
    Description:
    find the greatest common divisor of two numbers, by iterating from 1 to the minimum of x and y until find one

    Parameters:
        x = int, the first positive integer number
        y = int, the second positive integer number

    Return:
        int, the greatest common divisor
    """
    if(x > y):
        min = y
    else:
        min = x
    for i in range(min):
        num = i + 1
        if((x % num == 0) and (y % num == 0)):
            gcd = num
              
    return gcd

def find_coprime_based_on_num(num, m):
    '''
    Description:
    Find the coprime of m based on a positive number

    Paramters:
        num = int, a positive number between 1 and m - 1
        m = int, the size of the alphabet
    '''
    # look up
    for i in range(num, m - 1):
        if(find_gcd(i, m) == 1):
            return i
    # look down
    for i in range(1, num):
        if(find_gcd(i, m) == 1):
            return i
    return -1


def affine_cipher_encrypt(text, a, b, m):
    '''
    Description:
        Given positive integer a, b, and m where a and m are coprime, encrypt a text using affine cipher

    Parameters:
        text = string, the text that will be encrypted
        a = int, the factor that each letter will be multiplied by
        b = int, the constant that the letter will be incremented by after the multiplication
        m = int, the size of the alphabet

    Return:
        string, the encrypted text
    '''
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr((a * ord(text[i]) + b) % m)
    return encrypted_text

def find_inverse_a(a, m):
    '''
    Description:
        find the modulo inverse of a, a^-1, so that a * a^-1 % m == 1

    Parameters:
        a = int, a positive integer number whose inverse this function need to find.
        m = int, the size of the alphabet

    Return:
        int, the modulo inverse of a with respect to m
    '''
    for i in range(1, m):
        # greatest common divisor that is 1
        if(a * i % m == 1):
            return i
        
    # return a invalid number
    return -1

def affine_cipher_decrypt(text, a_inverse, b, m):
    '''
    Description:
        Given positive integer a_inverse, b and size of alphabet m, decrypt a text using affine cipher

    Parameters:
        text = string, the text that will be encrypted
        a_inverse = int, a_inverse * a % m == 1 where a is the factor used in encryption
        b = int, the constant that the letter was incremented by after the multiplication during encryption
        m = int, the size of the alphabet

    Return:
        string, the decrypted text
    '''
    result = ""
    for i in range(0, len(text)):
        result += chr(a_inverse * (ord(text[i]) - b) % m)
    return result