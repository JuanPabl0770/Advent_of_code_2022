class CrateSorter():

    def __init__(self, input):

        self.crates = {}
        self.procedure_steps = []

        while True:  # loop to iterate through crates
            input_line = input.readline().replace('\n', '')
            if not input_line:
                break

            for i in range(len(input_line)):
                if 65 <= ord(input_line[i]) <= 90:
                    crate_stack = ((i + 1) // 4) + 1
                    if crate_stack in self.crates:
                        self.crates[crate_stack].insert(0, input_line[i])
                    else:
                        self.crates[crate_stack] = [input_line[i]]

        while True:  # loop to iterate though procedure steps
            input_line = input.readline().strip()
            if not input_line:
                break

            input_line = input_line.replace('move ', '')
            input_line = input_line.replace('from ', '')
            input_line = input_line.replace('to ', '')

            self.procedure_steps.append(input_line.split(' '))

    def run_procedure(self):
        for step in self.procedure_steps:
            for i in range(int(step[0])):
                value = self.crates[int(step[1])].pop()
                self.crates[int(step[2])].append(value)

    def run_procedure_9001(self):
        for step in self.procedure_steps:
            crate_height = len(self.crates.get(int(step[1])))
            crates_stack = self.crates.get(int(step[1]))[crate_height-int(step[0]):]
            for i in range(int(step[0])):
                self.crates.get(int(step[1])).pop()
            self.crates.get(int(step[2])).extend(crates_stack)

    def get_top_crates(self):
        top_crates_str = ''
        for i in range(len(self.crates.keys())):
            top_crates_str += self.crates.get(i+1).pop()
        return top_crates_str


f = open('input.txt', 'r')
crate_sorter = CrateSorter(f)
# crate_sorter.run_procedure()
crate_sorter.run_procedure_9001()
print(crate_sorter.get_top_crates())
f.close()
