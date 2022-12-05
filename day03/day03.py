import numpy as np

class Rucksack_sorter():
    def get_repeated_item_value(self, rucksack):

        chunks, chunk_size = len(rucksack), len(rucksack) // 2
        compartment1, compartment2 = [rucksack[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for char in compartment1:
            if char in compartment2:
                if char.islower():
                    return ord(char) - 96
                if char.isupper():
                    return ord(char) - 38

    def get_sum_of_priorities(self, rucksacks):
        sum = 0
        for rucksack in rucksacks:
            sum += self.get_repeated_item_value(rucksack)
        return sum

    def get_sum_of_badge_priorities(self, rucksacks):
        sum = 0
        for i in range(len(rucksacks)//3):
            group = [rucksacks[i*3], rucksacks[(i*3)+1], rucksacks[(i*3)+2]]
            found = False
            for char in group[0]:
                if char in group[1] and char in group[2] and not found:
                    found = True
                    if char.islower():
                        sum+= ord(char) - 96
                    if char.isupper():
                        sum+= ord(char) - 38
        return sum


f = open('input.txt', 'r')
rucksacks = []
for line in f:
    rucksacks.append(line.strip())

rucksack_sorter = Rucksack_sorter()
print('#1 the sum of the priorities for repeated item is: ', rucksack_sorter.get_sum_of_priorities(rucksacks))
print('#2 the sum of the priorities for elf groupe is: ', rucksack_sorter.get_sum_of_badge_priorities(rucksacks))