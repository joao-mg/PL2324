import re

def somador(file_path):
    sum = 0
    active = True

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if re.fullmatch(r'off', word, re.IGNORECASE):
                    active = False
                    print("Processing turned off.")
                elif re.fullmatch(r'on', word, re.IGNORECASE):
                    active = True
                    print("Processing turned on.")
                elif active and re.match(r'\d+', word):
                    sum += int(word)
                elif re.match(r'=',word):
                    print("The sum is:", sum)

    return sum

file_path = r"C:\Users\USER\Desktop\Uni\PL\PL2324\TPC3\teste.txt"
soma = somador(file_path)
print("Somatorio dos numeros é:", soma)