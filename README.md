# Korea Subway Dataset (한국 지하철 데이터셋)

## **Korean**

> #### 1. 설명
>
> > - Korea Subway Dataset(한국 지하철 데이터셋)은 인터넷에서 한국 지하철 데이터를 크롤링 하여 .csv 파일로 만드는 프로젝트입니다.
> > - 데이터셋을 다운받길 원하시면 dataset 폴더로 가시면 됩니다.

<br />

> #### 2. 데이터 분류
>
> > #### 서울 지하철 데이터셋
> >
> > |   데이터 명 |             변수 명 | 데이터 타입 |
> > | ----------: | ------------------: | :---------: |
> > |      역번호 |              number |    char     |
> > |      노선명 |                line |    char     |
> > |        역명 |                name |    char     |
> > | 로마자 역명 |        english_name |    char     |
> > |   한자 역명 |          hanja_name |    char     |
> > |   접속 노선 |            transfer |    char     |
> > |   역간 거리 |            distance |    char     |
> > |   누적 거리 | cumulative_distance |    char     |
> > |      소재지 |            location |    char     |
>
> > #### 부산 지하철 데이터셋
> >
> > |   데이터 명 |             변수 명 | 데이터 타입 |
> > | ----------: | ------------------: | :---------: |
> > |      역번호 |              number |    char     |
> > |      노선명 |                line |    char     |
> > |        역명 |                name |    char     |
> > | 로마자 역명 |        english_name |    char     |
> > | 일본어 역명 |       japanese_name |    char     |
> > | 중국어 역명 |        chinese_name |    char     |
> > |   한자 역명 |          hanja_name |    char     |
> > |   접속 노선 |            transfer |    char     |
> > |   역간 거리 |            distance |    char     |
> > |   누적 거리 | cumulative_distance |    char     |
> > |      소재지 |            location |    char     |

<br />

> #### 3. 현재 업데이트 된 노선 리스트
>
> > #### 서울 지하철
> >
> > - [ ] 수도권 전철 1호선
> > - [x] 서울 지하철 2호선
> > - [x] 수도권 전철 3호선
> > - [x] 수도권 전철 4호선
> > - [x] 수도권 전철 5호선
> > - [x] 서울 지하철 6호선
> > - [x] 서울 지하철 7호선
> > - [x] 서울 지하철 8호선
> > - [x] 서울 지하철 9호선
> > - [x] 경강선
> > - [x] 수도권 전철 경의·중앙선
> > - [x] 경춘선
> > - [x] 인천국제공항철도
> > - [x] 서해선
> > - [ ] 수도권 전철 수인·분당선
> > - [x] 신분당선
> > - [x] 김포 도시철도
> > - [x] 용인 경전철
> > - [x] 서울 경전철 우이신설선
> > - [x] 의정부 경전철
> > - [x] 인천 도시철도 1호선
> > - [x] 인천 도시철도 2호선
> > - [x] 인천공항 자기부상철도
>
> > #### 부산 지하철
> >
> > - [x] 부산 도시철도 1호선
> > - [x] 부산 도시철도 1호선
> > - [x] 부산 도시철도 1호선
> > - [x] 부산 도시철도 1호선
> > - [x] 부산-김해 경전철
> > - [ ] 동해선

<br />

> #### 4. 데이터를 가져 온 사이트
>
> > #### 서울 지하철
> >
> > [위키백과](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8)
>
> > #### 부산 지하철
> >
> > [위키백과](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8)

<br />

> #### 5. 알림
>
> > #### 서울 지하철
> >
> > - 파이썬 크롤링 코드가 `scrapper_seoul_VER_1.py` 와 `scrapper_seoul_VER_2.py` 두 개가 존재하는데 `VER_2` 코드만 사용하세요.
> > - `VER_1` 코드는 200줄이 넘어가는 매우 더러운 코드이기 때문에 `html_table_parser`을 이용한 `VER_2`코드가 훨씬 낫습니다.
>
> > #### 부산 지하철
> >
> > - 없음

---

## **English**

> #### 1. Description
>
> - This Project is make Korea Subway Dataset throught web-pages Crawling.
> - If you want download CSV files, go to Dataset folders.

<br />

> #### 2. Data category
>
> > #### Seoul Subway Dataset
> >
> > |                      Data name |            Variable | Data type |
> > | -----------------------------: | ------------------: | :-------: |
> > |                 Station Number |              number |   char    |
> > |                           Line |                line |   char    |
> > |                   Station Name |                name |   char    |
> > |           English Station Name |        english_name |   char    |
> > | Chinese character Station Name |          hanja_name |   char    |
> > |                  Transfer Line |            transfer |   char    |
> > |      Distance between stations |            distance |   char    |
> > |            Cumulative distance | cumulative_distance |   char    |
> > |                       Location |            location |   char    |
>
> > #### Busan Subway Dataset
> >
> > |                      Data name |            Variable | Data type |
> > | -----------------------------: | ------------------: | :-------: |
> > |                 Station Number |              number |   char    |
> > |                           Line |                line |   char    |
> > |                   Station Name |                name |   char    |
> > |           English Station Name |        english_name |   char    |
> > |          Japanese Station Name |       japanese_name |   char    |
> > |           Chinese Station Name |        chinese_name |   char    |
> > | Chinese character Station Name |          hanja_name |   char    |
> > |                  Transfer Line |            transfer |   char    |
> > |      Distance between stations |            distance |   char    |
> > |            Cumulative distance | cumulative_distance |   char    |
> > |                       Location |            location |   char    |

<br />

> #### 3. Updated Lines List
>
> > #### Seoul Subway
> >
> > - [ ] Line 1
> > - [x] Line 2
> > - [x] Line 3
> > - [x] Line 4
> > - [x] Line 5
> > - [x] Line 6
> > - [x] Line 7
> > - [x] Line 8
> > - [x] Line 9
> > - [x] Gyeonggang Line
> > - [x] Gyeongui Jungang Line
> > - [x] Gyuongchun Line
> > - [x] Airport Railroad Line
> > - [x] Seohae Line
> > - [ ] Suin Bundang Line
> > - [x] Shinbundang Line
> > - [x] Gimpo GoldLine
> > - [x] Ever Line
> > - [x] Ui Lrt Line
> > - [x] Uijeongbu Lrt Line
> > - [x] Incheon Line1
> > - [x] Incheon Line2
> > - [x] Incheon Airport Maglev Line
>
> > #### Busan Subway
> >
> > - [x] Line1
> > - [x] Line2
> > - [x] Line3
> > - [x] Line14
> > - [x] Busan Gimhae Light Rail Transit
> > - [ ] DongHae Line

<br />

> #### 4. Data Crawling Site
>
> > #### Seoul Subway
> >
> > [Korea wikipedia](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8)
>
> > #### Busan Subway
> >
> > [Korea wikipedia](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:%EB%8C%80%EB%AC%B8)

<br />

> #### 5. Notice
>
> > #### Seoul Subway
> >
> > - In the src folder, python crawling code exists that `scrapper_seoul_VER_1.py` and `scrapper_seoul_VER_2.py`. But, I recommend only used `VER_2`.
> > - Because, `VER_1` is very BAD code with more than 200 lines. So, `VER_2` that used `html_table_parser` better than `VER_1`
>
> > #### Busan Subway
> >
> > - None
