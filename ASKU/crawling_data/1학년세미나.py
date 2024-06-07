import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd


 # 전공과목영문코드 입력
cour_num = []
name = []
cour_time = []
cour_prof = []

# 24-1 1학년세미나
major_cour_cls_alpha = {'GEKS':'6649'} #1학년세미나
alpha_list = []
for alpha_front in range(65, 91):
    for num_back in range(1, 10):
        alpha_list.append(chr(alpha_front)+str(num_back))
    for alpha_back in range(65, 91):
        alpha_list.append(chr(alpha_front)+chr(alpha_back))

#print(alpha_list)

#for number in range (250, 900):
    #for cour_cls in range(0, 10):

for cour_cls in alpha_list:
    url = "https://infodepot.korea.ac.kr/lecture1/lecsubjectPlanView.jsp?year=2024&term=1R&grad_cd=0136&col_cd=9999&dept_cd="+ "6649" +"&cour_cd=" + "GEKS"  + '007'  + "&cour_cls=" + cour_cls + "&"
    html = req.urlopen(url)
    doc = BeautifulSoup(html,"html.parser")
    h3_tag = doc.find('h3')
        
    if (not h3_tag) or not h3_tag.string or len(h3_tag.string) == 19:
        print('no site')
        continue
        
    temp_title = doc.h3.string
    #print(temp_title)
    #title = temp_title.split("[")[1].split("]")[0]
    # 첫 번째 '['의 위치를 찾고, 그 이후의 첫 번째 '[' 위치를 찾음
    start = temp_title.find('[', temp_title.find('[') + 1)
    # 마지막 ']'의 위치를 찾음
    end = temp_title.rfind(']')

    # start와 end 사이의 문자열 추출
    title = temp_title[start:end].strip()
    

    print(title)
    try:
        time = doc.find(class_="tbl_view").tbody.tr.td.string.splitlines()
        time = " ".join(time)
        prof = doc.find(class_="tbl_view").next_sibling.next_sibling.next_sibling.next_sibling.tbody.tr.td.string
    except:
        time = None
        prof = None
    cour_time.append(time)
    cour_prof.append(prof)
    cour_number = "GEKS" + '007' + "-" + cour_cls
    cour_num.append(cour_number)
    name.append(title)
    #print(url)
    print(f"{cour_number} 완료")    
        
cour_table = pd.DataFrame({"학수번호" : cour_num, "강의명" : name, "시간" : cour_time, "교수명" : cour_prof})
cour_table.to_csv('scrape_course_GEKS.csv', index=False)
print(cour_table)      