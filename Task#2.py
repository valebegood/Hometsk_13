class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self,other):
       return self.name + " " + other.name, self.population + other.population
    
    
    


Bosnia = Country('Bosnia', 10_000_000)
Herzegovina = Country('Herzegovina', 5_000_000)
result = Bosnia  + Herzegovina
print(result[0])
print(result[1])
