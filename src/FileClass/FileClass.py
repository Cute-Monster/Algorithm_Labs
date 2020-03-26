class File:
    def __init__(self, name, salary, position, working_years, kids, less=None, more=None):
        self.name = name
        self.salary = int(salary)
        self.position = position
        self.working_years = int(working_years)
        self.kids = int(kids)
        self.less = less
        self.more = more

    def __getitem__(self, item):
        print("__getitem__")

    def print_data(self):
        print("\t" + self.name,
              self.salary,
              self.position,
              self.working_years,
              self.kids, sep="\t\t")