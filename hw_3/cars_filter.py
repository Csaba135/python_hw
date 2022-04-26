import csv
cars = []
with open('input.csv') as csv_file:
    reader = csv.reader(csv_file)

    for index, row in enumerate(reader):
        if index == 0:
            keys = row
        else:
            cars.append(dict(zip(keys, row)))
slow_cars = list(filter(lambda car: True if car["HP"] < "120" else False, cars))
fast_cars = list(filter(lambda car: True if car["HP"] >= "120" and car["HP"] < "180" else False, cars))
sport_cars = list(filter(lambda car: True if car["HP"] > "180" else False, cars))
cheap_cars = list(filter(lambda car: True if car["Price"] <= "1000" else False, cars))
medium_cars = list(filter(lambda car: True if car["Price"] >= "1000" and car["Price"] < "5000" else False, cars))
expensive_cars = list(filter(lambda car: True if car["Price"] > "5000" else False, cars))
opel_cars = list(filter(lambda car: True if car["Brand"] == "Opel" else False, cars))
ford_cars = list(filter(lambda car: True if car["Brand"] == "Ford" else False, cars))
mazda_cars = list(filter(lambda car: True if car["Brand"] == "Mazda" else False, cars))