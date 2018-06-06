import psutil, datetime, subprocess
from subprocess import PIPE
# print('##########MEM##########')
# mem =  psutil.virtual_memory()
# print(mem)
# print(mem.total)
# print(mem.used)
# print(mem.used/mem.total)
# # svmem(total=17045966848, available=8977645568, percent=47.3, used=8068321280, free=8977645568)
# # 17045966848
# # 8068321280
# # 0.473327289202528
# print('##########CPU##########')
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_times())
# print(psutil.cpu_times_percent())
# # 2
# # scputimes(user=180123.49999999997, system=203529.609375, idle=2720648.359375, interrupt=4547.140625, dpc=1787.578125)
# # scputimes(user=0.0, system=0.0, idle=0.0, interrupt=0.0, dpc=0.0)

# #disk
# print('##########DISK##########')
# print(psutil.disk_partitions())
# print(psutil.disk_io_counters())
# print(psutil.disk_usage("/"))
# print('##########NET##########')
# print(psutil.net_io_counters())
# print(psutil.net_io_counters(pernic=True))
# # [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')]
# # sdiskio(read_count=3653294, write_count=6437060, read_bytes=115110837248, write_bytes=196411829248, read_time=1961, write_time=5164)
# # sdiskusage(total=252974198784, used=92170276864, free=160803921920, percent=36.4)
# # ##########NET##########
# # snetio(bytes_sent=3312205183, bytes_recv=13996691748, packets_sent=7590343, packets_recv=12663531, errin=0, errout=0, dropin=0, dropout=0)
# # {'Wi-Fi': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Local Area Connection* 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Ethernet': snetio(bytes_sent=3312205183, bytes_recv=13996691748, packets_sent=7590343, packets_recv=12663531, errin=0, errout=0, dropin=0, dropout=0), 'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}

#
# print('##########OTHER##########')
# print(psutil.users())
# print(psutil.boot_time())
#
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
# # [suser(name='jcao', terminal=None, host='0.4.0.0', started=1528247290.0, pid=None)]
# # 1527490528.0
# # 2018-05-28 14:55:28
# print('##########PROCESS##########')
print(psutil.pids())
print(psutil.Process(21768))
p = psutil.Process(21768)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.status())
print(p.create_time())
print(p.cpu_times())
print(p.memory_percent())
print(p.memory_info())
print(p.io_counters())
print(p.connections())
# print(p.kill())
print(psutil.Popen(["/user/bin/python", "-c", "print('hello')"],stdout=PIPE ))





#
# [0, 4, 376, 548, 656, 740, 748, 932, 960, 980, 988, 552, 884, 1128, 1140, 1248, 1272, 1292, 1320, 1384, 1396, 1472, 1548, 1652, 1692, 1832, 1948, 2000, 1524, 1740, 1776, 1772, 1884, 2064, 2084, 2172, 2208, 2400, 2420, 2520, 2592, 2616, 2680, 2728, 2804, 2812, 2980, 3096, 3224, 3296, 3336, 3344, 3352, 3376, 3592, 3696, 3816, 3956, 3964, 3972, 3984, 3996, 4020, 4028, 4036, 4084, 3204, 3496, 4104, 4144, 4176, 4204, 4224, 4252, 4296, 4344, 4352, 4404, 4432, 4452, 4788, 4924, 4988, 5228, 5536, 5972, 6008, 6768, 6824, 8112, 8088, 7248, 7068, 3192, 7660, 7028, 6692, 7144, 3168, 2788, 7672, 3184, 8720, 8836, 10852, 13220, 15108, 14376, 7716, 8348, 11040, 14480, 18120, 13364, 18548, 16572, 8176, 20524, 6212, 11184, 11072, 6720, 12540, 6292, 15572, 20212, 4804, 6540, 17588, 18800, 12676, 2244, 4800, 24664, 21704, 4760, 10216, 24440, 3416, 22208, 11248, 15964, 2608, 21356, 22704, 22320, 25568, 23268, 19272, 12532, 8148, 24300, 4064, 8096, 3280, 22492, 17628, 20756, 25072, 6572, 19988, 23296, 16396, 17692, 15560, 17812, 15764, 5456, 4332, 19336, 25032, 23252, 4644, 7804, 15252, 21596, 416, 22024, 9124, 20316, 3936, 25488, 17036, 9788, 22552, 3028, 10824, 7124, 16736, 6360, 15064, 12168, 1228, 2868, 14220, 2784, 13164, 8640, 8140, 24252, 16292, 23108, 20836, 6624, 1196, 24456, 20808, 10664, 20232, 18516, 18900, 21196, 25464, 20540, 3448, 572, 4292, 10944, 8264, 4828, 24500, 19048, 1284, 12796, 9624, 25220, 5532, 18904, 12364, 5552, 2232, 21164, 16140, 23952, 12244, 13140, 6908, 3048, 16196, 760, 10984, 19108, 16236, 21464, 22288, 24788, 22164, 22912, 14028, 20160, 18168, 21768, 13976, 17396, 21616, 5564, 19920, 22600]
# psutil.Process(pid=2804, name='svchost.exe', started='2018-05-28 14:55:31')
# chrome.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe











