salario_base = float(input("digite seu salário"))
horas_extras = float(input("digite o quanto de horas extras"))
valor_por_hora_extra = float(input("digite o valor da hora extra"))
salario_total=salario_base + (horas_extras*valor_por_hora_extra)
print(f"seu salario é:{salario_total}")