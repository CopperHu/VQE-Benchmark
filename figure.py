import matplotlib.pyplot as plt
import numpy as np
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
current_path = os.path.abspath(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(current_path, 'images')

bond_length = [0.4,0.5,0.6,0.8,0.9,1,1.3,1.5]
#[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
hf = [-71.06282955,
-73.12423439,
-74.1275568,
-74.85022706,
-74.94502101,
-74.96466254,
-74.83613482,
-74.70415687
]
fci = [-71.07194128,
-73.13764403,
-74.14620411,
-74.8830018,
-74.9876927,
-75.0198548,
-74.94877911,
-74.87343609
]
ccsd = [-71.07193001,-73.1376252,-74.14617586,-74.88293945,-74.98760054,-75.01971514,-74.94821456,-74.87247615]
uccsd = [-71.07192663,
-73.13762103,
-74.14617092,
-74.88293433,
-74.98760116,
-75.01973432,
-74.94851308,
-74.87309854,
]



COLOR = {
    'hf': 'tab:red',
    'fci': 'tab:orange',
    'ccsd': 'tab:blue',
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
    ax.axhline(y=0.0014, linestyle='--')
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
        elif method == 'ccsd':
            data[method] = ccsd
        elif method == 'uccsd':
            data[method] = uccsd

    return data

result = calculate(methods=['hf','fci','ccsd','uccsd','chem_acc'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax2.yaxis.set_label_position("left")
ax2.yaxis.tick_left()

ls, labels = plot_absolute(ax1, calculate(methods=['hf','fci','ccsd','uccsd']))
plot_relative(ax2, calculate(methods=['fci','ccsd','uccsd']))

ax1.set_title("H2O PES", loc='left')
ax2.set_title("H2O energy error", loc='left')

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

plt.savefig(image_path('h2o.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig(image_path('h2o.pdf'), bbox_extra_artists=(lgd,), bbox_inches='tight')

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