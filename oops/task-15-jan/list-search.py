#q1 : Create your own class to perform a list search operation 
class ListSearch:
    def __init__(self):
        self.list=[]
        
    def setList(self):
        lengthOfLement = input("Enter number of element :")
        for i in range(int(lengthOfLement)):
            self.list.append(input("Enter data:"))

        return self.list

    def search(self, find):
        if find in self.list:
            return "Your Element Present!"
        else:
            return "Your Element Not Present!"


obj = ListSearch()
# obj.setList()
# output = obj.search(input("Please enter the value:"))
# print(output)


# q2 : create a class for dict new element addition
class AddToDict:
    def __init__(self):
        self.dict={}
        
    def setDict(self):
        self.dict.update({'key':'value'})

        return self.dict

obj2 = AddToDict()
# output2 = obj2.setDict()
# print(output2)