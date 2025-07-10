from typing import Optional, Tuple
from geopy.geocoders import Nominatim

def get_location_from_address(address: str) -> Optional[Tuple[float, float]]:
    """
    주소를 받아 (위도, 경도) 튜플을 반환합니다. 실패 시 None 반환.
    """
    geolocator = Nominatim(user_agent="my_trash_finder")
    try:
        location = geolocator.geocode(address)
        if location is None:
            return None
        return (location.latitude, location.longitude)
    except Exception:
        return None 