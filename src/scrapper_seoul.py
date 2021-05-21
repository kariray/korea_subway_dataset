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
    # except_name1 : 소재지에서 구만 하나로 분리 되어 있는 것
    # except_name2 : 소재지에서 구와 시 모두 하나로 분리 되어 있는 것
    except_name1 = {
        "서울_지하철_2호선": "신대방",
        "서울_지하철_2호선": "시청",
        "서울_지하철_2호선": "까치산",
        "수도권_전철_경의·중앙선": "구리",
        "경춘선": "갈매",
        "수도권_전철_수인·분당선": "청량리",
        "수도권_전철_수인·분당선": "복정",
        "신분당선": "강남",
        "서울_경전철_우이신설선": "신설동",
        "인천_도시철도_1호선": "인천터미널",
        "인천_도시철도_2호선": "주안국가산단(인천J밸리)"
    }
    except_name2 = {
        "서울_지하철_7호선": "장암",
        "서울_지하철_7호선": "도봉산",
        "김포 도시철도": "김포공항"}

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

    if (items[-2+i].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2")) or (name.replace("\n", "") in except_name2.values() and page_name in except_name2.keys()):
        temp_location1 = items[-2].get_text().replace("\n", " ")
        if items[-1+i].has_attr("rowspan") or name.replace("\n", "") in except_name2:
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
        if items[-1+i].has_attr("rowspan") and row.find("th", rowspan=lambda x: x != "2") or (name.replace("\n", "") in except_name1.values() and page_name in except_name1.keys()):
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

    return {
        'number': number.replace("\n", ""),
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

        write_csv(line_data, city_name)
