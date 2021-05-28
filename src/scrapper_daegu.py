import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import os
from make_csv import write_csv

os.system('clear')


def scrap_station(row, page_name):
    line = page_name.replace("_", " ")
    number = row[0]
    name = row[1]
    english_name = row[2]
    hanja_name = row[3]
    transfer = row[-5]
    distance = row[-4]
    cumulative_distance = row[-3]
    location = row[-2] + " " + row[-1]

    return {
        'number': number.replace("_", " "),
        'line': line,
        'name': name,
        'english_name': english_name,
        'hanja_name': hanja_name,
        'transfer': transfer.replace("●", "", 1).replace("●", ","),
        'distance': distance,
        'cumulative_distance': cumulative_distance,
        'location': location
    }


def get_data_daegu():
    city_name = "daegu"
    seoul_subway_lines = [
        "대구_도시철도_1호선",
        "대구_도시철도_2호선",
        "대구_도시철도_3호선"
    ]

    for seoul_subway_line in seoul_subway_lines:
        line_name = seoul_subway_line
        line_data = {"line_name": line_name, "station_data": []}
        url = f"https://ko.wikipedia.org/wiki/{line_name}"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        data = soup.find("table", {"class": "wikitable"})
        table = parser_functions.make2d(data)
        for i in range(1, len(table)):
            scraped_station = scrap_station(
                table[i], line_name)
            if scraped_station:
                line_data["station_data"].append(scraped_station)

        write_csv(line_data, city_name)
