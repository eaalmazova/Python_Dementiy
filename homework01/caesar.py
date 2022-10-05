#!/usr/bin/env python
# coding: utf-8


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for char in plaintext:
        if ord(char)>=65 and ord(char)<=90:
            over = bool((ord(char)+shift)//91)
            ciphertext+=chr(ord(char)+shift-(90-65+1)*int(over))
        elif ord(char)>=97 and ord(char)<=122:
            over = bool((ord(char)+shift)//123)
            ciphertext+=chr(ord(char)+shift-(122-97+1)*int(over))
        else:
            ciphertext+=char
    return ciphertext


# In[5]:


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        if ord(char)>=65 and ord(char)<=90:
            over = not bool((ord(char)-shift)//65)
            plaintext+=chr(ord(char)-shift+(90-65+1)*int(over))
        elif ord(char)>=97 and ord(char)<=122:
            over = not bool((ord(char)-shift)//97)
            plaintext+=chr(ord(char)-shift+(122-97+1)*int(over))
        else:
            plaintext+=char
    return plaintext


