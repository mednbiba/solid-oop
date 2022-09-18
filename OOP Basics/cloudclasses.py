
#Following freeCodeCamp.org Tutorial
#Basic Class Definition
class cloudprovider:
    #Class Attribute
    discount_rate=0.8
    all=[]

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
        #print("cloud provider object instance created")

        #Actions 
        cloudprovider.all.append(self)

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
        self.subprice=self.subprice*self.discount_rate
        return("new price ="+str(self.subprice))

    #python doc : best practice for representation
    def __repr__(self) -> str:
        return f"Cloud('{self.name}','{self.subprice}')"


cloud1=cloudprovider("Azure","b","c",100)
cloud2=cloudprovider("AWS","b","c",100)
cloud3=cloudprovider("ALIBABA","b","c",100)
cloud4=cloudprovider("DigitalOcean","b","c",100)
cloud5=cloudprovider("Heroku","b","c",100)

print(cloudprovider.all)

