# %%
import matplotlib.pylab as plt
import numpy as np
import tracemalloc
import pandas as pd
import time

# %%
plt.figure()
plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
plt.show()
# %%
def tracing_start():
    tracemalloc.stop()
    print("nTracing Status : ", tracemalloc.is_tracing())
    tracemalloc.start()
    print("Tracing Status : ", tracemalloc.is_tracing())
def tracing_mem():
    first_size, first_peak = tracemalloc.get_traced_memory()
    peak = first_peak/(1024*1024)
    print("Peak Size in MB - ", peak)
# %%
tracing_start()
start = time.time()
sq_list1 = [elem + elem**2 for elem in range(1,1000)]
#print(sq_list1)
end = time.time()
print("time elapsed {} milli seconds".format((end-start)*1000))
tracing_mem()
# %%

# %%


def time_performance(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        oper_millsec = (end-start)*1000
        return oper_millsec
    return wrapper


@time_performance
def add_element(data_structure, element):
    data_structure.append(element)


perormance_time = []
list1 = []
for elem in range(1, 10000):
    perormance_time.append(add_element(list1, elem))
plt.figure()
plt.plot(perormance_time)
plt.show()


# sq_list1 = []
# perormance_time = []
# for elem in range(1, 1000):
#     start = time.time()
#     sq_list1.append(elem)
#     end = time.time()
#     oper_millsec = (end-start)*1000
#     perormance_time.append(oper_millsec)
# plt.figure()
# plt.plot(perormance_time)
# plt.show()

# %%
