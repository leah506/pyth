class animal:
    def __init__(self, legs, type, name ):
        self. legs = legs
        self. type = type
        self. name = name
        
    def make_sound(self):
        print(f"{self.name}says{self.sound}")

    def category(self):
        print(f"{self.name} is a{animal.vertebrate}")


anim1 = animal( 2, "bird", "hen")
anim2 = animal( 4, "mammal", "dog")
anim3 = animal(0, "fish", "tilapia")
    

print(anim3.type)










class library:
    def __init__(self, title, author):
        self.title = title
        self. author = author

    def return_book(self):
        print(f"title{self.title}, author: {self.author}, return{self.return_book}")

shelf1 = library("the beginning", "mary.A. ann")
        
print(shelf1.title)











class hospital:
    def __init__(self, number, name, disease):
        self.number = number
        self.name = name
        self.disease = disease
        self.ward = "for i range" 

    def attendance(self):
        print(f"patient{self.number} is called{self.name} suffering from{self.disease} is in ward no:{self.ward}attended{hospital.today}")


    def not_seriosly_sick():
        print("not to be admitted")

pat1 = hospital(1, "angeline isaack" "typhoid") 

print(pat1.ward)
