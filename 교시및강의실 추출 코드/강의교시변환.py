import pandas as pd
import ast

def transform_list(value):
    try:
        parsed_value = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value
    
    if isinstance(parsed_value, list):
        if all(isinstance(x, str) and '-' in x for x in parsed_value):
            return [[int(i) for i in x.split('-')] for x in parsed_value]
        elif all(isinstance(x, (int, float)) for x in parsed_value):
            return [[x] for x in parsed_value]
    return parsed_value

def process_csv_to_excel(input_csv, output_excel):
    df = pd.read_csv(input_csv)
    df = df.applymap(transform_list)
    df.to_excel(output_excel, index=False)

# 사용 예시
input_csv = 'your_input_file.csv'
output_excel = 'your_output_file.xlsx'
process_csv_to_excel(input_csv, output_excel)

# 새로 추출?
# 숫자면 바로 2차원 ㅂ매열, 
# 2-3이;면 .....