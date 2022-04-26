import csv
import json
import os
from cars_filter import *
if __name__ == "__main__":
    def writer_function(path,type_car):
        with open(path, 'w') as json_file:
            json.dump(type_car, json_file, indent=2)
    writer_function('output_data/slow_cars.json',slow_cars)
    writer_function('output_data/fast_cars.json', fast_cars)
    writer_function('output_data/sport_cars.json', sport_cars)
    writer_function('output_data/cheap_cars.json', cheap_cars)
    writer_function('output_data/medium_cars.json', medium_cars)
    writer_function('output_data/expensive_cars.json', expensive_cars)
    writer_function('output_data/opel_cars.json', opel_cars)
    writer_function('output_data/ford_cars.json', ford_cars)
    writer_function('output_data/mazda_cars.json', mazda_cars)

