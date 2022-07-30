class Company:
    def __init__(self):
        print("in class constructor")
    class Employee:
        def __init__(self):
            print("in Employee Constructor")
        def m1(self):
            print("in m1")
            print("="*10)
comp_obj = Company()
employee = comp_obj.Employee()
employee.m1()

Company().Employee().m1()