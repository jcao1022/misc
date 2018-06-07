import psutil, datetime, subprocess
from subprocess import PIPE
print('##########MEM##########')
mem =  psutil.virtual_memory()
print(mem)
print(mem.total)
print(mem.used)
print(mem.used/mem.total)
# svmem(total=17045966848, available=8977645568, percent=47.3, used=8068321280, free=8977645568)
# 17045966848
# 8068321280
# 0.473327289202528
print('##########CPU##########')
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_times_percent())
# 2
# scputimes(user=180123.49999999997, system=203529.609375, idle=2720648.359375, interrupt=4547.140625, dpc=1787.578125)
# scputimes(user=0.0, system=0.0, idle=0.0, interrupt=0.0, dpc=0.0)

#disk
print('##########DISK##########')
print(psutil.disk_partitions())
print(psutil.disk_io_counters())
print(psutil.disk_usage("/"))
print('##########NET##########')
print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')]
# sdiskio(read_count=3653294, write_count=6437060, read_bytes=115110837248, write_bytes=196411829248, read_time=1961, write_time=5164)
# sdiskusage(total=252974198784, used=92170276864, free=160803921920, percent=36.4)
# ##########NET##########
# snetio(bytes_sent=3312205183, bytes_recv=13996691748, packets_sent=7590343, packets_recv=12663531, errin=0, errout=0, dropin=0, dropout=0)
# {'Wi-Fi': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Local Area Connection* 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Ethernet': snetio(bytes_sent=3312205183, bytes_recv=13996691748, packets_sent=7590343, packets_recv=12663531, errin=0, errout=0, dropin=0, dropout=0), 'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}


print('##########OTHER##########')
print(psutil.users())
print(psutil.boot_time())

print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
# [suser(name='jcao', terminal=None, host='0.4.0.0', started=1528247290.0, pid=None)]
# 1527490528.0
# 2018-05-28 14:55:28
print('##########PROCESS##########')
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
p = psutil.Popen(["/user/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()
p.connections()
p.communication()
p.cpu_times()









