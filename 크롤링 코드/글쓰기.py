# 글쓰기 GEWR002만 0-70, 알파벳


import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

# 전공과목영문코드 입력
#학수번호 - 분반
cour_num = []
#과목명 
cour_name = []
#교수명
cour_prof = []
#학점
cour_credit = []
#이수구분
cour_division = []
#강의시간 및 장소
cour_time__location = []

for cour_cls in range(0, 65):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GEWR"  + '002'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    try:
        rows = doc.find(class_="tbl_view").tbody.find_all('tr')
            #학점
        credit = rows[0].find_all('td')[1].text.strip()
            #이수구분
        division = rows[2].find_all('td')[0].text.strip()
            #학수번호-분반
        number_class = rows[1].find_all('td')[0].text.strip()
            #강의시간표 및 장소
        time_location = rows[3].find_all('td')[1].text.strip()
            #과목명
        title = rows[4].find_all('td')[0].text.strip()
            #교수명
        prof = doc.find(class_="bottom_view").find_all('tr')[0].find_all('td')[0].text.strip()

    except Exception as e:
        print(f"Error parsing {url}: {e}")
        time = None
        prof = None
        course_credit = None
        course_division = None
        course_code_sec = None
        course_schedule_location = None

    cour_prof.append(prof)
        # cour_number = f'GEST{str(num).zfill(3)}-{str(cour_cls).zfill(2)}'
    cour_name.append(title)
    cour_credit.append(credit)
    cour_division.append(division)
    cour_num.append(number_class)
    cour_time__location.append(time_location)

    print(f"{number_class} 완료")

for cour_cls in ['A1', 'A2', 'A3', 'A4', 'B1', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GEWR"  + '002'  + "&cour_cls=" + cour_cls + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    try:
        rows = doc.find(class_="tbl_view").tbody.find_all('tr')
            #학점
        credit = rows[0].find_all('td')[1].text.strip()
            #이수구분
        division = rows[2].find_all('td')[0].text.strip()
            #학수번호-분반
        number_class = rows[1].find_all('td')[0].text.strip()
            #강의시간표 및 장소
        time_location = rows[3].find_all('td')[1].text.strip()
            #과목명
        title = rows[4].find_all('td')[0].text.strip()
            #교수명
        prof = doc.find(class_="bottom_view").find_all('tr')[0].find_all('td')[0].text.strip()

    except Exception as e:
        print(f"Error parsing {url}: {e}")
        time = None
        prof = None
        course_credit = None
        course_division = None
        course_code_sec = None
        course_schedule_location = None

    cour_prof.append(prof)
        # cour_number = f'GEST{str(num).zfill(3)}-{str(cour_cls).zfill(2)}'
    cour_name.append(title)
    cour_credit.append(credit)
    cour_division.append(division)
    cour_num.append(number_class)
    cour_time__location.append(time_location)

    print(f"{number_class} 완료")
        
# 데이터프레임으로 변환 및 저장
df = pd.DataFrame({
    '학수번호-분반': cour_num,
    '과목명': cour_name,
    '교수명': cour_prof,
    '학점': cour_credit,
    '이수구분': cour_division,
    '강의시간표 및 장소': cour_time__location
})

# 데이터프레임을 CSV 파일로 저장
df.to_csv('글쓰기.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")
