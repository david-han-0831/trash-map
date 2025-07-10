import pandas as pd
import folium 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


user_input = input("주소를 입력하세요 (예: 서울시청): ")


geolocator = Nominatim(user_agent="my_toilet_finder")
location = geolocator.geocode(user_input)
if location is None:
    print("주소를 찾을 수 없습니다. 정확히 입력해 주세요.")
    exit()

my_location = (location.latitude, location.longitude)
print(f"입력한 위치의 좌표: {my_location}")

lat, lon = my_location

if not (33 <= lat <= 43 and 124 <= lon <= 132):
    print('이 지역은 대한민국이 아닙니다. 대한민국은 동경 124도에서 132도 사이, 북위 33도에서 43도 사이에 위치합니다.')
    exit()



df = pd.read_excel('12_04_01_E_공중화장실정보.xlsx', engine='openpyxl')

df = df.dropna(subset = ['WGS84위도','WGS84경도'])
df = df[(df['WGS84위도'] >= 33) & (df['WGS84위도'] <= 43) & (df['WGS84경도'] >= 124) & (df['WGS84경도'] <= 132)]

df['거리'] = df.apply(lambda row: geodesic(my_location, (row['WGS84위도'], row['WGS84경도'])).meters, axis=1)

near_bins = df.sort_values('거리').head(3)


m = folium.Map(location=my_location, zoom_start=15)


folium.Marker(
    location=my_location,
    popup="내 위치 (입력 주소)",
    icon=folium.Icon(color='blue', icon='user')
).add_to(m)


for idx, row in near_bins.iterrows():
    folium.Marker(
        location=[row['WGS84위도'], row['WGS84경도']],
        popup=f"{row['소재지지번주소']} ({int(row['거리'])}m)",
        icon=folium.Icon(color='blue', icon='male')
    ).add_to(m)


m.save("주소기반_화장실_지도.html")
print("지도 저장 완료: 주소기반_화장실_지도.html")






