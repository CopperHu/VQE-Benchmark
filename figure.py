import matplotlib.pyplot as plt
import numpy as np
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
current_path = os.path.abspath(os.path.dirname(__file__))
IMAGE_PATH = os.path.join(current_path, 'images')

bond_length = [0.9,
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
2
]
hf = [-7.705753340141292, -7.76736213574856, -7.808743176493412, -7.835615825556919, -7.851953857958783, -7.860538661021181, -7.863357621535116, -7.861864769808649, -7.857144960203826, -7.850018697166804, -7.841112040771398, -7.830905584637069]
fci = [-7.722097692292443, -7.78332880596055, -7.824535779909315, -7.851524884456745, -7.868309219685463, -7.877685604559943, -7.881648229705644, -7.8816576024362055, -7.878808473158973, -7.873935934402737, -7.867685392276789, -7.860561269346807]
one_upccgsd = [-7.72299,
-7.78415,
-7.82532,
-7.85227,
-7.86901,
-7.87834,
-7.88225,
-7.879421024,
-7.86811,
-7.85331,
-7.83784,
-7.82353,
-7.81152,
-7.80234
]
uccsd = [
-7.723361108,
-7.784413774,
-7.825502785,
-7.852405586,
-7.869120584,
-7.878435734,
-7.882347327,
-7.882135215,
-7.878735274,
-7.874498676,
-7.867184801,
-7.858505643
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

ax1.set_title("LiH PES", loc='left')
ax2.set_title("LiH energy error", loc='left')

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

plt.savefig(image_path('LiH.png'), bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig(image_path('LiH.pdf'), bbox_extra_artists=(lgd,), bbox_inches='tight')

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