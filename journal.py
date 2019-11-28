import os


class Journal:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f'{self.__class__.__name__} with total {len(self.data)} enties'

    def add_entry(self, entry):
        self.data.append(entry)

    def log(self):
        for index, entry in enumerate(reversed(self.data)):
            print(f'[{index + 1}]: {entry}')

    def save(self):
        with open(os.path.join('journals', 'journal.txt'), 'w') as fout:
            for entry in self.data:
                fout.write(f'{entry}\n')

    def load(self):
        with open(os.path.join('journals', 'journal.txt'), 'r') as fin:
            for line in fin:
                self.data.append(line.strip())
