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

# IFLS : 아카데믹 800은 다, 801은 R, Z만 
# 교양 선택은 혼합
# 108 : 01-06, A1
# 109 : 01-02, B1
# 110 : 01, C1
# 111 : 01, D1, D2
# 112 : 01, E1-E5
# 240 : 01-07
# 241 : 01-04
# 242 : 01-05
# 243 : 01-03
# 245 : 01-03
# 246 : 01, 02
# 400 : 01
# 401 : 01
# 802 : 01-03
# 804 : 01
# 805 : 01
# 806 : 01
# 807 : 01-04
# 808 : 01-03
# 809 : 01, 02
# 810 : 01, 02
# 811 : 01, 02
# 813 : 01
# 814 : 01


major_cour_cls_mix = {'IFLS':'6649', 'GEWR':'6649' , 'GELI':'6649'} 
mix_list = []
for alpha_front in range(65, 91):
    for num_back in range(1, 10):
        mix_list.append(chr(alpha_front)+str(num_back))
    for alpha_back in range(65, 91):
        mix_list.append(chr(alpha_front)+chr(alpha_back))
for number in range(0, 100):
  mix_list.append(str(number))
  
# 800
for cour_cls in mix_list:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + '800'  + "&cour_cls=" + cour_cls + "&"
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

#801  
for cour_cls in ['R1', 'R2', 'R3', 'R4', 'R5', 'RA', 'RB', 'RC', 'RD', 'RE', 'RF', 'RG', 'RH', 'RI', 'RJ', 'RK', 'Z1', 'Z3', 'Z5', 'Z6']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + '801'  + "&cour_cls=" + cour_cls + "&"
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
# 교양 선택 108-112
for num in range(108, 113):
    for cour_cls in ['01', '02', '03', '04', '05', '06', 'A1', 'B1', 'C1', 'D1', 'D2', 'E1', 'E2', 'E3', 'E4', 'E5']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + str(num)  + "&cour_cls=" + cour_cls + "&"
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
    
# 교양 선택 240-814    
for num in [240, 241, 242, 243, 245, 246, 400, 401, 802, 804, 805, 806, 807, 808, 809, 810, 811, 813, 814]:
    for cour_cls in range(0, 10):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanViewNew.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + str(num)  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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
df.to_csv('전공4-3.csv', index=False, encoding='utf-8-sig')
print("CSV 파일로 저장 완료")
