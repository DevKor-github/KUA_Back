import pandas as pd
import re

# CSV 파일 경로
csv_file = 'C:\\Users\\soobin.park\\Desktop\\devkor_backend\\csv원본\\전공4-5.csv'

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv(csv_file)

# 정규표현식 패턴
pattern = re.compile(r'([월화수목금토일])\s*\((\d+(?:-\d+)?)\)\s*([^\s]+(?:\s+\d+호?)?)?')
# pattern = re.compile(r'([월화수목금토일])\s*\((\d+(?:-\d+)?)\)\s*([^\s]*?)')

# '강의시간표 및 장소' 열을 처리하여 '요일', '교시', '장소'를 추출하는 함수
def parse_schedule(schedule):
    if pd.isna(schedule) or schedule == '미정':
        return '', '', ''
    
    lines = re.split(r'[\r\n]+', schedule)
    days = []
    periods = []
    locations = []
    
    for line in lines:
        matches = pattern.findall(line)   
        for match in matches:
            day, period_str, location = match
            days.append(day)
            # periods.append(period_str)  # 교시가 범위인 경우 문자열로 저장
            if '-' in period_str:
                periods.append(period_str)  # 교시가 범위인 경우 문자열로 저장
            else:
                periods.append(int(period_str))  # 교시가 숫자인 경우 숫자로 변환하여 저장
            if location:
                locations.append(location.strip())
            else:
                locations.append('')  # 장소가 없는 경우 빈 문자열로 처리
    
     # 리스트를 쉼표로 구분된 문자열로 변환하여 반환
    # return ','.join(days), ','.join(periods), ','.join(locations)
    return days, periods, locations

# '강의시간표 및 장소' 열을 파싱하여 새로운 열에 추가
# df[['요일', '교시', '장소']] = df['강의시간표 및 장소'].apply(lambda x: pd.Series(parse_schedule(x)))

# '강의시간표 및 장소' 열을 파싱하여 리스트로 받기
df['요일'], df['교시'], df['장소'] = zip(*df['강의시간표 및 장소'].apply(parse_schedule))



# 결과를 CSV 파일로 저장 (옵션)
output_csv = 'C:\\Users\\soobin.park\\Desktop\\devkor_backend\\csv정리본\\전공4-5_modified.csv'
df.to_csv(output_csv, index=False, encoding='utf-8-sig')

# DataFrame 출력 (테스트용)
print(df)
