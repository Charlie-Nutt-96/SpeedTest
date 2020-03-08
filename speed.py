import speedtest
from datetime import datetime
import time
st=speedtest.Speedtest()

print("how often in minutes would you like to log data?")
mins = int(input())
if mins<=0:
    print ('thats not possible you nonce')
    print ('I quit... ')
    exit()

print('How many times would you like to test?')
tests=int(input())
if tests<=0:
    print('if you are gunna take the piss I wont bother...')
    exit()

print ("Reset log? [y/n]")
Reset=input()
if Reset=='y':
    f= open("speed.log","w+")
elif Reset=='n':
    f= open("speed.log","a+")
else:
    print ('that wasnt [y] or [n] you donkey')
    print ('Im just gunna kill myself now...')
    exit()

micromins = (mins*tests)%60
hours = (mins*tests-micromins) / 60
microhours = hours%24
days = (hours-microhours) / 24
print('this will take %d days %d hours %d minutes' % (days,microhours,micromins))
print('dont let the laptop power off in this time')

secs = mins * 60

for i in range(tests):
    start = time.time()
    print ("%d" % i)
    now = datetime.now()
    t=now.strftime("%d/%m/%Y %H:%M:%S")
    print ("%s" % t)
    d=st.download()
    print ("%f" % d)
    u=st.upload()
    print ("%f" % u)
    f.write("%s %f %f \n" % (t,d,u))
    f.close()
    # plot commands here
    f= open("speed.log","a+")
    end=time.time()
    time.sleep(max(secs-(end-start),0))
f.close()
