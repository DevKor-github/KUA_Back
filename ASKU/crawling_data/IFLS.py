import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

 # 전공과목영문코드 입력
cour_num = []
name = []
cour_time = []
cour_prof = []

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
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + '800'  + "&cour_cls=" + cour_cls + "&"
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
    cour_number = "IFLS" + '800' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")    

#801  
for cour_cls in ['R1', 'R2', 'R3', 'R4', 'R5', 'RA', 'RB', 'RC', 'RD', 'RE', 'RF', 'RG', 'RH', 'RI', 'RJ', 'RK', 'Z1', 'Z3', 'Z5', 'Z6']:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + '801'  + "&cour_cls=" + cour_cls + "&"
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
    cour_number = "IFLS" + '801' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")

# 교양 선택 108-112
for num in range(108, 113):
    for cour_cls in ['01', '02', '03', '04', '05', '06', 'A1', 'B1', 'C1', 'D1', 'D2', 'E1', 'E2', 'E3', 'E4', 'E5']:
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + str(num)  + "&cour_cls=" + cour_cls + "&"
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

        #   print(title)
        try:
            time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
            time = " ".join(time)
            prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
        except:
            time = None
            prof = None
        cour_time.append(time)
        cour_prof.append(prof)
        cour_number = "IFLS" + str(num) + "-" + cour_cls
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료")
    
# 교양 선택 240-814    
for num in [240, 241, 242, 243, 245, 246, 400, 401, 802, 804, 805, 806, 807, 808, 809, 810, 811, 813, 814]:
    for cour_cls in range(0, 10):
        url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "IFLS"  + str(num)  + "&cour_cls=" + str(cour_cls).zfill(2) + "&"
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
        cour_number = "IFLS" + str(num) + "-" + str(cour_cls).zfill(2)
        cour_num.append(cour_number)
        name.append(title)
        #print(url)
        print(f"{cour_number} 완료")

        
cour_table = pd.DataFrame({"학수번호" : cour_num, "강의명" : name, "시간" : cour_time, "교수명" : cour_prof})
cour_table.to_csv('scrape_course_IFLS.csv', index=False)
print(cour_table)      