import matplotlib.pyplot as plt
import pickle

# start_time_d = pickle.load(open("start_time_3072.p", "rb"))
# calc_time_d = pickle.load(open("./calc_time_3072.p", "rb"))

# start_time_list = sorted(start_time_d.items())
# x, y = zip(*start_time_list)
# plt.plot(x, y, '.')
# plt.title("start time")
# plt.xlabel("number of participants")
# plt.ylabel("execution time in seconds")
# plt.xticks(range(0, 25, 5))
# plt.yticks(range(0, 50, 5))
# plt.show()
#
# plt.plot(x, y)
# plt.title("start time")
# plt.xlabel("number of participants")
# plt.ylabel("execution time in seconds")
# plt.xticks(range(0, 25, 5))
# plt.yscale("log")
# plt.show()
#
# for k, v in calc_time_d.items():
#    avg = sum(calc_time_d[k]) / len(calc_time_d)
#    calc_time_d[k] = avg
# calc_time_l = sorted(calc_time_d.items())
# x, y = zip(*calc_time_l)

# plt.plot(x, y)
# plt.title("average calculation time for 3072 calculations")
# plt.xlabel("number of participants")
# plt.xticks(range(0, 25, 5))
# plt.ylabel("execution time in seconds")
# plt.show()
#
# plt.plot(x, y)
##plt.title("calculation time")
# plt.title("average calculation time for 3072 calculations")
# plt.xlabel("number of participants")
# plt.xticks(range(0, 25, 5))
# plt.yscale("log")
# plt.ylabel("execution time in seconds")
# plt.show()

# start_time_list = sorted(start_time_d.items())
# x_start, y_start = zip(*start_time_list)
#
# for k, v in calc_time_d.items():
#    avg = sum(calc_time_d[k]) / len(calc_time_d)
#    # avg = sum(calc_time_d[k])
#    calc_time_d[k] = avg
# calc_time_l = sorted(calc_time_d.items())
# x_calc, y_calc = zip(*calc_time_l)
#
# ax = plt.subplot(111)
# width = 0.2
#
# x_ticks = x_start
#
# x_calc = list(x_calc)
# for i in range(len(x_calc)):
#    x_calc[i] = x_calc[i] + width/2
# x_start= list(x_start)
# for i in range(len(x_start)):
#    x_start[i] = x_start[i] - width/2
#
# ax.bar(x_calc, y_calc, width, label="calc time", align="center")
# ax.bar(x_start, y_start, width, label="Startup time", align="center")
# ax.autoscale(tight=True)
#
# ax.set_xlabel("Participants")
# ax.set_ylabel("execution time (sec)")
# ax.legend()
# plt.yscale("log")
# plt.grid()
# plt.xticks(x_ticks, x_ticks)
# plt.show()

# calc_time_d_p3 = pickle.load(open("./calc_time_1-10000_p3.p", "rb"))
# calc_time_d_p10 = pickle.load(open("./calc_time_1-10000_p3.p", "rb"))
#
# for k, v in calc_time_d_p3.items():
#    avg = sum(calc_time_d_p3[k]) / len(calc_time_d_p3)
#    #avg = sum(calc_time_d[k])
#    calc_time_d_p3[k] = avg
# calc_time_l_p3 = sorted(calc_time_d_p3.items())
# x_calc_p3, y_calc_p3 = zip(*calc_time_l_p3)


# for k, v in calc_time_d_p10.items():
#    avg = sum(calc_time_d_p10[k]) / len(calc_time_d_p10)
#    #avg = sum(calc_time_d[k])
#    calc_time_d_p10[k] = avg
# calc_time_l_p10 = sorted(calc_time_d_p10.items())
# x_calc_p10, y_calc_p10 = zip(*calc_time_l_p10)
#
# plt.plot(x_calc_p10, y_calc_p10,".")
##plt.title("calculation time")
# plt.title("average calculation time for 3072 calculations")
# plt.xlabel("iterations")
# plt.yscale("linear")
# plt.ylabel("execution time in seconds")
# plt.show()


# ax = plt.subplot(111)
# width = 0.4
#
# x_calc_p10=list(x_calc_p10)
# for i in range(len(x_calc_p10)):
#    x_calc_p10[i] = x_calc_p10[i]+width
#
# ax.bar(x_calc_p10, y_calc_p10, width, label="calc time p10", align="center")
# ax.bar(x_calc_p3, y_calc_p3, width, label="calc time p3", align="center")
# ax.autoscale(tight=True)
#
# ax.set_xlabel("Participants")
# ax.set_ylabel("execution time (sec)")
# ax.legend()
# plt.yscale("log")
# plt.grid()
# plt.xticks(x_calc_p10,x_calc_p10)
# plt.show()


start_time_d_p3 = pickle.load(open("calc_time_1-10000_p3.p", "rb"))
start_time_d_p10 = pickle.load(open("calc_time_1-10000_p10.p", "rb"))
start_time_l_p3 = sorted(start_time_d_p3.items())
x_p3, y_p3 = zip(*start_time_l_p3)
start_time_l_p10 = sorted(start_time_d_p10.items())
x_p10, y_p10 = zip(*start_time_l_p10)

plt.plot(x_p3, y_p3, ".", label="3 participants")
plt.plot(x_p3, y_p10, ".", label="10 participants")
plt.yscale("log")
plt.title("Comparison of computing the sign-sum function with different participants")
plt.xlabel("Number of computing sign-sum function")
plt.ylabel("execution time")
plt.legend()
plt.show()
