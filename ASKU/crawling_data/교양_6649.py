import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd


cour_num = []
name = []
cour_time = []
cour_prof = []

gyoyang_6649 = [ 'GEBT', 'GECT', 'SPGE',  'GEQR',    'GEHI',  'SPFL']

# GEST
for num in range (0, 200):
    for cour_cls in range(0, 10):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + 'GEST'  + str(num).zfill(3)  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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
        cour_number = 'GEST' + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료")

# 00만
for cour_cd in ['GELA', 'GESO', 'GEFC', 'GECE']:
    for num in range (0, 200):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + cour_cd  + str(num).zfill(3)  + "&cour_cls=" + '00' + "&"
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
        cour_number = cour_cd + str(num).zfill(3) + "-" + '00'
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료")
            
# GEBT
for cour_cls in range(0, 10):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GEBT"  + '001'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['의 위치를 찾고, 그 이후의 첫 번째 '[' 위치를 찾음
    start = temp_title.find('[', temp_title.find('[') + 1)
    # 마지막 ']'의 위치를 찾음
    end = temp_title.rfind(']')

    # start와 end 사이의 문자열 추출
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
    cour_number = "GEBT" + '001' + "-" + str(cour_cls).zfill(2)
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")   

# GECT
for cour_cls in range(0, 20):
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GECT"  + '002'  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
            
    temp_title = doc.h3.string
    #print(temp_title)
    # 첫 번째 '['의 위치를 찾고, 그 이후의 첫 번째 '[' 위치를 찾음
    start = temp_title.find('[', temp_title.find('[') + 1)
    # 마지막 ']'의 위치를 찾음
    end = temp_title.rfind(']')

    # start와 end 사이의 문자열 추출
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
    cour_number = "GECT" + '002' + "-" + str(cour_cls).zfill(2)
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료") 

# SPFL
for num in ['107', '117', '131']:
    for cour_cls in ['00', '01', '02', '03', '04', 'Fl', 'G1']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "SPFL"  + num  + "&cour_cls=" + cour_cls + "&"
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
        cour_number = "SPFL" + num + "-" + cour_cls
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료") 

# SPGE
for num in range(100, 300):
    for cour_cls in ['00', '01', '02']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "SPGE"  + str(num)  + "&cour_cls=" + cour_cls + "&"
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
        cour_number = "SPGE" + str(num) + "-" + cour_cls
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료") 
        
# GEQR, GEHI
for cour_cd in ['GEQR', 'GEHI']:
    for num in range (0, 100):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + cour_cd  + str(num).zfill(3)  + "&cour_cls=" + '00' + "&"
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
        cour_number = cour_cd + str(num).zfill(3) + "-" + '00'
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료")


cour_table = pd.DataFrame({"학수번호" : cour_num, "강의명" : name, "시간" : cour_time, "교수명" : cour_prof})
cour_table.to_csv('scrape_course_교양_6649.csv', index=False)
print(cour_table)