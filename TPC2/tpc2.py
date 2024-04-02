import re




def conversor(texto):
    texto_convertido = re.sub(r'^\#\s+(.*)', r"<p><h1>\1</h1></p>", texto)
    texto_convertido = re.sub(r'^\#{2}\s+(.*)', r"<p><h2>\1</h2></p>", texto)
    texto_convertido = re.sub(r'^\#{3}\s+(.*)', r"<p><h3>\1</h3></p>", texto)
    texto_convertido = re.sub(r'\*{2}([^*]+)\*{2}', r"<p><b>\1</b></p>", texto)
    texto_convertido = re.sub(r'\*([^*]+)\*', r"<p><i>\1</i></p>", texto)
    texto_convertido = re.sub(r'^>\s+(.*)', r"<p><blockquote>\1</blockquote></p>", texto)
    texto_convertido = re.sub(r'^\d+\.\s+(.*)', r"<p><ol>\1</ol></p>", texto)
    texto_convertido = re.sub(r'^\-\s+(.*)', r"<p><ul>\1</ul></p>", texto)
    texto_convertido = re.sub(r'^`(.*)`$', r"<p><code>\1</code></p>", texto)
    texto_convertido = re.sub(r'^-{3}$', r"<p><hr></p>", texto)
    texto_convertido = re.sub(r'^\[(.*)\]\((.*)\)$', r"<p><a href='\2'>\1</a></p>", texto)
    texto_convertido = re.sub(r'^!\[(.*)\]\((.*)\)$', r"<p><img src='\2' alt='\1'></p>", texto)
    return texto_convertido

def converter_arquivo(input_file, output_file, conversor):
    # Abrir o arquivo de entrada para leitura
    with open(input_file, 'r') as input_f:
        # Ler o conteúdo do arquivo de entrada
        original_content = input_f.read()

    # Aplicar a função de conversão
    texto_html = conversor(original_content)

    # Escrever no arquivo de saída
    with open(output_file, 'w') as output_f:
        # Escrever o início no arquivo de saída
        output_f.write("<!DOCTYPE html><html><head><title>Page Title</title></head><body>\n")

        # Escrever o conteúdo convertido no arquivo de saída
        output_f.write(texto_html)

        # Escrever o final no arquivo de saída
        output_f.write("\n</body></html>")

# Nome dos arquivos de entrada e saída
arquivo_entrada = "input.txt"
arquivo_saida = "output.html"

# Chamar a função para converter o arquivo, passando a função de conversão como argumento
converter_arquivo(arquivo_entrada, arquivo_saida, conversor)

print("Conversão concluída. Verifique o arquivo de saída:", arquivo_saida)
