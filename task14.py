class iterator:    
    """_summary_
    """    
    def __init__(self, countries_with_cities, list_of_cities):
        self.countries_with_cities = countries_with_cities
        self.list_of_cities = list_of_cities
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self) -> tuple:   
        if self.count < len(self.list_of_cities):
            city = self.list_of_cities[self.count]
            self.count += 1
            return self.list_of_cities[self.count - 1], self.countries_with_cities.get(city) 
        raise StopIteration  
        
def reverse(countries_with_cities) -> dict:
    new_dict = dict()
    for k, v in countries_with_cities.items():
        for city in v:
            new_dict[city] = k
    return new_dict            
    
countries_with_cities = {
    'Россия': ['Москва', 'Санкт-Петербург', 'Новосибирск'],
    'США': ['Нью-Йорк', 'Лос-Анджелес', 'Чикаго'],
    'Франция': ['Париж', 'Марсель', 'Лион'],
    'Германия': ['Берлин', 'Мюнхен', 'Гамбург'],
}

list_of_cities = ["Москва", "Санкт-Петербург", "Гамбург", "Париж"]
new_dict = reverse(countries_with_cities)
result = iterator(new_dict, list_of_cities)

for i in result:
    print(f"Город: {i[0]} \t Страна: {i[1]}")

