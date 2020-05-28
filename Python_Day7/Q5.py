'''

Within university there are several departments are available
Without existing university there is no chance of existance of departments.
Department should strongly associate with university.

University(container object-->the object which holds other object) Vs Department(contained object) ===>Strong association

This type of strong association between objects is nothing but composition.

Without existing container object there is no chance of existance of contained object,
then container object and contained object are strongly associated
and if you delete the container object then all of its contained objects are also deleted.

'''
class Department:
    def __init__(self,depname,building_no):
        self.depname=depname
        self.building_no=building_no

    def display(self):
        return(self.depname,self.building_no)


class University:
    def __init__(self,uni_name,depname,building_no):
        self.uni_name=uni_name
        self.obj_department=Department(depname,building_no)
    def display(self):
        return self.obj_department.display()

u=University("Pune Univeristy","Physics Department",15)
print(u.display())


