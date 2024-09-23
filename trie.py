class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print(f'Inserted: {word}')
        self.display()

    def delete(self, word):
        if self._delete_helper(self.root, word, 0):
            print(f'Deleted: {word}')
        else:
            print(f'Word not found: {word}')
        self.display()

    def _delete_helper(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        can_delete_child = self._delete_helper(node.children[char], word, index + 1)

        if can_delete_child:
            del node.children[char]
            return len(node.children) == 0

        return False

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def display(self, node=None, word='', level=0):
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print(' ' * level + f'*- {word}')
        for char, child_node in node.children.items():
            self.display(child_node, word + char, level + 1)

if __name__ == "__main__":
    trie = Trie()

    while True:
        operation = input("Enter operation (insert, delete, search, exit): ").strip().lower()
        if operation == 'exit':
            break
        elif operation in ['insert', 'delete', 'search']:
            word = input("Enter the word: ").strip()
            if operation == 'insert':
                trie.insert(word)
            elif operation == 'delete':
                trie.delete(word)
            elif operation == 'search':
                found = trie.search(word)
                print(f'Search result for "{word}":', 'Found' if found else 'Not Found')
        else:
            print("Invalid operation. Please try again.")
