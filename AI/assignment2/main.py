import aim.csp as csp

class Problem(csp.CSP):

    def __init__(self, fh):
        # Place here your code to load problem from opened file object fh and
        # set variables, domains, graph, and constraint_function accordingly
        super().__init__(variables, domains, graph, constraints_function)

    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        pass


    def read_input_data(self, path):
        """
        describe function here:
        :param path:
        :return:
        """
        # create file object
        file = open(path)

        # creates a list of input file. removes \n
        filelines = file.read().splitlines()

        print(filelines)

        # adds timetable slots to list T
        timetable_slot_list = filelines[0].split(' ')
        del timetable_slot_list[0]
        T = []
        for el in timetable_slot_list:
            T.append((el.split(',')[0], el.split(',')[1]))

        # adds rooms to list R
        rooms_list = filelines[1].split(' ')
        del rooms_list[0]
        R = []
        for el in rooms_list:
            R.append(el)

        # adds student classes to list S
        student_classes_list = filelines[2].split(' ')
        del student_classes_list[0]
        S = []
        for el in student_classes_list:
            S.append(el)

        # adds weekly classes to W
        weekly_classes_list = filelines[3].split(' ')
        del weekly_classes_list[0]
        W = []
        for el in weekly_classes_list:
            W.append((el.split(',')[0], el.split(',')[1], el.split(',')[2]))

        # adds associations to list A
        associations_list = filelines[3].split(' ')
        del associations_list[0]
        A = []
        for el in associations_list:
            A.append((el.split(',')[0], el.split(',')[1]))


def solve(input_file, output_file):
    p = Problem(input_file)
    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.dump_solution(output_file)


def read_input_data(path):
    """
    :param path:
    :return:
    """
    #
    file = open(path)

    # creates a list of input file. removes \n
    filelines = file.read().splitlines()

    print(filelines)

    # adds timetable slots to list T
    timetable_slot_list = filelines[0].split(' ')
    del timetable_slot_list[0]
    T = []
    for el in timetable_slot_list:
        T.append((el.split(',')[0], el.split(',')[1]))

    # adds rooms to list R
    rooms_list = filelines[1].split(' ')
    del rooms_list[0]
    R = []
    for el in rooms_list:
        R.append(el)

    # adds student classes to list S
    student_classes_list = filelines[2].split(' ')
    del student_classes_list[0]
    S = []
    for el in student_classes_list:
        S.append(el)

    # adds weekly classes to W
    weekly_classes_list = filelines[3].split(' ')
    del weekly_classes_list[0]
    W = []
    for el in weekly_classes_list:
        W.append((el.split(',')[0], el.split(',')[1], el.split(',')[2]))

    # adds associations to list A
    associations_list = filelines[3].split(' ')
    del associations_list[0]
    A = []
    for el in associations_list:
        A.append((el.split(',')[0], el.split(',')[1]))


if __name__ == "__main__":
    path = "./input1.txt"
    read_input_data(path)
