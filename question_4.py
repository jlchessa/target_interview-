# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros


pc_sp = round((sp / total) * 100, 2)
print("São Paulo : {}% das vendas totais da empresa".format(pc_sp))

pc_rj = round((rj / total) * 100, 2)
print("Rio de Janeiro : {}% das vendas totais da empresa".format(pc_rj))

pc_mg = round((mg / total) * 100, 2)
print("Minas Gerais: {}% das vendas totais da empresa".format(pc_mg))

pc_es = round((es / total) * 100, 2)
print("Espírito Santo: {}% das vendas totais da empresa".format(pc_es))

pc_outros = round((outros / total) * 100, 2)
print("Outros Estados: {}% das vendas totais da empresa".format(pc_outros))

