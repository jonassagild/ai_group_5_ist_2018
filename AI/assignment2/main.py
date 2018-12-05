import copy
import aim.csp as csp


class Problem(csp.CSP):
    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly
        self.read_input_data(fh)
        self.create_variables()
        self.create_domain()
        self.create_neighbors()

        super().__init__(self.variables, self.domains, self.neighbors, self.constraints_function)

    def dump_solution(self, fh, assignment):
        # Place here your code to write solution to opened file object fh
        solution = "";
        for key in assignment:
            solution = solution + key[0] + ',' + key[1] + ',' + key[2] + ' ' + assignment[key][1][0] + ',' + \
                       assignment[key][1][1] + ' ' + assignment[key][0] + "\n"

        fh.write(solution)

    def read_input_data(self, path):
        """
        Reads the input data and saves it to the variables as defined in the project description
        :param path:
        :return:
        """
        # create file object
        file = path

        # creates a list of input file. removes \n
        filelines = file.read().splitlines()

        # adds timetable slots to list T
        timetable_slot_list = filelines[0].split(' ')
        del timetable_slot_list[0]
        self.T = []
        for el in timetable_slot_list:
            self.T.append((el.split(',')[0], el.split(',')[1]))

        # adds rooms to list R
        rooms_list = filelines[1].split(' ')
        del rooms_list[0]
        self.R = []
        for el in rooms_list:
            self.R.append(el)

        # adds student classes to list S
        student_classes_list = filelines[2].split(' ')
        del student_classes_list[0]
        self.S = []
        for el in student_classes_list:
            self.S.append(el)

        # adds weekly classes to W
        weekly_classes_list = filelines[3].split(' ')
        del weekly_classes_list[0]
        self.W = []
        for el in weekly_classes_list:
            self.W.append((el.split(',')[0], el.split(',')[1], el.split(',')[2]))

        # adds associations to list A
        associations_list = filelines[4].split(' ')
        del associations_list[0]
        self.A = []
        for el in associations_list:
            self.A.append((el.split(',')[0], el.split(',')[1]))

        self.D = {}
        for association in self.A:
            if self.D.get(association[1], False):
                self.D[association[1]].add(association[0])
            else:
                self.D[association[1]] = {association[0]}

    def create_domain(self):
        """
        method creates the domains of each variable.
        domains: A dict of {var:[possible_value, ...]} entries.
        """
        # TODO: for each variable, create the domain
        # TODO: The domain is the cartesian product of rooms and timetable slots

        # creates the domain
        domain = []
        for room in self.R:
            for timetableslot in self.T:
                domain.append((room, timetableslot))

        self.domains = {}
        # creates the domain dict. Each domain is unique, so we need to use deepcopy
        # Since only one class can be connected to one timetableslot, we do not have to do deepcopy.
        # (not 100% sure of this) If any of the methods in the csp removes parts of the domain after e.g. forward
        # checking, then this will end up wrong.
        # TODO: ask teacher about this! (Or just check yourself)
        for variable in self.variables:
            domain_copy = copy.deepcopy(domain)
            self.domains[variable] = domain_copy

    def create_variables(self):
        """
        method creates the variables. The variables are the tuples containes in W.
        variables: A list of variables; each is atomic (e.g. int or string).
        :return: none
        """
        self.variables = self.W

    def create_neighbors(self):
        """

        :return: none
        """

        self.neighbors = {}

        for var in self.variables:
            neighbors = []
            neighbors = copy.deepcopy(self.variables)
            neighbors.remove(var)
            self.neighbors[var] = neighbors

    def constraints_function(self, A, a, B, b):
        """
        A function f(A, a, B, b) that returns true if neighbors A, B satisfy the constraint when they have values A=a, B=b
        :param A:
        :param a:
        :param B:
        :param b:
        :return: True or False
        """
        # • each room can only hold one class at a time
        if a == b:
            return False

        # • each student class can only attend one class at a time
        # checks if the assigned times are the same
        if a[1] == b[1]:
            # checks if some of the student classes are the same for this class
            if self.D[A[0]] & self.D[B[0]]:
                return False

        # checks if the student class and the type is the same
        if A[0] == B[0] and A[1] == B[1]:
            # checks if its the same weekday
            if a[1][0] == b[1][0]:
                return False

        # if nothing is false, then all constraints are true
        return True


def solve(input_file, output_file):
    p = Problem(input_file)
    # csp.backtracking_search(p,p.domains)
    # Place here your code that calls function csp.backtracking_search(self, ...)
    assignment = csp.backtracking_search(p)

    p.dump_solution(output_file, assignment)


if __name__ == "__main__":
    input_path = "./input1.txt"
    input_file = open(input_path)

    output_path = "./output1.txt"
    output_file = open(output_path, 'w')
    solve(input_file, output_file)
