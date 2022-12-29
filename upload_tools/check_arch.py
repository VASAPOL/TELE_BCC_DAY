import cpuinfo as cpu_s
from sys import platform

manufacturer = cpu_s.get_cpu_info().get('brand_raw')        #get arch
arch = 'arm' if 'm1' in manufacturer.lower() else 'intel'   #arch convertion


def check_platform():
    if platform == "linux" or platform == "linux2":
        return 'linux'
    elif platform == "darwin":
        if arch == 'arm':
            return 'arm macos'
        else :
            return 'intel'
    elif platform == "win32":
        return 'window'