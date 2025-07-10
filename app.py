import streamlit as st
from data_loader import load_and_clean_data, load_and_clean_toilets
from geocode_utils import get_location_from_address
from map_generator import generate_trash_bin_map, generate_toilet_map
from geopy.distance import geodesic
import pandas as pd
from streamlit.components.v1 import html
import tempfile
import os

st.set_page_config(page_title="위치기반 지도 서비스", layout="wide")
st.title("위치기반 지도 서비스")

tabs = st.tabs(["휴지통 지도", "공중화장실 지도"])

with tabs[0]:
    st.header("휴지통 지도")
    address = st.text_input("주소를 입력하세요 (예: 서울시청)", key="trash")
    if address:
        loc = get_location_from_address(address)
        if loc is None:
            st.error("주소를 찾을 수 없습니다. 정확히 입력해 주세요.")
        else:
            df = load_and_clean_data('전국휴지통표준데이터.csv')
            df['거리'] = df.apply(lambda row: geodesic(loc, (row['위도'], row['경도'])).meters, axis=1)
            near_bins = df.sort_values('거리').head(3)
            # folium 지도 임시 파일로 저장 후 html로 임베드
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
                generate_trash_bin_map(loc, near_bins, tmpfile.name)
                tmpfile.flush()
                with open(tmpfile.name, 'r', encoding='utf-8') as f:
                    map_html = f.read()
                html(map_html, height=500)
            os.unlink(tmpfile.name)

with tabs[1]:
    st.header("공중화장실 지도")
    address = st.text_input("주소를 입력하세요 (예: 서울시청)", key="toilet")
    if address:
        loc = get_location_from_address(address)
        if loc is None:
            st.error("주소를 찾을 수 없습니다. 정확히 입력해 주세요.")
        else:
            df = load_and_clean_toilets('12_04_01_E_공중화장실정보.xlsx')
            df['거리'] = df.apply(lambda row: geodesic(loc, (row['위도'], row['경도'])).meters, axis=1)
            near_toilets = df.sort_values('거리').head(3)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
                generate_toilet_map(loc, near_toilets, tmpfile.name)
                tmpfile.flush()
                with open(tmpfile.name, 'r', encoding='utf-8') as f:
                    map_html = f.read()
                html(map_html, height=500)
            os.unlink(tmpfile.name) 