class Directory:
    root = None
    parent_dir = None

    def __init__(self, name, root, parent_dir, sub_directories):
        self.name = name
        self.root = root
        self.parent_dir = parent_dir
        self.sub_directories = sub_directories
        self.size = 0
        self.files = []


class Directory_System:
    root = None
    active_directory = None
    sum_at_most_100000 = 0
    total_space = 70_000_000
    smallest_dir_to_update = None

    def build_directory(self, input_lines):
        while True:
            if not input_lines:
                break

            line = input_lines.pop(0).strip().split(' ')
            if line[0] == '$':
                if line[1] == 'cd':
                    if not self.active_directory:
                        self.active_directory = Directory(line[2], None, None, [])
                        self.root = self.active_directory
                        # print('created root directory', self.active_directory.name)
                    elif line[2] == '..':
                        self.active_directory = self.active_directory.parent_dir
                        # print('moved back one directory', self.active_directory.name)
                    else:
                        for sub_dir in self.active_directory.sub_directories:
                            if sub_dir.name == line[2]:
                                self.active_directory = sub_dir
                                # print('moved into directory', self.active_directory.name)
                elif line[1] == 'ls':
                    pass
            elif line[0] == 'dir':
                self.active_directory.sub_directories.append(Directory(line[1], self.root, self.active_directory, []))
                # print('created directory', line[1], 'into ', self.active_directory.name)
            else:
                self.active_directory.files.append([line[1], int(line[0])])
                self.add_size_to_directory_structure(self.active_directory, int(line[0]))
                # print('added file', line[1], 'into ', self.active_directory.name)

    def add_size_to_directory_structure(self, active_dir, size):
        active_dir.size += size
        if active_dir.parent_dir is None:
            return
        self.add_size_to_directory_structure(active_dir.parent_dir, size)

    def print_directory_root(self):
        print('*', self.root.name, self.root.size)
        self.print_directory(2, self.root)

    def print_directory(self, cont, dir):
        if len(dir.sub_directories) == 0:
            return
        for sub_dir in dir.sub_directories:
            print('*' * cont, sub_dir.name, 'size= ', sub_dir.size)
            for file in sub_dir.files:
                print('|' * cont, file[0], file[1])

            self.print_directory(cont + 1, sub_dir)

    def find_sum_at_most_100000(self):
        self.sum_at_most_100000 = 0
        self.sum_at_most(self.root)

    def sum_at_most(self, dir):
        if len(dir.sub_directories) == 0:
            return
        for sub_dir in dir.sub_directories:
            if sub_dir.size <= 100_000:
                self.sum_at_most_100000 += sub_dir.size
            self.sum_at_most(sub_dir)

    def find_smallest_dir(self, update_size):
        self.smallest_dir_to_update = self.root
        missing_space = update_size - (self.total_space - self.root.size)
        self.smallest_dir(self.root, missing_space)

    def smallest_dir(self, dir, missing_space):
        if len(dir.sub_directories) == 0:
            if self.smallest_dir_to_update.size > dir.size >= missing_space:
                self.smallest_dir_to_update = dir
            return
        for sub_dir in dir.sub_directories:
            if self.smallest_dir_to_update.size > sub_dir.size >= missing_space:
                self.smallest_dir_to_update = sub_dir
            self.smallest_dir(sub_dir, missing_space)


f = open('input.txt', 'r')
directory_system = Directory_System()
directory_system.build_directory(f.readlines())
# directory_system.print_directory_root()
directory_system.find_sum_at_most_100000()
print(directory_system.sum_at_most_100000)
directory_system.find_smallest_dir(30_000_000)
print(directory_system.smallest_dir_to_update.size)

f.close()
