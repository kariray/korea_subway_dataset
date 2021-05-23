import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import os
from make_csv import write_csv

os.system('clear')


def scrap_station(row, page_name, check_line, check_note):
    city = ["서울특별시", "경기도"]
    if check_line == True:
        cl = 0
    else:
        cl = -1

    if check_note == True:
        cn = -1
    else:
        cn = 0

    number = row[0]

    if check_line == True:
        line = row[1]
    else:
        line = page_name

    name = row[2+cl]
    english_name = row[3+cl]
    hanja_name = row[4+cl]
    transfer = row[-5+cn]
    distance = row[-4+cn]
    cumulative_distance = row[-3+cn]
    if row[-1+cn] in city:
        location = row[-1+cn] + " " + row[-2+cn]
    else:
        location = row[-2+cn] + " " + row[-1+cn]

    return {
        'number': number.replace(" ", ""),
        'line': line,
        'name': name,
        'english_name': english_name,
        'hanja_name': hanja_name,
        'transfer': transfer.replace("●", "", 1).replace("●", ","),
        'distance': distance,
        'cumulative_distance': cumulative_distance,
        'location': location
    }


def get_data_seoul():
    city_name = "seoul"
    # seoul_subway_lines = [[지하철노선이름, 테이블 내 노선명 유무, 테이블 내 비고란 유무, 시작테이블, 끝테이블 + 1(테이블이 한 개면 None)]]
    seoul_subway_lines = [
        #["수도권_전철_1호선", True, False, 1, 4],
        ["서울_지하철_2호선", False, False, 0, 3],
        ["수도권_전철_3호선", True, False, 0, None],
        ["수도권_전철_4호선", True, False, 0, None],
        ["수도권_전철_5호선", False, False, 0, 2],
        ["서울_지하철_6호선", False, False, 0, None],
        ["서울_지하철_7호선", False, False, 0, None],
        ["서울_지하철_8호선", False, False, 0, None],
        ["서울_지하철_9호선", False, False, 0, None],
        ["경강선", False, True, 0, None],
        ["수도권_전철_경의·중앙선", True, False, 0, 3],
        ["경춘선", False, False, 0, None],
        ["인천국제공항철도", False, True, 0, None],
        ["서해선", False, True, 0, None],
        #["수도권_전철_수인·분당선", True, False, 0, None],
        ["신분당선", False, False, 0, None],
        ["김포_도시철도", False, True, 0, None],
        ["용인_경전철", False, False, 0, None],
        ["서울_경전철_우이신설선", False, False, 0, None],
        ["의정부_경전철", False, False, 0, None],
        ["인천_도시철도_1호선", False, False, 0, None],
        ["인천_도시철도_2호선", False, False, 0, None],
        ["인천공항_자기부상철도", False, False, 0, None]
    ]

    for seoul_subway_line in seoul_subway_lines:
        line_name = seoul_subway_line[0]
        line_data = {"line_name": line_name, "station_data": []}
        url = f"https://ko.wikipedia.org/wiki/{line_name}"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        if seoul_subway_line[4] == None:
            data = soup.find_all("table", {"class": "wikitable"})[
                seoul_subway_line[3]]
            table = parser_functions.make2d(data)
            for i in range(1, len(table)):
                scraped_station = scrap_station(
                    table[i], seoul_subway_line[0], seoul_subway_line[1], seoul_subway_line[2])
                if scraped_station:
                    line_data["station_data"].append(scraped_station)

        else:
            data = soup.find_all("table", {"class": "wikitable"})
            for i in range(seoul_subway_line[3], seoul_subway_line[4]):
                d = data[i]
                table = parser_functions.make2d(d)
                for i in range(1, len(table)):
                    scraped_station = scrap_station(
                        table[i], seoul_subway_line[0], seoul_subway_line[1], seoul_subway_line[2])
                    if scraped_station:
                        line_data["station_data"].append(scraped_station)

        write_csv(line_data, city_name)
