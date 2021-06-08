# Assignment
As soon as you connect a computer to the internet you will soon see that attempts are made to
connect to your computer via SSH. Malicious parties will try to steal your password
recommend logging in to your computer. That is why it is wise to analyze your ssh log files andfile
to take measures. In this exam you have to analyze the log file and notice a number of things.

# system.log
dt;prog;pid;ip;user;state
2020-07-13 14:10:02.332880;sshd;584;192.168.179.3;root;started
2020-07-13 15:11:03.332880;sshd;584;192.168.179.3;root;finished
2020-07-13 14:09:06.332880;sshd;140;192.168.179.9;frans;failed

# login success
2020-07-13 14:10:02.332880;sshd;584;192.168.179.3;root;started
2020-07-13 15:11:03.332880;sshd;584;192.168.179.3;root;finished

# login failed
2020-07-13 14:09:06.332880;sshd;140;192.168.179.9;frans;failed

# methods
dayCount
ipCount
longSessions
findCulprit

# imports
datetime
from opgt import readLog


# toepassingen
- timedelta
- read file (with as fp)
- read ip-adres

unknown check 





