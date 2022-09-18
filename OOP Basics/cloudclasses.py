
#Basic Class Definition
class cloudprovider:
    def __init__(self,name="",user="",passwd="") -> None:
        self.name=name
        self.user=user
        self.passwd=passwd
        print("cloud provider object instance created")

    def check_name_set(self):
        if(self.name==""):
            return("Cloud Name has not been set properly")
        else:
            return(f"Cloud Name has been set properly:{self.name}")


cloud1=cloudprovider("")

print(cloud1.check_name_set())