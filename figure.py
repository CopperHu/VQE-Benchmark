import matplotlib.pyplot as plt
import numpy as np
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
current_path = os.path.abspath(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(current_path, 'images')

bond_length = [0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
#[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
hf = [-2.7489969585270506, -3.020144532388091, -3.1346122556993024, 
-3.1607433635619886, -3.1355322139663, -3.006753467084848, 
-2.9240604854986474, -2.8373157242246476, -2.7501500441838154, -2.6649830750728105, 
-2.5834077202079944, -2.5064402766675933, -2.4346810960608742, -2.3684212842827153, -2.2524669201642173,
 -2.1573199749555823, -2.080475139704439, -2.0191297425412404, -1.9706022460146242]
fci = [-2.796419230339956, -3.0779954519765003, -3.204411879484107, 
-3.244542240044894, -3.236066279892344, -3.151729141125461, 
-3.0978256472309074, -3.044600244086702, -2.9955654258319395, 
-2.9526683640244045, -2.9166892428878852, -2.8875693764359553, -2.864702877760445, -2.8471921339556046, 
-2.8243416519132496, -2.81211947490214, -2.80578476479308, -2.802565368060126, 
-2.800958899654437]
one_upccgsd = [-2.77227,
-3.04669,
-3.1644,
-3.19388,
-3.17229,
-3.06048,
-3.00355,
-2.95577,
-2.91452,
-2.88286,
-2.85862,
-2.84105,
-2.82853,
-2.81985,
-2.79688,
-2.79173,
-2.79571,
-2.79772,
-2.7994
]
uccsd = [
-7.723418271,
-7.78435,
-7.82552,
-7.85247,
-7.86921,
-7.878445261,
-7.882352708,
-7.879421024,
-7.868223971,
-7.853438898,
-7.837968246,
-7.823663938,
-7.811635937,
-7.802323918
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

result = calculate(methods=['hf','fci','1-upccgsd','chem_acc'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax2.yaxis.set_label_position("left")
ax2.yaxis.tick_left()

ls, labels = plot_absolute(ax1, calculate(methods=['hf','fci','1-upccgsd']))
plot_relative(ax2, calculate(methods=['fci','1-upccgsd']))

ax1.set_title("H6 PES", loc='left')
ax2.set_title("H6 energy error", loc='left')

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

plt.savefig(image_path('H6.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig(image_path('H6.pdf'), bbox_extra_artists=(lgd,), bbox_inches='tight')

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