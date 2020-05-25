'''
4.Create a function showStudent() in such a way that it should accept student id, name, and it’s college name
and if the id and college name is missing in function call it should show it as by default id is 1 and college name  is VITA.
'''

def showStudent(name,id=1,college_name='VITA'):
    print(f"id={id}\nname={name}\ncollege name={college_name}")



showStudent("Mukund")
showStudent("Mangesh",10,"Nowrosjee Wadia College Pune")