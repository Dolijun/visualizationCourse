# import os
# import pandas as pd
# import cv2
# from tqdm import tqdm

# 统计数据集所有图像的信息
# df = pd.DataFrame()
# root = "fruit81_full"
# for fruit in tqdm(os.listdir(root)):
#     for filename in os.listdir(os.path.join(root, fruit)):
#         try:
#             file_path = os.path.join(root, fruit, filename)
#             img = cv2.imread(file_path)
#             df = df._append({'类别': fruit, '图像路径': file_path, '宽度': img.shape[1], '高度': img.shape[0]}, ignore_index=True)
#         except:
#             print(file_path, "读取失败")
#
#     df.to_excel("static_info.xlsx", index=False)
# dt = pd.read_excel("static_info.xlsx")
# df = pd.DataFrame(dt)

# # 根据类别统计信息进行可视化
# from scipy.stats import gaussian_kde
# from matplotlib.colors import LogNorm
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = df["宽度"]
# y = df["高度"]
# xy = np.vstack([x, y])
# z = gaussian_kde(xy)(xy)
#
# idx = z.argsort()
# x, y, z = x[idx], y[idx], z[idx]
#
# plt.scatter(x, y, c=z, cmap="Spectral_r")
# plt.tick_params(labelsize=15)
#
# xy_max = max(max(df["宽度"]), max(df["高度"]))
#
# plt.xlim(xmin=0, xmax=xy_max)
# plt.ylim(ymin=0, ymax=xy_max)
#
# plt.ylabel("height", fontsize=25)
# plt.xlabel("width", fontsize=25)
#
# plt.savefig("size_static.pdf", dpi=300, bbox_inches="tight")
#
# plt.show()

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置 matplotlib 字体
matplotlib.rc("font", family="SimHei")
plt.rcParams["axes.unicode_minus"]=False

dt = pd.read_excel("static_info.xlsx")
df = pd.DataFrame(dt)

nd = np.array(df["类别"])
dict_ = {}
for c in nd:
    if c not in dict_.keys():
        dict_[c] = 1
    else:
        dict_[c] += 1
plt.figure(figsize=(22, 7))

x = dict_.keys()
y = dict_.values()

plt.bar(x, y, facecolor="#1f77b4", edgecolor='k')

plt.xticks(rotation=90)
plt.tick_params(labelsize=10)
plt.xlabel("类别", fontsize=20)
plt.ylabel("图像数量", fontsize=20)
plt.savefig("classes_static.pdf", dpi=300, bbox_inches="tight")
plt.show()
