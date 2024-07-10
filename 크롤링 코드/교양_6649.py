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

gyoyang_6649 = [ 'GEBT', 'GECT', 'SPGE',  'GEQR',    'GEHI',  'SPFL']

# GEST
for num in range (0, 200):
    for cour_cls in range(0, 10):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + 'GEST'  + str(num).zfill(3)  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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

# 00만
for cour_cd in ['GELA', 'GESO', 'GEFC', 'GECE']:
    for num in range (0, 200):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + cour_cd  + str(num).zfill(3)  + "&cour_cls=" + '00' + "&"
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
            
# GEBT
for cour_cls in range(0, 10):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GEBT"  + '001'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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

# GECT
for cour_cls in range(0, 20):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GECT"  + '002'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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

# SPFL
for num in ['107', '117', '131']:
    for cour_cls in ['00', '01', '02', '03', '04', 'Fl', 'G1']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "SPFL"  + num  + "&cour_cls=" + cour_cls + "&"
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

# SPGE
for num in range(100, 300):
    for cour_cls in ['00', '01', '02']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "SPGE"  + str(num)  + "&cour_cls=" + cour_cls + "&"
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
        
# GEQR, GEHI
for cour_cd in ['GEQR', 'GEHI']:
    for num in range (0, 100):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + cour_cd  + str(num).zfill(3)  + "&cour_cls=" + '00' + "&"
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

df = pd.DataFrame({
    '학수번호-분반': cour_num,
    '과목명': cour_name,
    '교수명': cour_prof,
    '학점': cour_credit,
    '이수구분': cour_division,
    '강의시간표 및 장소': cour_time__location
})

# 데이터프레임을 CSV 파일로 저장
df.to_csv('교양6649.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")