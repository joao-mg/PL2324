import os
import sys


teste = {}

def parser(file_path):               # Parser: função que lê um ficheiro CSV e guarda as informações num dicionário
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.strip().split(',')
            teste[line[0]] = tuple(line[1:])
            
def ordered_modalidades():  #Ponto 1:Lista ordenada alfabeticamente das modalidades desportivas;
    modalidades = sorted(set(teste[id][7] for id in teste))
    return modalidades

def percentagemvalido(): #Ponto 2:Percentagens de atletas aptos e inaptos para a prática desportiva;
    valid = sum(1 for id in teste if teste[id][11] == 'true')
    total = len(teste)
    return (valid / total) * 100 if total > 0 else 0

def athletes_age_group(): #Ponto 3: Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39].
    age_groups = {i: 0 for i in range(0, 101, 5)}
    for id in teste:
        age = int(teste[id][4])
        age_group = min(range(0, 101, 5), key=lambda x: abs(x - age))
        age_groups[age_group] += 1
    return age_groups

def print_athletes_age_group():
    for age, count in athletes_age_group().items():
        print(f'{age}-{age+4}: {count}')
        
        

parser(r'C:\Users\USER\Desktop\Uni\PL\PL2324\TPC1\emd.csv')
print(ordered_modalidades())
validPercentage = percentagemvalido()
invalidPercentage = 100 - validPercentage
print(f'Valid: {validPercentage}%')
print(f'Invalid: {invalidPercentage}%')
print_athletes_age_group()