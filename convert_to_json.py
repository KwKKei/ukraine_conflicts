import openpyxl
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def convert_to_json(file_path, file_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    headers = data[0]
    json_data = []
    for row in data[1:]:
        json_data.append(dict(zip(headers, row)))

    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4, cls=DateTimeEncoder)

if __name__ == "__main__":
    convert_to_json('C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final project/ukraine_conflicts/static/protests.xlsx', 'protests.json')        
    convert_to_json('C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final project/ukraine_conflicts/static/battles.xlsx', 'battles.json')        
    convert_to_json('C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final project/ukraine_conflicts/static/explosion.xlsx', 'explosion.json')        
    convert_to_json('C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final project/ukraine_conflicts/static/develop.xlsx', 'develop.json')        
    convert_to_json('C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final project/ukraine_conflicts/static/violance.xlsx', 'violance.json')