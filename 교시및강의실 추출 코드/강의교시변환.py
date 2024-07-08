import pandas as pd
import ast

def transform_list(value):
    # 문자열 리스트를 실제 리스트로 변환
    try:
        parsed_value = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value
    
    if isinstance(parsed_value, list):
        if all(isinstance(x, (int, float)) for x in parsed_value):
            return [[x] for x in parsed_value]
        elif all(isinstance(x, str) for x in parsed_value) and len(parsed_value) == 1 and '-' in parsed_value[0]:
            return [[int(i) for i in parsed_value[0].split('-')]]
    return parsed_value

def process_csv_to_excel(input_csv, output_excel):
    # CSV 파일 읽기
    df = pd.read_csv(input_csv)
    
    # 각 셀에 대해 변환 함수 적용
    df = df.applymap(transform_list)
    
    # 엑셀 파일로 저장
    df.to_excel(output_excel, index=False)

# 사용 예시
input_csv = 'your_input_file.csv'
output_excel = 'your_output_file.xlsx'
process_csv_to_excel(input_csv, output_excel)

# 새로 추출?
# 숫자면 바로 2차원 ㅂ매열, 
# 2-3이;면 .....