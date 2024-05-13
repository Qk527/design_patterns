from adapters import CsvToJsonAdapter
from data_handlers import JsonDataHandler, CsvDataHandler

def load_and_display_data(data_handler, file_path):
  data = data_handler.load_data(file_path)
  print(data)

if __name__ == '__main__':
  #Json handler
  json_handler = JsonDataHandler()
  json_file_path = 'data/sample_data.json'

  #csv handler with adapter
  csv_handler = CsvDataHandler()
