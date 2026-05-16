class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Exercício 1
    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end = True

    # Exercício 2
    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end

    # Exercício 3
    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True

    # Exercício 4
    def _collect_words(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)

        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)

    def collect_words(self, prefix=""):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return []

            current = current.children[char]

        result = []

        self._collect_words(current, prefix, result)

        return result

    # Exercício 5
    def autocomplete(self, prefix, k):
        words = self.collect_words(prefix)

        words.sort()

        return words[:k]

    # Exercício 6
    def autocorrect(self, word):
        if self.search(word):
            return word

        best_prefix = ""
        current_prefix = ""

        current = self.root

        for char in word:
            if char in current.children:
                current_prefix += char
                current = current.children[char]
                best_prefix = current_prefix
            else:
                break

        suggestions = self.collect_words(best_prefix)

        if not suggestions:
            suggestions = self.collect_words()

        suggestions.sort()

        return suggestions[0] if suggestions else None
    
trie = Trie()

words = [
    "car",
    "cart",
    "carro",
    "casa",
    "cadeira",
    "cachorro"
]

for w in words:
    trie.insert(w)

print("=== SEARCH ===")
print(trie.search("car"))
print(trie.search("cart"))
print(trie.search("ca"))

print("\n=== PREFIX ===")
print(trie.starts_with("ca"))
print(trie.starts_with("dog"))

print("\n=== COLLECT ===")
print(trie.collect_words())
print(trie.collect_words("car"))

print("\n=== AUTOCOMPLETE ===")
print(trie.autocomplete("ca", 3))

print("\n=== AUTOCORRECT ===")
print(trie.autocorrect("carr"))
print(trie.autocorrect("cade"))
print(trie.autocorrect("zzz"))