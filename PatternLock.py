import argparse
from itertools import permutations
import math
from draw import draw_path
from test import test_path

class password():
    def __init__(self, rule):
        self.vertex_dict = {'1':(0,0),'2':(1,0),'3':(2,0),'4':(0,1),'5':(1,1),'6':(2,1),'7':(0,2),'8':(1,2),'9':(2,2)}
        self.paths_with_center = [[['7','9'],'8'],[['4','6'],'5'],[['1','3'],'2'],[['7','1'],'4'],[['8','2'],'5'],[['9','3'],'6'],[['7','3'],'5'],[['9','1'],'5']]
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:

    # Find the longest path
    def find_longest_path(self):
        password_permutations = permutations('123456789')
        if self.rule == 1:
            for permutation in password_permutations:
                permutation_str = ''.join(permutation)
                invalid = False
                for invalid_path in self.paths_with_center:
                    if ''.join(invalid_path[0]) in permutation_str or ''.join(reversed(invalid_path[0])) in permutation_str:
                        invalid = True
                        break
                if invalid:
                    continue
                total = 0
                for i in range(1, len(permutation)):
                    total += self.distance(self.vertex_dict[permutation[i - 1]], self.vertex_dict[permutation[i]])
                if total == self.longest_length:
                    self.longest_path.append(permutation_str)
                if total > self.longest_length:
                    self.longest_length = total
                    self.longest_path = [permutation_str]
        if self.rule == 2:
            for permutation in password_permutations:
                permutation_str = ''.join(permutation)
                invalid = False
                for invalid_path in self.paths_with_center:
                    if ''.join(invalid_path[0]) in permutation_str:
                        index = permutation_str.index(''.join(invalid_path[0]))
                        partial_string = permutation_str[:index]
                        if invalid_path[1] not in partial_string:
                            invalid = True
                            break
                    if ''.join(reversed(invalid_path[0])) in permutation_str:
                        index = permutation_str.index(''.join(reversed(invalid_path[0])))
                        partial_string = permutation_str[:index]
                        if invalid_path[1] not in partial_string:
                            invalid = True
                            break
                if invalid:
                    continue
                total = 0
                for i in range(1, len(permutation)):
                    total += self.distance(self.vertex_dict[permutation[i - 1]], self.vertex_dict[permutation[i]])
                if total == self.longest_length:
                    self.longest_path.append(permutation_str)
                if total > self.longest_length:
                    self.longest_length = total
                    self.longest_path = [permutation_str]

  
    # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PatternLock')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='Index of the rule')
    args = parser.parse_args()

    # usage
    # python PatternLock.py -rule 1
    # python PatternLock.py -rule 2
    
    # Initialize the object using rule 1 or rule 2
    run = password(args.rule)
    # Find the longest path
    run.find_longest_path()
    # Print and save the result
    run.print_result()
    # Draw the first longest path
    run.draw()
    # Verify the result
    run.test()

