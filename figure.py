import matplotlib.pyplot as plt
import numpy as np
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
current_path = os.path.abspath(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(current_path, 'images')

bond_length = [0.7,
0.8,
0.9,
1,
1.1,
1.2,
1.3,
1.4,
1.5,
1.6,
1.7,
1.8,
1.9,
2,
2.1,
2.2,
2.3,
2.4,
2.5
]
hf = [-14.84151496,
-15.14608058,
-15.33853935,
-15.45576153,
-15.52210475,
-15.55370255,
-15.561404,
-15.55259645,
-15.53236268,
-15.50425036,
-15.47078815,
-15.433825,
-15.3947506,
-15.35463873,
-15.31434025,
-15.27454306,
-15.23581072,
-15.19860763,
-15.16331571
]
fci = [-14.87132976,
-15.17280541,
-15.36415094,
-15.48174107,
-15.54963817,
-15.58381205,
-15.59504708,
-15.59074335,
-15.57605125,
-15.55462369,
-15.52912134,
-15.50154509,
-15.47345142,
-15.44609374,
-15.42051855,
-15.39762993,
-15.37821354,
-15.36287431,
-15.35183431
]
one_upccgsd = [-14.86258771,
-15.16429399,
-15.35534802,
-15.47208031,
-15.53857764,
-15.57083703,
-15.57964623,
-15.57237266,
-15.55411498,
-15.52846298,
-15.4980173,
-15.46473503,
-15.43019166,
-15.39572156,
-15.36319061,
-15.33935474,
-15.307564,
-15.286951,
-15.25878288
]
uccsd = [
-14.87093547,
-15.17246706,
-15.36384473,
-15.4814481,
-15.54932273,
-15.58343747,
-15.59457844,
-15.59014317,
-15.57527204,
-15.55360068,
-15.52775918,
-15.49970176,
-15.47084737,
-15.44254842,
-15.41488732,
-15.38860869,
-15.36638353,
-15.3439368,
-15.32649794
]



COLOR = {
    'hf': 'tab:red',
    'fci': 'tab:orange',
    '1-upccgsd': 'tab:blue',
    'uccsd': 'tab:green',
    'chem_acc': 'tab:brown'
}

def image_path(name):
    if not os.path.isdir(IMAGE_PATH):
        os.makedirs(IMAGE_PATH, exist_ok=True)
    return os.path.join(IMAGE_PATH, name)

# plot style, add label
def plot_absolute(ax, data : dict):
    ls, labels = [], []
    for k in data:
        if k=='bond_length(A)':
            continue
        else:
            d = data[k]
            l, = ax.plot(data['bond_length(A)'], d, '-o', markersize=4, color=COLOR[k])
            ls.append(l)
            labels.append(k)

    ax.set_xlabel("bond_length(A)", size=16)
    ax.set_ylabel("energy(Hartree)", size=16)
    print(labels)
    return ls, labels

def plot_relative(ax, data: dict, to='fci', log=False):
    ls, labels = [], []
    d_fci = data[to]
    for k in data:
        if k == to or k=='bond_length(A)':
            continue
        else:
            d = data[k]
            if log:
                ls.append(ax.semilogy(data['bond_length(A)'], list(map(lambda x,y: x-y, d, d_fci)), '-o', markersize=4, color=COLOR[k]))
            else:
                ls.append(ax.plot(data['bond_length(A)'], list(map(lambda x,y: x-y, d, d_fci)), '-o', markersize=4, color=COLOR[k]))
            labels.append(k)
    # chemical accuracy
    ax.axhline(y=0.0014, linestyle='--', COLOR='tab:brown')
    labels.append(to)
    ax.set_xlabel("bond_length(A)", size=16)
    ax.set_ylabel("energy(Hartree) ({} = 0)".format(to), size=16)
    return ls, labels

# 绘制普通图像
def calculate(methods):
    data = {}
    data['bond_length(A)'] = bond_length
    for method in methods:
        if method == 'hf':
            data[method] = hf
        elif method == 'fci':
            data[method] = fci
        elif method == '1-upccgsd':
            data[method] = one_upccgsd
        elif method == 'uccsd':
            data[method] = uccsd

    return data

result = calculate(methods=['hf','fci', 'uccsd', '1-upccgsd','chem_acc'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax2.yaxis.set_label_position("left")
ax2.yaxis.tick_left()

ls, labels = plot_absolute(ax1, calculate(methods=['hf','fci', 'uccsd','1-upccgsd']))
plot_relative(ax2, calculate(methods=['fci','1-upccgsd','uccsd']))

ax1.set_title("BeH2 PES", loc='left')
ax2.set_title("BeH2 energy error", loc='left')

plt.tight_layout()
plt.subplots_adjust(top=0.85)
# 设置legend
lgd = fig.legend(
    ls,
    labels=labels,
    loc="upper center",
    ncol=4,
    frameon=False,
    prop={'size': 15},
    borderaxespad=-0.4,
    bbox_to_anchor=(0.5, 0.97))

plt.savefig(image_path('BeH2.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig(image_path('BeH2.pdf'), bbox_extra_artists=(lgd,), bbox_inches='tight')

""" x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
# 在绘制时设置lable, 逗号是必须的
l1, = plt.plot(x, y1, label = 'line')
l2, = plt.plot(x, y2, label = 'parabola', color = 'red', linewidth = 1.0, linestyle = '--')

# 设置坐标轴的取值范围
plt.xlim((-1, 1))
plt.ylim((0, 2))

# 设置坐标轴的lable
plt.xlabel('X axis')
plt.ylabel('Y axis')

# 设置x坐标轴刻度, 原来为0.25, 修改后为0.5
plt.xticks(np.linspace(-1, 1, 5))
# 设置y坐标轴刻度及标签, $$是设置字体
plt.yticks([0, 0.5], ['$minimum$', 'normal'])"""

plt.show()