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

major_001 = {'COED' : '4064'}
major_201 = { 'LBNC':'6093'}
major_202 = {'GLEA':'6095',  'MHUM':'6342'}

major_301 = {'AICE' : '6545'}
major_303 = {'ISEC':'5944'}
major_315 = { 'BNCS':'6666'}

for key, value in major_001.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '001' + "&cour_cls=" + '00' + "&"
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

for key, value in major_201.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '201' + "&cour_cls=" + '00' + "&"
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

for key, value in major_202.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '202' + "&cour_cls=" + '00' + "&"
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

for key, value in major_301.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '301' + "&cour_cls=" + '00' + "&"
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

for key, value in major_303.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '303' + "&cour_cls=" + '00' + "&"
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

for key, value in major_315.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '315' + "&cour_cls=" + '00' + "&"
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



for key, value in major_315.items():
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + '315' + "&cour_cls=" + '00' + "&"
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

# 00
major_105_107 = { 'POLI':'0199'}
major_212_214_218 = { 'EMLA':'5672'}
major_211_310 = {'FNEG':'5046'}
major_201_301 = {'MUKE':'5753'}
major_202_303 = {'UNIP':'6463'}
major_300_301_302 = { 'HMCI':'6094'}
major_315_414 = {  'LESF':'4425'}
major_301_401_402 = {'DTPR':'7283'}
major_304_402 = {'FADM':'4638'}

#01
major_01_202_204 = {'GEMS':'3653'}
for key, value in major_01_202_204.items():
    for num in [202, 204]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '01' + "&"
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


for key, value in major_105_107.items():
    for num in [105, 107]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_212_214_218.items():
    for num in [212, 214, 218]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_211_310.items():
    for num in [211, 310]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_201_301.items():
    for num in [201, 301]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_202_303.items():
    for num in [202, 303]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_300_301_302.items():
    for num in [300, 301, 302]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_315_414.items():
    for num in [315, 414]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_301_401_402.items():
    for num in [301, 401, 402]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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

for key, value in major_304_402.items():
    for num in [304, 402]:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num) + "&cour_cls=" + '00' + "&"
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
df.to_csv('전공10.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")