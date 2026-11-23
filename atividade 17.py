Extrator de E-mails e Telefones (Regex): Usando o módulo re, crie um script que leia
um texto longo e extraia todas as ocorrências válidas de endereços de e-mail e números
de telefone no formato: (XX) XXXXX-XXXX.

RESPOSTA:
import re

texto = "Contato: joao.silva@email.com ou pelo celular (62) 99876-5432. Suporte: dev@empresa.com.br"

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', texto)
telefones = re.findall(r'\(\d{2}\)\s\d{5}-\d{4}', texto)

print("E-mails:", emails)
print("Telefones:", telefones)
