from plyer import notification
from .battery_info import get_battery_info

def notify_battery_full():
    info = get_battery_info()
    if info['percent'] == 100 and info['plugged']:
        notification.notify(
            title='Battery Full',
            message='Battery is at 100%. Please unplug the charger.',
            timeout=10
        )
