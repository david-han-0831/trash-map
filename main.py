from data_loader import load_and_clean_data, load_and_clean_toilets
from geocode_utils import get_location_from_address
from map_generator import generate_trash_bin_map, generate_toilet_map
from geopy.distance import geodesic

if __name__ == "__main__":
    while True:
        print('\n ========위치기반 지도리스트=======')
        print('1. 휴지통')
        print('2. 공중화장실')
        print('3. 나가기')
        c = input('메뉴번호를 입력하시오 : ')
        if c == '1':
            address = input('주소를 입력하세요 (예: 서울시청): ')
            loc = get_location_from_address(address)
            if loc is None:
                print('[오류] 주소를 찾을 수 없습니다. 정확히 입력해 주세요.')
                continue
            df = load_and_clean_data('전국휴지통표준데이터.csv')
            df['거리'] = df.apply(lambda row: geodesic(loc, (row['위도'], row['경도'])).meters, axis=1)
            near_bins = df.sort_values('거리').head(3)
            generate_trash_bin_map(loc, near_bins, '주소기반_휴지통_지도.html')
            print('지도 저장 완료: 주소기반_휴지통_지도.html')
        elif c == '2':
            address = input('주소를 입력하세요 (예: 서울시청): ')
            loc = get_location_from_address(address)
            if loc is None:
                print('[오류] 주소를 찾을 수 없습니다. 정확히 입력해 주세요.')
                continue
            df = load_and_clean_toilets('12_04_01_E_공중화장실정보.xlsx')
            df['거리'] = df.apply(lambda row: geodesic(loc, (row['위도'], row['경도'])).meters, axis=1)
            near_toilets = df.sort_values('거리').head(3)
            generate_toilet_map(loc, near_toilets, '주소기반_화장실_지도.html')
            print('지도 저장 완료: 주소기반_화장실_지도.html')
        elif c == '3':
            print('프로그램을 종료합니다.')
            break
        else:
            print('[오류] 잘못된 입력입니다. 다시 선택해 주세요.') 