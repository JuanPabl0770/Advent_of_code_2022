class Cleaning_parties():

    def fully_contains(self, elve1, elve2):

        elve1 = [int(elve1[0]),int(elve1[1])]
        elve2 = [int(elve2[0]),int(elve2[1])]

        if elve2[0] <= elve1[0] <= elve2[1] and elve2[0] <= elve1[1] <= elve2[1]:
            return True
        elif elve1[0] <= elve2[0] <= elve1[1] and elve1[0] <= elve2[1] <= elve1[1]:
            return True
        return False

    def overlaps(self, elve1, elve2):

        elve1 = [int(elve1[0]), int(elve1[1])]
        elve2 = [int(elve2[0]), int(elve2[1])]

        if elve2[0] <= elve1[0] <= elve2[1]:
            return True
        if elve1[0] <= elve2[0] <= elve1[1]:
            return True
        return False

    def get_total_pairs(self, pairs):

        total_pairs_contained = 0
        total_pairs_overlaped = 0
        for elve1, elve2 in pairs:
            if self.fully_contains(elve1.split('-'), elve2.split('-')):
                total_pairs_contained += 1
            if self.overlaps(elve1.split('-'), elve2.split('-')):
                total_pairs_overlaped += 1
        return total_pairs_contained , total_pairs_overlaped



f = open('input.txt', 'r')
pairs = []
for line in f:
    pairs.append(line.strip().split(','))

cleaning_parties = Cleaning_parties()
print(cleaning_parties.get_total_pairs(pairs))
