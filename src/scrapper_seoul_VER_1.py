# This Code not use html_table_parser.
# It's just Fucking CODE!!!!
import requests
from bs4 import BeautifulSoup
import os
from make_csv import write_csv

os.system('clear')

temp_line = ''
temp_location1 = ''
temp_location2 = ''


def line_have_two_name(items):
    number = items[0].get_text()
    name = items[1].get_text()
    english_name = items[2].get_text()
    hanja_name = items[3].get_text()
    return number, name, english_name, hanja_name


def scrape_station(row, page_name, check_line, check_note):
    global temp_line, temp_location1, temp_location2
    check_page_name = page_name
    # except_name1 : 소재지에서 구만 하나로 분리 되어 있는 것
    # except_name2 : 소재지에서 구와 시 모두 하나로 분리 되어 있는 것 또는 시가 맨 처음인 경우 + 구가 분리
    except_name1 = {
        "231": "서울_지하철_2호선",
        "201": "서울_지하철_2호선",
        "234-4": "서울_지하철_2호선",
        "243": "서울_지하철_2호선",
        "434": "수도권_전철_4호선",
        "531": "수도권_전철_5호선",
        "543": "수도권_전철_5호선",
        "745": "서울_지하철_7호선",
        "746": "서울_지하철_7호선",
        "911": "서울_지하철_9호선",
        "K123": "수도권_전철_경의·중앙선",
        "K222": "수도권_전철_수인·분당선",
        "S122": "서울_경전철_우이신설선",
        "I126": "인천_도시철도_1호선",
        "I217": "인천_도시철도_2호선",
        "A04": "인천국제공항철도"
    }
    except_name2 = {
        "709": "서울_지하철_7호선",
        "710": "서울_지하철_7호선",
        "P123": "경춘선",
        "D07": "신분당선",
        "K209": "수도권_전철_수인·분당선",
        "G109": "김포_도시철도",
        "A06": "인천국제공항철도",
        "A01": "인천국제공항철도"
    }

    items = row.find_all(["td", "th"])

    if len(items) == 1:
        temp_line = items[0].get_text()
        return

    if items[0].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2"):
        line = items[0].get_text()
        temp_line = line
        number = items[1].get_text()
        name = items[2].get_text()
        english_name = items[3].get_text()
        hanja_name = items[4].get_text()
    elif items[0].has_attr("colspan"):
        return
    elif row.find("th", {"rowspan": "2"}):
        line = temp_line
        number, name, english_name, hanja_name = line_have_two_name(items)
    else:
        if check_line == True:
            line = temp_line
        else:
            line = page_name.replace("_", " ")

        number = items[0].get_text()
        name = items[1].get_text()
        english_name = items[2].get_text()
        hanja_name = items[3].get_text()

    if check_note == True:
        i = -1
    else:
        i = 0

    if (items[-2+i].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2")) or (except_name2.get(number.replace("\n", "").replace(" ", "")) == check_page_name):
        temp_location1 = items[-2+i].get_text().replace("\n", " ")
        if items[-1+i].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2") or (except_name2.get(number.replace("\n", "").replace(" ", "")) == check_page_name):
            temp_location2 = items[-1+i].get_text()
            location = temp_location1 + temp_location2
            transfer = items[-5+i].get_text()
            distance = items[-4+i].get_text()
            cumulative_distance = items[-3+i].get_text()
        else:
            location = temp_location1 + temp_location2
            transfer = items[-4+i].get_text()
            distance = items[-3+i].get_text()
            cumulative_distance = items[-2+i].get_text()
    else:
        location = temp_location1
        if (items[-1+i].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2")) or (except_name1.get(number.replace("\n", "").replace(" ", "")) == check_page_name):
            #temp_location1 = items[-2].get_text().replace("\n", " ")
            temp_location2 = items[-1+i].get_text()
            location = temp_location1 + temp_location2
            transfer = items[-4+i].get_text()
            distance = items[-3+i].get_text()
            cumulative_distance = items[-2+i].get_text()
        elif row.find("th", {"rowspan": "2"}) and items[-1+i].has_attr("rowspan"):
            temp_location2 = items[-1+i].get_text()
            location = temp_location1 + temp_location2
            transfer = items[-4+i].get_text()
            distance = items[-3+i].get_text()
            cumulative_distance = items[-2+i].get_text()
        else:
            location = temp_location1 + temp_location2
            transfer = items[-3+i].get_text()
            distance = items[-2+i].get_text()
            cumulative_distance = items[-1+i].get_text()

    if name.replace("\n", "") == "지축":  # 3호선 지축역
        location = temp_location1 + temp_location2
        transfer = items[-3+i].get_text()
        distance = items[-2+i].get_text()
        cumulative_distance = items[-1+i].get_text()

    return {
        'number': number.replace("\n", "").replace(" ", ""),
        'line': line.replace("\n", ""),
        'name': name.replace("\n", ""),
        'english_name': english_name.replace("\n", ""),
        'hanja_name': hanja_name.replace("\n", ""),
        'transfer': transfer.replace("\n", "").replace("●", "", 1).replace("●", ","),
        'distance': distance.replace("\n", ""),
        'cumulative_distance': cumulative_distance.replace("\n", ""),
        'location': location.replace("\n", "")
    }


def get_data_seoul():
    city_name = "seoul"
    # seoul_subway_lines = [[지하철노선이름, 테이블 내 노선명 유무, 테이블 내 비고란 유무, 시작테이블, 끝테이블 + 1(테이블이 한 개면 None)]]
    seoul_subway_lines = [
        ["수도권_전철_1호선", True, False, 1, 4],
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
        ["수도권_전철_수인·분당선", True, False, 0, None],
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
            rows = data.find_all("tr")[1:]
        elif line_name == "수도권_전철_1호선":  # 1호선 2번째 테이블 비고란 제거
            data = soup.find_all("table", {"class": "wikitable"})[
                seoul_subway_line[3]:seoul_subway_line[4]]
            rows = []
            temp = []
            for i in range(len(data)):
                temp = data[i].find_all("tr")[1:]
                if i == 1:
                    temp = data[i].find_all("tr")[1:-1]
                rows = rows + temp
        else:
            data = soup.find_all("table", {"class": "wikitable"})[
                seoul_subway_line[3]:seoul_subway_line[4]]
            rows = []
            temp = []
            for d in data:
                temp = d.find_all("tr")[1:]
                rows = rows + temp

        for row in rows:
            scraped_station = scrape_station(
                row, line_name, seoul_subway_line[1], seoul_subway_line[2])
            if scraped_station:
                line_data["station_data"].append(scraped_station)

        #write_csv(line_data, city_name)
        print(line_data)
