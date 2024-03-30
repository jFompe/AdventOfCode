from hashlib import md5


def read_input(filename: str):
    with open(filename, 'r') as f:
        return f.readline()
    

def find_hash(secret: str, zeroes: int) -> str:
    n = 1
    prefix = '0' * zeroes
    while True:
        hash_key = md5((secret + str(n)).encode())
        if hash_key.hexdigest()[:zeroes] == prefix:
            return n
        n += 1


# Part 1

FILE = 'day4.txt'
secret_key = read_input(FILE)
print(find_hash(secret_key, 5))


# Part 2

print(find_hash(secret_key, 6))
