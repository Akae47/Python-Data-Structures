import sys


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


class Tree:
    def __init__(self, key):
        self.root = None
        key = self.clean(key.lower())
        for ch in key:
            if ch == ' ' or self.isValidLetter(ch):
                self.insert(ch)

    def insert(self, ch):
        if self.root is None:
            self.root = Node(ch)
        else:
            self.insert_helper(self.root, ch)

    def insert_helper(self, node, ch):
        if ch < node.ch:
            if node.left is None:
                node.left = Node(ch)
            else:
                self.insert_helper(node.left, ch)
        elif ch > node.ch:
            if node.right is None:
                node.right = Node(ch)
            else:
                self.insert_helper(node.right, ch)

    def encrypt(self, message):
        message = self.clean(message.lower())
        encrypted = ''
        for ch in message:
            if ch == ' ' or self.isValidLetter(ch):
                encrypted += self.encrypt_ch(ch) + '!'
        return encrypted[:-1]

    def encrypt_ch(self, ch):
        return self.encrypt_ch_helper(self.root, ch)

    def encrypt_ch_helper(self, node, ch):
        if node is None:
            return ''
        if ch == node.ch:
            return '*'
        elif ch < node.ch:
            return '<' + self.encrypt_ch_helper(node.left, ch)
        else:
            return '>' + self.encrypt_ch_helper(node.right, ch)

    def decrypt(self, codes_string):
        codes = codes_string.split('!')
        decrypted = ''
        for code in codes:
            decrypted += self.decrypt_code(code)
        return decrypted

    def decrypt_code(self, code):
        node = self.root
        for ch in code:
            if ch == '<':
                node = node.left
            elif ch == '>':
                node = node.right
            else:
                break
        return node.ch

    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if self.isValidCh(text[i]):
                cleanText += text[i]
        return cleanText

    def isValidLetter(self, ch):
        if ch >= "a" and ch <= "z":
            return True
        return False

    def isValidCh(self, ch):
        if ch == " " or self.isValidLetter(ch):
            return True
        return False


def main():
    debug = True  # Set to False before submitting
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # Read the input lines
    key = in_data.readline().strip()

    # Create a Tree object
    key_tree = Tree(key)

    # Read string to be encrypted
    text_message = in_data.readline().strip()

    # Print the encryption
    print(key_tree.encrypt(text_message))

    # Read the string to be decrypted
    coded_message = in_data.readline().strip()

    # Print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
