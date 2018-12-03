import copy

import aim.csp as csp


class Problem(csp.CSP):
    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly
        self.read_input_data(fh)
        self.create_variables()
        self.create_domain()
        super().__init__(self.variables, self.domains, self.graph, self.constraints_function)

    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        pass

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

        print(filelines)

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
        associations_list = filelines[3].split(' ')
        del associations_list[0]
        self.A = []
        for el in associations_list:
            self.A.append((el.split(',')[0], el.split(',')[1]))

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


def solve(input_file, output_file):
    p = Problem(input_file)

    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)


if __name__ == "__main__":
    input_path = "./input1.txt"
    input_file = open(input_path)

    output_path = "./output1.txt"
    output_file = open(output_path)
    solve(input_file, output_file)
