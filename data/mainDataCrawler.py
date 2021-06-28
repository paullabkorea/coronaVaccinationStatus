import numpy as np
import pandas as pd

table = pd.read_html('https://ncv.kdca.go.kr/mainStatus.es?mid=a11702000000', encoding='utf-8')
인구 = pd.read_csv('./populationData.csv', encoding='cp949')

인구['1차 접종 누계'] = table[1]['1회차 접종']['당일 누계']
인구['2차 접종 누계'] = table[1]['2회차 접종']['당일 누계']

인구['1차 접종 퍼센트'] = (인구['1차 접종 누계'] / 인구['총인구 (명)']) * 100
인구['2차 접종 퍼센트'] = (인구['2차 접종 누계'] / 인구['총인구 (명)']) * 100

인구.to_json('data.json', force_ascii=False, orient='records')
