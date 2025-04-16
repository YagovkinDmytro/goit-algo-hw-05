class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove(pair)
                    return True
        return None
        
        
        

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("bananaa", 40)
H.insert("bananaaa", 50)
H.insert("bananaaaa", 60)

print(H.get("apple"))   
print(H.get("orange"))  
print(H.get("banana"))
print(H.get("bananaa"))
print(H.get("bananaaa"))
print(H.get("bananaaaa"))
print(H.table)
print(H.delete("bananaaaa"))
print(H.table)
print(H.delete("bananaaa"))
print(H.delete("bananaa"))
print(H.delete("bana"))
print(H.table)
