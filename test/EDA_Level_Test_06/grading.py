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
        'condition01': (df.columns != ['기간', '구분1', '구분2', '전체', '남자', '여자']).sum() == 0,
        'condition02': df.구분1.isin(['시','구']).sum() == 286,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 10

    condition_dict = {
        'condition01': df.여자.dtype == float,
        'condition02': df.여자.isna().sum() == 50,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 5

    condition_dict = {
        'condition01': (df.구분1=='교육수준별Ⅱ(65세 이상)').sum() == 0,
        'condition02': df.여자.isna().sum() == 25,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 3, 10

    condition_dict = {
        'condition01': '여자비율' in df.columns,
        'condition02': (df.여자비율.isna().index != df.여자.isna().index).sum() == 0,
        'condition03': (df.여자비율.apply(lambda x: round(x, 6)).fillna('-') != df.여자비율.fillna('-')).sum() == 0,
        'condition04': df.loc[4, '여자비율'] == 56.783920,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 4, 10

    condition_dict = {
        'condition01': df.구.is_monotonic_increasing,
        'condition02': (df.회귀계수 < 0).sum() == 1,
        'condition03': (df.평균 < 50.5).sum() == 3,
        'condition04': (df.MinMax > 1).sum() == 2,
        'condition05': (df.평균 * 0.005 > df.표준편차).sum() == 8,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 5, 10

    condition_dict = {
        'condition01': df.여자비율.isna().sum() == 0,
        'condition02': df.여자.isna().sum() == 25,
        'condition03': df.loc[230, '여자비율'] == 52.552076,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 6, 10

    condition_dict = {
        'condition01': df.isna().sum().sum() == 0,
        'condition02': (df.남자 * 0.05 > df.여자).sum() == 18,
        'condition03': '여자비율' not in df.columns,
        'condition04': df.loc[310, '여자'] == 2,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 7, 10

    condition_dict = {
        'condition01': all(df.columns == ['구분1', '구분2', '전체', '남자', '여자']),
        'condition02': df.iloc[:,2:].sum().sum() == 0,
        'condition03': df.구분1.is_monotonic_increasing,
        'condition04': df[df.구분1=='구'].구분2.is_monotonic_increasing,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 8, 10

    condition_dict = {
        'condition01': all(df.columns == ['구분1', '구분2', '전체', '남자', '여자']),
        'condition02': sum((df.iloc[:, 2:] > 0).sum() == [1, 0, 13]) == 3,
        'condition03': df.구분1.is_monotonic_increasing,
        'condition04': df[df.구분1=='구'].구분2.is_monotonic_increasing,
        'condition05': df.loc[12, '전체'] == -0.762727,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-3
@result_deco
def check_03_03(df: pd.core.frame.DataFrame):
    question_no, points = 9, 10

    condition_dict = {
        'condition01': all(df.columns == ['구분1', '최대', '최소']),
        'condition02': df.구분1.isin(['시']).sum() == 0,
        'condition03': df.구분1.is_monotonic_increasing,
        'condition04': df.loc[0, '최대'] == '고졸',
        'condition04': df.loc[2, '최소'] == '30~44세',
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 3-4
@result_deco
def check_03_04(df: pd.core.frame.DataFrame):
    question_no, points = 10, 10

    condition_dict = {
        'condition01': all(df.columns == ['구분1', '최대', '최소']),
        'condition02': df.구분1.isin(['시']).sum() == 0,
        'condition03': df.구분1.is_monotonic_increasing,
        'condition04': df.loc[0, '최대'] == '은평구',
        'condition04': pd.isna(df.loc[2, '최소']),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

