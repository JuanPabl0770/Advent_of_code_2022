class RopeSimulator:
    tail_visited = set()
    rope = [[0, 0] for i in range(10)]
    head = rope[0]

    def follow_motions(self, motions):

        self.tail_visited.add((0, 0))

        for motion in motions:

            direction, steps = motion.strip().split()

            is_tail = False

            for i in range(len(self.rope) - 1):

                if i + 1 == len(self.rope) - 1:
                    is_tail = True

                knot_1 = self.rope[i]
                knot_2 = self.rope[i+1]
                
                if direction == 'R':
                    for i in range(int(steps)):
                        knot_1[0] +=  1
                        self.follow_head(knot_1, knot_2, is_tail)
                    
                elif direction == 'L':
                    for i in range(int(steps)):
                        knot_1[0] -=  1
                        self.follow_head(knot_1, knot_2, is_tail)

                elif direction == 'U':
                    for i in range(int(steps)):
                        knot_1[1] +=  1
                        self.follow_head(knot_1, knot_2, is_tail)

                elif direction == 'D':
                    for i in range(int(steps)):
                        knot_1[1] -=  1
                        self.follow_head(knot_1, knot_2, is_tail)

    def follow_head(self, knot_1, knot_2, is_tail):

        if knot_2[1] == knot_1[1]:
            if  knot_2[0] + 2 == knot_1[0]:
                knot_2[0] = knot_1[0] - 1
                
            if knot_2[0] - 2 == knot_1[0]:
                knot_2[0] = knot_1[0] + 1
                
        #y axis
        elif knot_2[0] == knot_1[0]:
            if knot_2[1] + 2 == knot_1[1]:
                knot_2[1] = knot_1[1] - 1
                
            if knot_2[1] - 2 == knot_1[1]:
                knot_2[1] = knot_1[1] + 1
                

        #diag right y
        elif knot_2[0] + 1 == knot_1[0]:
            #diag right up
            if knot_2[1] + 2 == knot_1[1]:
                knot_2[0] = knot_1[0]
                knot_2[1] = knot_1[1] - 1
                
            #diag right down
            if knot_2[1] - 2 == knot_1[1]:
                knot_2[0] = knot_1[0]
                knot_2[1] = knot_1[1] + 1
                
        
        #diag left y
        elif knot_2[0] - 1 == knot_1[0]:
            #diag left up
            if knot_2[1] + 2 == knot_1[1]:
                knot_2[0] = knot_1[0]
                knot_2[1] = knot_1[1] - 1
                
            #diag left down
            if knot_2[1] - 2 == knot_1[1]:
                knot_2[0] = knot_1[0]
                knot_2[1] = knot_1[1] + 1
                

        #diag right x
        elif knot_2[1] + 1 == knot_1[1]:
            #diag right up
            if knot_2[0] + 2 == knot_1[0]:
                knot_2[1] = knot_1[1]
                knot_2[0] = knot_1[0] - 1

            #diag right down
            if knot_2[0] - 2 == knot_1[0]:
                knot_2[1] = knot_1[1]
                knot_2[0] = knot_1[0] + 1
        
        #diag left x
        elif knot_2[1] - 1 == knot_1[1]:
            #diag left up
            if knot_2[0] + 2 == knot_1[0]:
                knot_2[1] = knot_1[1]
                knot_2[0] = knot_1[0] - 1

            #diag left down
            if knot_2[0] - 2 == knot_1[0]:
                knot_2[1] = knot_1[1]
                knot_2[0] = knot_1[0] + 1
        
        if is_tail:
            self.tail_visited.add((knot_2[0], knot_2[1]))
                

            

f = open('day09\input.txt', 'r')
ropeSimulator = RopeSimulator()
ropeSimulator.follow_motions(f.readlines())
print( len(ropeSimulator.tail_visited), ropeSimulator.tail_visited)
f.close()