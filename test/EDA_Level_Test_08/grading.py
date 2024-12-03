import pandas as pd

points_list = [0] * 11

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

    condition_dict = {
        'condition01': len(df) == 60060,
        'condition02': len(df[df.사용월==202205]) == 1230,
        'condition03': df[df.사용월==202205].유임승차인원.sum() == 336278144,
        'condition04': len(df.columns) == 8,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 5

    condition_dict = {
        'condition01': len(df) == 51162,
        'condition02': len(df[df.사용월==202205]) == 615,
        'condition03': df[df.사용월==202205].유임승차인원.sum() == 168139072,
        'condition04': df.index.is_monotonic_increasing,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 10

    condition_dict = {
        'condition01': len(df) == 51092,
        'condition02': len(df[df.사용월==201812]) == 595,
        'condition03': df.loc[32888].values[3:7].sum() == 138191,
        'condition04': df.index.is_monotonic_increasing,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-4
@result_deco
def check_01_04(df: pd.core.frame.DataFrame):
    question_no, points = 3, 5

    condition_dict = {
        'condition01': len(df) == 51092,
        'condition02': len(df[df.호선명 == '9호선']) == 3034,
        'condition03': len(df[df.지하철역 == '잠실새내']) == 90,
        'condition04': len(df[df.지하철역.isin(['(', ')'])]) == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-5
@result_deco
def check_01_05(df: pd.core.frame.DataFrame):
    question_no, points = 4, 10

    condition_dict = {
        'condition01': len(df[df.호선명 == '7호선']) == 3780,
        'condition02': len(df[df.호선명 == '7호선 인천']) == 799,
        'condition03': df[df.호선명 == '7호선'].유임승차인원.sum() == 1342712883,
        'condition04': df.index.is_monotonic_increasing,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 5, 5

    condition_dict = {
        'condition01': df.index.is_monotonic_increasing,
        'condition02': df.iloc[-2].name == '효창공원앞',
        'condition03': df.iloc[256].sum() == 432588,
        'condition04': len(df) == 524,
        'condition05': len(df.columns) == 4,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 6, 10

    condition_dict = {
        'condition01': len(df) == 10,
        'condition02': df.호선수.is_monotonic_decreasing,
        'condition03': df[df.호선수==3].index.is_monotonic_decreasing,
        'condition04': df.columns[0] == '호선수',
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 7, 10

    condition_dict = {
        'condition01': len(df) == 10,
        'condition02': df[df.호선수==3].환승호선.is_monotonic_increasing,
        'condition03': df.iloc[-1].name == '디지털미디어시티',
        'condition04': all(df.columns == ['호선수', '환승호선']),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 8, 10

    condition_dict = {
        'condition01': len(df) == 23,
        'condition02': df[df.호선수==3].무임승하차율.is_monotonic_decreasing,
        'condition03': df.iloc[-1].name == '합정',
        'condition04': df.columns.str.contains('승하차율').sum() == 3,
        'condition05': len(df[df.호선수==2]) == 17,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 9, 15

    condition_dict = {
        'condition01': len(df) == 6,
        'condition02': sum(df.유동인구증감률 > -5) == 3,
        'condition03': df.유동인구증감률.sum() < -100,
        'condition04': df.index[2] == '구반포',
        'condition05': all([(df.iloc[i, :] > df.iloc[i+1, :]).유동인구증감률 for i in range(len(df)-1)]),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 10, 15

    condition_dict = {
        'condition01': len(df) == 17,
        'condition02': sum(df.호선명 == '5호선') == 5,
        'condition03': df[df.호선명 == '9호선'].신설월.is_monotonic_decreasing,
        'condition04': df.loc[[9,10], '지하철역'].is_monotonic_increasing,
        'condition05': all(df.index == range(17)),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result