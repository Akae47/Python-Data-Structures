#  File: BST_Cipher.py
#  Student Name: Akwawo Ekpu
#  Student UT EID: ace2453


import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        self.root = None
        key = self.clean(key.lower())
        for ch in key:
            if ch == ' ' or ('a' <= ch <= 'z'):
                self.insert(ch)

    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        if self.root is None:
            self.root = Node(ch)
        else:
            node = self.root
            while True:
                if ch < node.ch:
                    if node.left is None:
                        node.left = Node(ch)
                        break
                    else:
                        node = node.left
                elif ch > node.ch:
                    if node.right is None:
                        node.right = Node(ch)
                        break
                    else:
                        node = node.right
                else:
                    break

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        message = self.clean(message.lower())
        encrypted = ''
        for ch in message:
            if ch == ' ' or ('a' <= ch <= 'z'):
                encrypted += self.encrypt_ch(ch) + '!'
        return encrypted[:-1]

    # Encrypts a single character
    def encrypt_ch(self, ch):
        node = self.root
        path = ''
        while node is not None:
            if ch == node.ch:
                break
            elif ch < node.ch:
                path += '<'
                node = node.left
            else:
                path += '>'
                node = node.right
        return '*' + path

    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        codes = codes_string.split('!')
        decrypted = ''
        for code in codes:
            decrypted += self.decrypt_code(code)
        return decrypted

    # Decrypts a single code
    def decrypt_code(self, code):
        node = self.root
        if code[1:]:
            for ch in code[1:]:
                if ch == '<' and node.left:
                    node = node.left
                elif ch == '>' and node.right:
                    node = node.right
                else:
                    break
        return node.ch if node else ''

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
