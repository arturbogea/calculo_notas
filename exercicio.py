# Lista de aprovados na faculdade.

print("""
    Bem-vindo(a) ao sistema de notas da faculdade.
""")


aprovados = []
recuperacao = []
reprovados = []

def calculo_nota(n1, n2):
    return (n1 + n2) / 2

def calculo_final(aluno, nota, num_faltas):


    if nota >= 7.0 and num_faltas < 15:
        aprovados.append(aluno)
        print(f"Parabéns! Você foi aprovado(a)! Aluno(a) {aluno} foi aprovada com nota final {nota:.2f} e teve {num_faltas} faltas.")
    
    elif 4.0 <= nota < 7 and num_faltas <= 15:
        recuperacao.append(aluno)
        print(f"Aluno(a) {aluno} foi em recuperação, com nota final {nota:.2f} e teve {num_faltas} faltas. Estude, você ainda tem mais uma chance") 
   
    elif num_faltas > 15:
            reprovados.append(aluno)
            print(f"Aluno(a) {aluno} está reprovado(a) por faltas. A sua nota final foi {nota:.2f}, mas infelizmente teve {num_faltas} faltas.")
    
    else:
         reprovados.append(aluno)
         print(f"Aluno(a) {aluno} está reprovado. Não desiste, foque nos seus sonhos, se esforce mais no semestre que vem. Não desiste, foque nos seus sonhos, se esforce mais no semestre que vem.")


incluir_aluno = "s"

while incluir_aluno == "s":

    nome = input("Informe o nome do aluno(a): ")
    nota1 = float(input("Informe a nota do 1º trimestre: "))
    nota2 = float(input("Informe a nota do 2º trimestre: "))
    faltas = int(input("Informe o numero de faltas que o aluno(a) teve no semestre: "))

    calc_nota = calculo_nota(n1=nota1, n2=nota2)
    
    calculo_final(nome, calc_nota, faltas)
    
    incluir_aluno = input("Deseja incluir outro aluno? s(sim) / n(não)").lower()

    if incluir_aluno != "s":
         break    


    
print(f"""
    lista de alunos aprovados {aprovados}\n
    lista de alunos em recuperação {recuperacao}\n
    lista de alunos reprovados {reprovados}
""")
