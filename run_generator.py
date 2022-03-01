import os as alpha
alpha.system("nvidia-smi")

alpha.system("nvidia-smi").nvmlInit()

handle = alpha.system("nvidia-smi").nvmlDeviceGetHandleByIndex(0)
# card id 0 hardcoded here, there is also a call to get all available card ids, so we could iterate

info = alpha.system("nvidia-smi").nvmlDeviceGetMemoryInfo(handle)

print("Total memory:", info.total)
print("Free memory:", info.free)
print("Used memory:", info.used)

alpha.system("nvidia-smi").nvmlShutdown()
