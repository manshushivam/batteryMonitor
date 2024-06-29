import psutil

def get_battery_info():
    battery = psutil.sensors_battery()
    return {
        'percent': battery.percent,
        'plugged': battery.power_plugged,
        'secsleft': battery.secsleft
    }
