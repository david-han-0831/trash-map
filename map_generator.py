from typing import Tuple
import pandas as pd
import folium

def generate_trash_bin_map(center: Tuple[float, float], bins: pd.DataFrame, output_path: str) -> None:
    """
    중심 좌표와 가까운 휴지통 데이터프레임을 받아 folium 지도를 생성하고 저장합니다.
    """
    m = folium.Map(location=center, zoom_start=15)
    folium.Marker(
        location=center,
        popup="내 위치 (입력 주소)",
        icon=folium.Icon(color='blue', icon='user')
    ).add_to(m)
    for _, row in bins.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=f"{row['설치장소명']} ({int(row['거리'])}m)",
            icon=folium.Icon(color='green', icon='trash')
        ).add_to(m)
    m.save(output_path)

def generate_toilet_map(center: Tuple[float, float], toilets: pd.DataFrame, output_path: str) -> None:
    """
    중심 좌표와 가까운 공중화장실 데이터프레임을 받아 folium 지도를 생성하고 저장합니다.
    """
    m = folium.Map(location=center, zoom_start=15)
    folium.Marker(
        location=center,
        popup="내 위치 (입력 주소)",
        icon=folium.Icon(color='blue', icon='user')
    ).add_to(m)
    for _, row in toilets.iterrows():
        folium.Marker(
            location=[row['위도'], row['경도']],
            popup=f"{row['소재지지번주소']} ({int(row['거리'])}m)",
            icon=folium.Icon(color='blue', icon='male')
        ).add_to(m)
    m.save(output_path) 