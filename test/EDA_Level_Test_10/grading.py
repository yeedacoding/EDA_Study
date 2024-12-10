import pandas as pd

points_list = [0] * 7

def result_deco(func):
    def wrapper(*args, **kwargs):
        global points_list
        question_no, points, result = func(*args, **kwargs)
        if result:
            points_list[question_no] = points
            print(f'정답입니다! {points}점 누적 되었습니다!')
        else:
            points_list[question_no] = 0
            print('오답입니다. 다시 한번 확인해주세요.')       

        print('현재 누적 점수:', sum(points_list), '/ 100')
        
    return wrapper

# 1-1
@result_deco
def check_01_01(df: pd.core.frame.DataFrame):
    question_no, points = 0, 5

    try:
        condition_dict = {
            'condition01': len(df) == 318,
            'condition02': len(df.columns) == 12,
            'condition03': df.columns[3:].is_monotonic_increasing,
            'condition04': all(df.columns[3:] == list(map(str, range(2013, 2022)))),
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 10

    try:
        condition_dict = {
            'condition01': len(df) == 26,
            'condition02': all(df.columns == ['자치구', '구분', *list(map(str, range(2013, 2022)))]),
            'condition03': all(~df.자치구.isin(['소계', '강남', '강북'])),
            'condition04': not df.구분.is_unique,
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 10

    try:
        condition_dict = {
            'condition01': len(df) == 26 * 3,
            'condition02': all(df.columns == ['자치구', '구분', *list(map(str, range(2013, 2022)))]),
            'condition03': all(~df.자치구.isin(['소계'])),
            'condition04': (df.iloc[:,2:].applymap(type) == float).sum().sum() == len(df) * len(range(2013, 2022)),
            'condition05': df[['자치구', '구분']].applymap(lambda x: '(' in x).sum().sum() == 0,
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 1-4
@result_deco
def check_01_04(df: pd.core.frame.DataFrame):
    question_no, points = 3, 15

    gu_list = ['서울시', '종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
    cat_list = ['발생건수', '사망자수', '부상자수', '차량통행속도', '인구', '면적', '인구밀도']
    type_list = ['합계', '차대사람', '차대차', '차량단독', '건널목', '-']

    try:
        condition_dict = {
            'condition01': len(df) == 422,
            'condition02': sum(df.사고유형 == '-') == 104,
            'condition03': all(df.자치구.unique() == gu_list) and all(df.사고유형.unique() == type_list) and all(df.구분.unique() == cat_list),
            'condition04': all(df.columns == ['자치구', '사고유형', '구분', *list(map(str, range(2013, 2022)))]),
            'condition05': (df.iloc[:,3:].applymap(type) == float).sum().sum() == len(df) * len(range(2013, 2022)),
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 4, 20

    cat_list = ['인구 만명당 발생건수', '인구 만명당 사망자수', '인구 만명당 부상자수', '인구밀도당 부상자수', '인구밀도당 사망자수', '인구밀도당 발생건수', '차량통행속도당 사망자수', '차량통행속도당 발생건수', '차량통행속도당 부상자수']
    type_list = ['합계', '차대사람', '차대차', '차량단독']

    try:
        condition_dict = {
            'condition01': len(df) == 36,
            'condition02': all(df.사고유형.unique() == type_list) and all(df.구분.unique() == cat_list),
            'condition03': all(df.columns == ['자치구', '사고유형', '구분', *list(map(str, range(2013, 2022)))]),
            'condition04': (df.iloc[:,3:] == df.iloc[:,3:].round(2)).sum().sum() == len(df) * len(range(2013, 2022)),
            'condition05': all(df.index == range(len(df))),
            'condition06': (df.iloc[21, 7], df.iloc[29, 4],df.iloc[7, 11]) == (0.19, 4.72, 34.42),
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 5, 20

    gu_list = ['서울시', '종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
    cat_list = ['인구 만명당 발생건수', '인구 만명당 사망자수', '인구 만명당 부상자수', '인구밀도당 발생건수', '인구밀도당 사망자수', '인구밀도당 부상자수',  '차량통행속도당 발생건수', '차량통행속도당 사망자수',  '차량통행속도당 부상자수']
    type_list = ['합계', '차대사람', '차대차', '차량단독', '건널목']

    try:
        condition_dict = {
            'condition01': len(df) == 954,
            'condition02': all(df.자치구.unique() == gu_list) and all(df.사고유형.unique() == type_list) and all(df.구분.unique() == cat_list),
            'condition03': all(df.columns == ['자치구', '사고유형', '구분', *list(map(str, range(2013, 2022)))]),
            'condition04': (df.iloc[:,3:] == df.iloc[:,3:].round(2)).sum().sum() == len(df) * len(range(2013, 2022)),
            'condition05': all(df.index == range(len(df))),
            'condition06': (df.iloc[124, 7], df.iloc[467, 4],df.iloc[234, 11]) == (0.33, 19.58, 60.7),
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

# 3
@result_deco
def check_03(df: pd.core.frame.DataFrame):
    question_no, points = 6, 20

    columns = ['사고유형', '구분', '연도', '자치구', '값']
    cat_list = ['인구 만명당 발생건수', '인구밀도당 발생건수', '차량통행속도당 발생건수']

    try:
        condition_dict = {
            'condition01': len(df) == 27,
            'condition02': all(df.자치구.unique() == ['중구', '강남구', '서초구', '강동구']) and all(df.사고유형.unique() == ['합계']) and all(df.구분.unique() == cat_list) and all(df.연도.unique() == list(map(str, range(2013,2022)))),
            'condition03': all(df.columns == columns),
            'condition04': all(df.index == range(len(df))),
            'condition05': (df.값.sum().round(2), df.값.mean().round(2)) == (2180.07, 80.74),
            'condition06': (df.값.iloc[2], df.값.iloc[17], df.값.iloc[25]) == (99.61, 5.54, 150.08),
        }

        if sum(condition_dict.values()) == len(condition_dict):
            result = True
        else:
            result = False
    except:
        result = False
        
    return question_no, points, result

