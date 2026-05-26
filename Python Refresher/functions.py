"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values

"""


def names(fname,mname,lname):
    name_dict = {}
    name_dict["First Name"] = fname
    name_dict["Middle Name"] = mname
    name_dict["Last Name"] = lname
    return name_dict

name_dict = names("Mahendra", "Singh", "Dhoni")
print(name_dict)