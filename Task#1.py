#Создайте метод add для сложения двух стран. Этот метод должен создать еще один объект страны 
#с объединенными названиями двух стран и суммированным населением двух стран.

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self,other_country):
        countries = f"{self.name} {other_country.name}"
        population = self.population + other_country.population
        return Country(countries , population)


    


Bosnia = Country('Bosnia', 10_000_000)
Herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = Bosnia.add(Herzegovina)

print(f"Name: {bosnia_herzegovina.name}")
print(f"Population: {bosnia_herzegovina.population}")
#bosnia_herzegovina.population -> 15_000_000
#bosnia_herzegovina.name -> 'Bosnia Herzegovina'
