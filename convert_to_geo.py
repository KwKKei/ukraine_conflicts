import json

# Path to the original JSON file
json_file_path = "C:/Users/wys6299/Desktop/UCSD/dsc106-wi24/projects/Final Project/ukraine_conflicts/static/battles.json"

# Read the original JSON data from the file
with open(json_file_path, "r") as f:
    original_json = json.load(f)

# Convert each entry to the desired format
features = []
for entry in original_json:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [entry["LONGITUDE"], entry["LATITUDE"]]
        },
        "properties": {
            "city": entry["LOCATION"],
            "date": entry["EVENT_DATE"],
            "disorder": entry["DISORDER_TYPE"],
            "event": entry["EVENT_TYPE"]
        }
    }
    features.append(feature)

# Create the FeatureCollection
feature_collection = {
    "type": "FeatureCollection",
    "features": features
}

# Convert to JSON string
new_json = json.dumps(feature_collection, indent=2)


# If you want to save it to a file, you can use:
with open("new_cities.json", "w") as f:
    f.write(new_json)