from typing import List


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent=None) -> None:
        self.parent: Directory = parent
        self.name: str = name
        self.subdirs: List[Directory] = []
        self.files: List[File] = []

    def __getitem__(self, arg):
        if arg == '..':
            return self.parent
        for dir in self.subdirs:
            if dir.name == arg:
                return dir
        return None
    
    def has_file(self, name: str) -> bool:
        for file in self.files:
            if file.name == name:
                return True
        return False
    
    @property
    def size(self):
        return sum(f.size for f in self.files) + sum(d.size for d in self.subdirs)


class OS:
    def __init__(self) -> None:
        self.cwd = Directory('/')

    def cd(self, dir: str) -> None:
        target = self.cwd[dir]
        if target:
            self.cwd = target


def find_underlimit_dirs(limit: int, dir: Directory, sizes: List[int]):
    if dir.size <= limit:
        sizes.append(dir.size)
    for subdir in dir.subdirs:
        find_underlimit_dirs(limit, subdir, sizes)


# Part 1

FILE = 'day7.txt'
with open(FILE, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
os = OS()
root = os.cwd

for line in lines:
    line = line.strip()
    if line.startswith('$'):
        if line.startswith('$ cd'):
            _, cmd, arg = line.split(' ')
            os.cd(arg)
    else:
        d1, d2 = line.split(' ')
        if d1 == 'dir' and not os.cwd[d2]:
            os.cwd.subdirs.append(Directory(d2, os.cwd))
        elif not os.cwd.has_file(d2):
            os.cwd.files.append(File(d2, int(d1)))

overlimit_dirs = []
find_underlimit_dirs(100_000, root, overlimit_dirs)
total_overlimit_size = sum(overlimit_dirs)
print(total_overlimit_size)


# Part 2

all_dirs = []
find_underlimit_dirs(float('inf'), root, all_dirs)
total_disk_space = 70000000
used_space = root.size
unused_space = total_disk_space - used_space
necessary_space = 30000000 - unused_space
space_to_free = min(s for s in all_dirs if s > necessary_space)
print(space_to_free)
