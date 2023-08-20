"""# DataLoader

This exercise has a file called laptop.txt attached. This file contain information about laptops in key: value pairs.

## Create a class named DataLoader, which:

-   Takes one argument: filename which is name of data file to load, e.g laptop.txt
-   Provide following methods:
    -   toDict
            This function should return the data of the filename provided to class constructor in the form of a Python dictionary
    -   toList
            This funtion should return the dat of the filename provided to class constructor as a list of tuples. i.e it should return a list,
             which contain tuples of (key, value)

## create a test file which test both the methods of the DataLoader class"""

class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def toDict(self):
        data_dict = {}
        with open(self.filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                data_dict[key] = value
        return data_dict

    def toList(self):
        data_list = []
        with open(self.filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                data_list.append((key, value))
        return data_list

loader = DataLoader('laptops.txt')
x = loader.toDict()
y = loader.toList()
print(x)
print(y)

