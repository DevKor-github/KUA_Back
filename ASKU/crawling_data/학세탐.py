# 학문세계의 탐구 GELI005 : 1A~, 2A~, 3A~, 4A~, 5A~, 6A~, 7A~, 8A~, 9A~, CD, CE, CF, CG, CH
# 006 : 01~06
# 007 : 'A1', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'
# 008 : 'D1', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4', 'F5'
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

# 전공과목영문코드 입력
cour_num = []
name = []
cour_time = []
cour_prof = []


num_alpha_list = []
for front_num in range(1, 10):
    for back_alpha in range(65, 91):
        num_alpha_list.append(str(front_num)+chr(back_alpha))

#005
for cour_cls in num_alpha_list:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '005'  + "&cour_cls=" + cour_cls + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['와 ']'의 위치를 찾기
    start = temp_title.find('[') + 1
    end = temp_title.find(']')

    # 해당 위치 사이의 문자열을 추출하고 양옆의 공백을 제거
    title = temp_title[start:end].strip()

    #print(title)
    try:
        time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
        time = " ".join(time)
        prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
    except:
        time = None
        prof = None
    cour_time.append(time)
    cour_prof.append(prof)
    cour_number = "GELI" + '005' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")    
    
#006
for cour_cls in range(0, 10):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '006'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['와 ']'의 위치를 찾기
    start = temp_title.find('[') + 1
    end = temp_title.find(']')

    # 해당 위치 사이의 문자열을 추출하고 양옆의 공백을 제거
    title = temp_title[start:end].strip()

    #print(title)
    try:
        time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
        time = " ".join(time)
        prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
    except:
        time = None
        prof = None
    cour_time.append(time)
    cour_prof.append(prof)
    cour_number = "GELI" + '006' + "-" + str(cour_cls).zfill(2)
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")    

#007
for cour_cls in ['A1', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '007'  + "&cour_cls=" + cour_cls + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['와 ']'의 위치를 찾기
    start = temp_title.find('[') + 1
    end = temp_title.find(']')

    # 해당 위치 사이의 문자열을 추출하고 양옆의 공백을 제거
    title = temp_title[start:end].strip()

    #print(title)
    try:
        time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
        time = " ".join(time)
        prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
    except:
        time = None
        prof = None
    cour_time.append(time)
    cour_prof.append(prof)
    cour_number = "GELI" + '007' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")    

#008
for cour_cls in ['D1', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4', 'F5']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GELI"  + '008'  + "&cour_cls=" + cour_cls + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['와 ']'의 위치를 찾기
    start = temp_title.find('[') + 1
    end = temp_title.find(']')

    # 해당 위치 사이의 문자열을 추출하고 양옆의 공백을 제거
    title = temp_title[start:end].strip()

    #print(title)
    try:
        time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
        time = " ".join(time)
        prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
    except:
        time = None
        prof = None
    cour_time.append(time)
    cour_prof.append(prof)
    cour_number = "GELI" + '008' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")   

cour_table = pd.DataFrame({"학수번호" : cour_num, "강의명" : name, "시간" : cour_time, "교수명" : cour_prof})
cour_table.to_csv('scrape_course_GELI.csv', index=False)
print(cour_table)      