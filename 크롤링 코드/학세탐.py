# 학문세계의 탐구 GELI005 : 1A~, 2A~, 3A~, 4A~, 5A~, 6A~, 7A~, 8A~, 9A~, CD, CE, CF, CG, CH
# 006 : 01~06
# 007 : 'A1', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'
# 008 : 'D1', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4', 'F5'
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

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


num_alpha_list = []
for front_num in range(1, 10):
    for back_alpha in range(65, 91):
        num_alpha_list.append(str(front_num)+chr(back_alpha))

#005
for cour_cls in num_alpha_list:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '005'  + "&cour_cls=" + cour_cls + "&"
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
    
#006
for cour_cls in range(0, 10):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '006'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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

#007
for cour_cls in ['A1', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '007'  + "&cour_cls=" + cour_cls + "&"
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

#008
for cour_cls in ['D1', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4', 'F5']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '008'  + "&cour_cls=" + cour_cls + "&"
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
df.to_csv('학세탐.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")
