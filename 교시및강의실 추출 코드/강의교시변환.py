import pandas as pd
import ast

def transform_list(value):
    try:
        parsed_value = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value
    
    if isinstance(parsed_value, list):
        transformed_value = []
        for item in parsed_value:
            if isinstance(item, int):
                transformed_value.append([item])
            elif isinstance(item, str) and '-' in item:
                try:
                    start, end = map(int, item.split('-'))
                    transformed_value.append(list(range(start, end + 1)))
                except ValueError:
                    transformed_value.append(item)
            else:
                transformed_value.append(item)
        return transformed_value
    return parsed_value


def process_csv_to_excel(input_csv, output_excel, column_to_transform):
    df = pd.read_csv(input_csv)
    # 특정 열에만 transform_list 함수 적용
    
    df[column_to_transform] = df[column_to_transform].apply(transform_list)

    df.to_excel(output_excel, index=False)

# 사용 예시
input_csv = output_csv = 'C:\\Users\\soobin.park\\Desktop\\re_뎁코백엔드깃헙\\교시및강의실추출\\학세탐.csv'
output_excel = 'C:\\Users\\soobin.park\\Desktop\\re_뎁코백엔드깃헙\\강의교시변환_최종본\\학세탐.xlsx'
process_csv_to_excel(input_csv, output_excel, '교시')
