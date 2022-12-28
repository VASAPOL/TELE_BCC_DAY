import cpuinfo as cpu_s
from sys import platform

manufacturer = cpu_s.get_cpu_info().get('brand_raw')        #get arch
arch = 'arm' if 'm1' in manufacturer.lower() else 'intel'   #arch convertion


if platform == "linux" or platform == "linux2":
    print ('linux')
elif platform == "darwin":
    if arch == 'arm':
        print('arm macos')
    else :
        print('intel')
elif platform == "win32":
    print ('window')
   