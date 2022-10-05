#!/usr/bin/env python
# coding: utf-8

# In[10]:

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    if keyword == 'a' or keyword == 'A':
        return plaintext
    if len(keyword)<len(plaintext):
        add = len(plaintext)-len(keyword*(len(plaintext)//len(keyword)))
        keyword=keyword*(len(plaintext)//len(keyword))+keyword[:add]
    keyword=keyword.lower()
    for i in range(len(plaintext)):
        if ord(plaintext[i])>=65 and ord(plaintext[i])<=90:
            over = bool((ord(plaintext[i])+(ord(keyword[i])-97))//91)
            ciphertext+=chr(ord(plaintext[i])+(ord(keyword[i])-97)-(90-65+1)*int(over))
        elif ord(plaintext[i])>=97 and ord(plaintext[i])<=122:
            over = bool((ord(plaintext[i])+(ord(keyword[i])-97))//123)
            ciphertext+=chr(ord(plaintext[i])+(ord(keyword[i])-97)-(122-97+1)*int(over))
        else:
            ciphertext+=plaintext[i]
    return ciphertext


# In[23]:


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    if keyword == 'a' or keyword == 'A':
        return ciphertext
    if len(keyword)<len(ciphertext):
        add = len(ciphertext)-len(keyword*(len(ciphertext)//len(keyword)))
        keyword=keyword*(len(ciphertext)//len(keyword))+keyword[:add]
    keyword=keyword.lower()
    for i in range(len(ciphertext)):
        if ord(ciphertext[i])>=65 and ord(ciphertext[i])<=90:
            over = not bool((ord(ciphertext[i])-(ord(keyword[i])-97))//65)
            plaintext+=chr(ord(ciphertext[i])-(ord(keyword[i])-97)+(90-65+1)*int(over))
        elif ord(ciphertext[i])>=97 and ord(ciphertext[i])<=122:
            over = not bool((ord(ciphertext[i])-(ord(keyword[i])-97))//97)
            plaintext+=chr(ord(ciphertext[i])-(ord(keyword[i])-97)+(122-97+1)*int(over))
        else:
            plaintext+=ciphertext[i]
    return plaintext

