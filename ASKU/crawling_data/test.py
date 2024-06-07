import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd
import os


# cour_cd : 학수번호, dept_cd : 학위코드,cour_cls : 분반

cour_num = []
name = []
cour_time = []
cour_prof = []
cour_major = []

major00_100_400 = {'EDUC':'0236','SEDU':'5960', 'NRSG' : '0233', 'BUSS' : '0142', 'IMEN':'5320','ACEE':'5204', 'SEMI':'6723', 'ENGY':'6724', 'DISS':'6910', 'GKSS':'6911', 'ARDE':'5339', 'BSMS':'5694', 'HEED':'0238', 'EDUC':'0236', 'HISE':'0243',  'GEOG':'0242', 'ELED':'0241', 'LESE':'4657', 'CYDF':'6880', 'MEDI':'0229',  'ECON':'0200', 'STAT':'0201', 'PHIL':'0147'}
for key, value in major00_100_400.items():
    for num in range (100, 500):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_100_500 = {'ARCH':'4887'}
for key, value in major00_100_500.items():
    for num in range (100, 600):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")

major00_200_300 = {'GLKS':'7037', 'EMLA':'5672', 'GLEA':'6095', 'FNEG':'5046', 'PAPP':'0203'}
for key, value in major00_200_300.items():
    for num in range (200, 400):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_300_400 = {'DTPR':'7283', 'DATA':'6725'}
for key, value in major00_300_400.items():
    for num in range (300, 500):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_100 = {'LALW':'5539', 'JAPN':'0157', 'CPSE':'4062', 'KMCE':'5962' }
for key, value in major00_100.items():
    for num in range (100, 200):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_200 = {'LBNC':'6093', 'MHUM':'6342', 'UNIP':'6463', 'MUKE':'5753', 'GEMS':'3653', }
for key, value in major00_200.items():
    for num in range (200, 300):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
marjo00_300 = {'TEEN':'6544', 'HMCI':'6094', 'FADM':'4638', 'BNCS':'6666', 'ISEC':'5944','SCED' : '4063'}
for key, value in marjo00_300.items():
    for num in range (300, 400):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_400 = {'ECOC':'7282', 'LESF':'4425', 'STEP':'5965'}
for key, value in major00_400.items():
    for num in range (400, 500):
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")
major00_700 = {'PSYC':'6565'}
for key, value in major00_700.items():
    for num in [701, 703, 704, 708]:
        for cour_cls in range(0, 10):
            url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ value +"&cour_cd=" + key + str(num).zfill(3) + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
            html = req.urlopen(url)
            doc = BeautifulSoup(html,"html.parser")
            h3_tag = doc.find('h3')
                
            if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
                print(key+str(num)+'-'+str(cour_cls)+'no site')
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
                major = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.string

            except:
                time = None
                prof = None
            cour_time.append(time)
            cour_prof.append(prof)
            cour_major.append(major)
            cour_number = key + str(num).zfill(3) + "-" + str(cour_cls).zfill(2)
            cour_num.append(cour_number)
            name.append(title)
            #print(url)
            print(f"{cour_number} 완료")            
cour_table = pd.DataFrame({"학수번호" : cour_num, "강의명" : name, "시간" : cour_time, "교수명" : cour_prof, "전공명" : cour_major})
csv_file = 'scrape_course_major.csv'
if os.path.exists(csv_file):
    # 존재하면 이어서 저장
    cour_table.to_csv(csv_file, mode='a', header=False, index=False)
else:
    # 존재하지 않으면 새로 저장
    cour_table.to_csv(csv_file, index=False)

print(cour_table)