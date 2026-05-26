import csv

class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = []

        with open(self.file_path, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        return data


    def get_sample(self, n=5):
        data = self.load_data()
        return data[:n]