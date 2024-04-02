import re

def somador(file_path):
    sum = 0
    active = True

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() == "OFF":
                    active = False
                    print("Processing turned off.")
                elif word.lower() == "ON":
                    active = True
                    print("Processing turned on.")
                elif active and re.match(r'\d+', word):
                    sum += int(word)
                elif re.match(r'=',word):
                    print("The sum is:", sum)

    return sum

file_path = "texto.txt"  # Replace with your file path
soma = somador(file_path)
print("Somatorio dos numeros é:", soma)