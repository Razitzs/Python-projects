class puto:
    def __init__(self,i,novia):
        self.id=i
        self.novia=novia
        self.followers=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

p1=puto("001","ninguna")

print(p1.followers)


