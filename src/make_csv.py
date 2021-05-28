import csv


def write_csv(line_data, city_name):
    file = open(f"dataset/{city_name}/{line_data['line_name']}.csv", mode="w")
    writer = csv.writer(file)
    if city_name == "pusan":
        writer.writerow(["number", "line", "name", "english_name", "japanese_name",
                         "chinese_name", "hanja_name", "transfer", "distance", "cumulative_distance", "location"])
    else:
        writer.writerow(["number", "line", "name", "english_name", "hanja_name",
                         "transfer", "distance", "cumalative_distance", "location"])
    for d in line_data['station_data']:
        writer.writerow(d.values())
    print(f"Created {line_data['line_name']}.csv file")
    return
