import matplotlib.pyplot as plt
print("="*40)
print('不确定性推理:主观贝叶斯')
print('E:前提,H:结论,C(E/S):可信度')
print("="*40)
print('定义域:')
print('\t{-5 <= C(E/S) <= 5}')
print('\t{0 <= P(H),P(E) <= 1}')
print('\t{LS,LN >= 0 LS,LN位于1两侧}')
print("="*40)
PH = float(input('请输入先验概率P(H):'))
PE = float(input('请输入先验概率P(E):'))
LS = float(input('请输入充分性度量LS:'))
LN = float(input('请输入必要性度量LN:'))

CES_SET = []
PHS_SET = []
i = -5
while i <= 5:
    CES_SET.append(i)
    i += 0.1

for CES in CES_SET:
    PEH = LS * (1 - LN) / (LS - LN)
    P_EH = 1 - PEH
    PH_E = P_EH * PH / (1 - PE)
    if PH_E > 1:
        PH_E = 1

    PHE = PEH * PH / PE
    if PHE > 1:
        PHE = 1

    if CES <= 0:
        PHS_SET.append(PH_E + (PH - PH_E) * (CES / 5 + 1))
    else:
        PHS_SET.append(PH + (PHE - PH) * CES / 5)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('P(H/S)-C(E/S)')
plt.plot(CES_SET, PHS_SET)
plt.show()
