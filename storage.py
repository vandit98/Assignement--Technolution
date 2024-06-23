import json
import os

class Storage:
    @staticmethod
    def load_data(file_name):
        """
        Load data from a JSON file.
        
        :param file_name: Name of the JSON file.
        :return: Data loaded from the JSON file.
        """
        if not os.path.exists(file_name):
            return []
        
        with open(file_name, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_data(file_name, data):
        """
        Save data to a JSON file.
        
        :param file_name: Name of the JSON file.
        :param data: Data to save to the file.
        """
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

# Example usage:
# books = [{'title': 'Book1', 'author': 'Author1', 'ISBN': '123', 'availability': True}]
# Storage.save_data('books.json', books)
# loaded_books = Storage.load_data('books.json')
# print(loaded_books)
