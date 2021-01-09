import matplotlib.pyplot as plt
import pickle

start_time_d = pickle.load(open("./start_time.p", "rb"))
calc_time_d = pickle.load(open("./calc_time.p", "rb"))


#start_time_list = sorted(start_time_d.items())
#x, y = zip(*start_time_list)
#plt.plot(x, y)
#plt.title("start time")
#plt.xlabel("number of participants")
#plt.ylabel("execution time in seconds")
#plt.xticks(range(0, 25, 5))
#plt.yticks(range(0, 50, 5))
#plt.show()
#
#plt.plot(x, y)
#plt.title("start time")
#plt.xlabel("number of participants")
#plt.ylabel("execution time in seconds")
#plt.xticks(range(0, 25, 5))
#plt.yscale("log")
#plt.show()
#
for k, v in calc_time_d.items():
    avg = sum(calc_time_d[k]) / len(calc_time_d)
    calc_time_d[k] = avg

calc_time_l = sorted(calc_time_d.items())
x, y = zip(*calc_time_l)
plt.plot(x, y)
plt.title("average calculation time for 3072 calculations")
plt.xlabel("number of participants")
plt.xticks(range(0, 25, 5))
plt.ylabel("execution time in seconds")
plt.show()

plt.plot(x, y)
#plt.title("calculation time")
plt.title("average calculation time for 3072 calculations")
plt.xlabel("number of participants")
plt.xticks(range(0, 25, 5))
plt.yscale("log")
plt.ylabel("execution time in seconds")
plt.show()