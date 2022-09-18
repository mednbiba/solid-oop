
#Following freeCodeCamp.org Tutorial
#Basic Class Definition
class cloudprovider:
    #Class Attribute
    discount_rate=0.8

    def __init__(self,name: str,user="",passwd="",subprice:float=0):

        #Validations
        assert len(name)>0,"Name must not be an empty string"
        assert len(user)>0
        assert len(passwd)>0

        #Instance Assignment
        self.name=name
        self.user=user
        self.passwd=passwd
        self.subprice=subprice
        print("cloud provider object instance created")

    def check_name_set(self):
        if(self.name==""):
            return("Cloud Name has not been set properly")
        else:
            return(f"Cloud Name has been set properly:{self.name}")
    def get_pricing_model(self):
        if(self.subprice>0):
            return("Normal Tier")
        else :
            return("Free Tier")
    def apply_discount(self):
        self.subprice=self.subprice*cloudprovider.discount_rate
        return("new price ="+str(self.subprice))


cloud1=cloudprovider("a","b","c",30)

#print(cloudprovider.__dict__) #get class att dictionary 
#print(cloud1.__dict__)      #get instance att dicitionary 
print(cloud1.subprice)
cloud1.apply_discount()
print(cloud1.subprice)
