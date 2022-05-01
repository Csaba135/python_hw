from collections import defaultdict
from helpers.data_types import AvailableFileTypes
from .file_workers import CSVWorker, JSONWorker


class Stats:
    def __init__(self, input_type, output_type):
        available_types_lower = [item.lower() for item in AvailableFileTypes.get_available_types()]
        if input_type not in available_types_lower:
            raise TypeError(f'{input_type} is not an available type')

        if output_type not in available_types_lower:
            raise TypeError(f'{output_type} is not an available type.')

        self.input_type = input_type
        self.output_type = output_type
        self.input_file_worker = None
        self.output_file_worker = None

        if self.input_type == 'csv':
            self.input_file_worker = CSVWorker()
        elif self.input_type == 'json':
            self.input_file_worker = JSONWorker()

        if self.output_type == 'csv':
            self.output_file_worker = CSVWorker()
        elif self.output_type == 'json':
            self.output_file_worker = JSONWorker()

    def run(self):
        # Step 1. Read from input file
        products = self.input_file_worker.read()

        # Step 2. Do some magic
        #color
        products_by_color = defaultdict(list)
        for product in products:
            products_by_color[product['color']].append(product)
        #gender
        products_by_gender = defaultdict(list)
        for product in products:
            products_by_gender[product['gender']].append(product)
        #promotion
        products_on_promotion = defaultdict(list)
        for product in products:
            if product['normal price']!=product['price']:
                products_on_promotion[product['price']].append(product)
        #most saled
        products_most_saled = defaultdict(list)
        for product in products:
            int_products=int(product['sales'])
            if int_products>1000:
                products_most_saled[product['sales']].append(product)
        #unsaled
        products_unsaled = defaultdict(list)
        for product in products:
            int_products=int(product['sales'])
            if int_products<10:
                products_unsaled[product['sales']].append(product)

        # Step 3. Write to output file
        #color
        for color, products in products_by_color.items():
            self.output_file_worker.write(color, products)
        #gender
        for gender, products in products_by_gender.items():
            self.output_file_worker.write(gender, products)
        #promotion
        for price, products in products_on_promotion.items():
            self.output_file_worker.write_promotion(products)
        #most sales
        for sales, products in products_most_saled.items():
            self.output_file_worker.write_most_sales(products)
        #unsaled
        for sales, products in products_unsaled.items():
            self.output_file_worker.write_unsaled(products)






