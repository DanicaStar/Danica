import  time
stric1=time.time()     #获取时间戳
localtime1= time.localtime(stric1)     #(tm_year=2020, tm_mon=12, tm_mday=4, tm_hour=10, tm_min=57, tm_sec=24, tm_wday=4, tm_yday=339, tm_isdst=0)
time1=time.strftime("%Y-%m-%d %H:%M:%S",localtime1)   #格式化时间，记录开始时间
print("开始时间为：",time1)
print(stric1)
print(localtime1)
list=[]
for i in range(10):
    list.append("str")
a="*".join(list)
print(a)

stric2=time.time()
localtime2= time.localtime(stric2)
time2=time.strftime("%Y-%m-%d %H:%M:%S",localtime2)   #记录结束时间
print("结束时间为：",time2)
time3=stric2-stric1
#time3=time.strptime(time03, "%Y-%m-%d %H:%M:%S") 
print ("程序的运行时间为：",time3)




