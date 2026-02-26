from src.GPS.map import generate_map
from src.GPS.sensor import get_gps_data
from src.alert_system import send_email_alert, check_air_quality, trigger_alert



generate_map()
get_gps_data()
trigger_alert()
check_air_quality()
send_email_alert()