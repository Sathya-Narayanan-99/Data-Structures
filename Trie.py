class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = '*'

    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        if '*' in cur:
            return True
        return False


if __name__ == '__main__':
    trie = Trie()
    trie.add('hello')
    trie.add('hi')
    print(trie.search('hello'))
    print(trie.search('hey'))
