import os
for i in range(34, 37):
    os.system("python3 scripts/eval_depth.py --epoch {}".format(i+1))

# from matplotlib import pyplot as plt
# import numpy as np
# with open("metrics.txt") as f:
#     lines = f.read().splitlines()
# N_epoch = len(lines)
# metrics = np.zeros((N_epoch, 7))
# for i, line in enumerate(lines):
#     metrics[i, :] = list(map(float, line.split()))
# fig, ax= plt.subplots(nrows=3, ncols=3, sharex=True,
#                                     figsize=(12, 12))
# ax[0, 0].set_title('Abs-Rel')
# ax[0, 0].plot(np.arange(N_epoch)+1, metrics[:, 0])

# ax[0, 1].set_title('Sq-Rel')
# ax[0, 1].plot(np.arange(N_epoch)+1, metrics[:, 1])

# ax[0, 2].set_title('RMSE')
# ax[0, 2].plot(np.arange(N_epoch)+1, metrics[:, 2])

# ax[1, 0].set_title('RMSE-Log')
# ax[1, 0].plot(np.arange(N_epoch)+1, metrics[:, 3])

# ax[1, 1].set_title('a1')
# ax[1, 1].plot(np.arange(N_epoch)+1, metrics[:, 4])

# ax[1, 2].set_title('a2')
# ax[1, 2].plot(np.arange(N_epoch)+1, metrics[:, 5])

# ax[2, 1].set_title('a3')
# ax[2, 1].plot(np.arange(N_epoch)+1, metrics[:, 6])

# fig.suptitle('Evaluation Metrics')
# plt.show()
