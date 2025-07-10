import pandas as pd

def load_and_clean_data(csv_path: str) -> pd.DataFrame:
    """
    휴지통 CSV 파일을 로드하고, 위도/경도 정제 및 대한민국 영역 필터링을 수행합니다.
    """
    df = pd.read_csv(csv_path, encoding='utf-8-sig')
    df['위도'] = pd.to_numeric(df['위도'], errors='coerce')
    df['경도'] = pd.to_numeric(df['경도'], errors='coerce')
    df = df.dropna(subset=['위도', '경도'])
    df = df[(df['위도'] >= 33) & (df['위도'] <= 43) & (df['경도'] >= 124) & (df['경도'] <= 132)]
    return df

def load_and_clean_toilets(xlsx_path: str) -> pd.DataFrame:
    """
    공중화장실 엑셀 파일을 로드하고, 위도/경도 정제 및 대한민국 영역 필터링을 수행합니다.
    """
    df = pd.read_excel(xlsx_path, engine='openpyxl')
    df = df.dropna(subset=['WGS84위도', 'WGS84경도'])
    df['위도'] = pd.to_numeric(df['WGS84위도'], errors='coerce')
    df['경도'] = pd.to_numeric(df['WGS84경도'], errors='coerce')
    df = df[(df['위도'] >= 33) & (df['위도'] <= 43) & (df['경도'] >= 124) & (df['경도'] <= 132)]
    return df 