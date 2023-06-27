from collections import UserDict
from datetime import datetime
import pickle


class AddressBook(UserDict):

    
    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n=5):
        records = list(self.data.values())
        total_records = len(records)
        current_index = 0

        while current_index < total_records:
            end_index = min(current_index + n, total_records)
            yield records[current_index:end_index]
            current_index += n

    def save_file(self, filename):
        with open(filename + '.bin', 'wb') as file:
            pickle.dump(self.data, file)


    def load_file(self, filename):
        with open(filename + '.bin', 'rb') as file:
            self.data = pickle.load(file)
        return self.data
        
    def search_contact(self, pattern, field):
        result = []
        find_pattern = pattern.strip().lower().replace(' ', '')
        search_field = field.strip().lower().replace(' ', '')
        for contact in self.data:
            if search_field == 'phone':
                for phone in contact[phone]:
                    if phone.startswith(find_pattern):
                        result.append(contact)
            elif search_field == 'name':
                for name in contact[name]:
                    if find_pattern in name:
                        result.append(contact)
        if not result:
            print('I didn`t find anything')
        return result