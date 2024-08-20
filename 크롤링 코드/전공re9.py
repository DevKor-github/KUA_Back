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

major16_800_900 = {'PHEK':'0237'}
major00_100_200 = {'CPSE':'4062', 'KMCE':'5962', 'LALW':'5539'}
major00_300_400 = { 'TEEN':'6544'}
major00_400_500 = { 'DATA':'6725',  'STEP':'5965', 'ITCS' : '5964'}
major00_700_800 = {'PSYC':'6565'}

for key, value in major16_800_900.items():
    for num in range (800, 900):
        for cour_cls in range(1, 7):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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

for key, value in major00_100_200.items():
    for num in range (100, 200):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + "00" + "&"
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
for key, value in major00_300_400.items():
    for num in range (300, 400):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + "00" + "&"
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
for key, value in major00_400_500.items():
    for num in range (400, 500):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + "00" + "&"
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
for key, value in major00_700_800.items():
    for num in range (700, 800):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=2R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + "00" + "&"
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
df.to_csv('전공9.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")