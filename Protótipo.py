# Definição dos alimentos
Food = "01. Salgado" 
Food2 = "02. Twix"
Food3 = "03. Paçoca"
Food4 = "04. Bolo de pote"
Food5 = "05. Bala"
Food6 = "06. Pão de queijo"
Food7 = "07. Freegells"
Food8 = "08. Salgadinho"
Food9 = "09. Barrinha de cereal"

# Definição dos sabores de salgado
Salgado1 = '1. Frango com catupiry'
Salgado2 = '2. Mortadela e queijo'
Salgado3 = '3. Pizza'
Salgado4 = '4. Queijo'
Salgado5 = '5. Hamburger'

# Definição dos sabores de bala
Bala1 = '1. Iogurte'
Bala2 = '2. Cereja'
Bala3 = '3. Azedinho'

# Definição dos sabores de bolo
Bolo1 = '1. Ninho com Nutella'
Bolo2 = '2. Brigadeiro'
Bolo3 = '3. Prestígio'
Bolo4 = '4. Cenoura'
Bolo5 = '5. Café'

# Definição dos sabores de salgadinho
Salgadinho1 = '1. Cebola'
Salgadinho2 = '2. Churrasco'

# Definição dos sabores de Freegells
Freegells1 = '1. Melancia'
Freegells2 = '2. Menta'
Freegells3 = '3. Morango'

# Definição das bebidas
Bebida1 = '1. Guaraná'
Bebida2 = '2. Coca-cola'
Bebida3 = '3. Suco de Laranja'
Bebida4 = '4. Suco de Morango'

# Seleção do alimento pelo usuário
Cantinafood = input(f'Insira o número do alimento que deseja comprar \n{Food} \n{Food2} \n{Food3} \n{Food4} \n{Food5} \n{Food6} \n{Food7} \n{Food8} \n{Food9}\nDigite aqui: ')

# Verificação da seleção e ações correspondentes
if Cantinafood == '01':
    Salgado = input(f'Qual o sabor do salgado? \n{Salgado1} \n{Salgado2} \n{Salgado3} \n{Salgado4} \n{Salgado5} \nDigite aqui: ')
    if Salgado in ['1', '2', '3', '4', '5']:
        print('Está reservado')
    else:
        print('Não temos mais sabores')

elif Cantinafood == '02':
    print('Seu Twix está reservado')

elif Cantinafood == '03':
    print('Sua paçoca está reservada')

elif Cantinafood == '04':
    Pote = input(f'Qual o sabor do bolo? \n{Bolo1} \n{Bolo2} \n{Bolo3} \n{Bolo4} \n{Bolo5}\nDigite aqui: ')
    if Pote in ['1', '2', '3', '4', '5']:
        print('Está reservado')
    else:
        print('Não temos esse sabor')

elif Cantinafood == '05':
    Bala = input(f'Qual o sabor da bala? \n{Bala1} \n{Bala2} \n{Bala3} \nDigite aqui: ')
    if Bala in ['1', '2', '3']:
        print('Está reservado')
    else:
        print('Não temos esse sabor')

elif Cantinafood == '06':
    print('Seu Pão de Queijo está reservado')

elif Cantinafood == '07':
    Freegells = input(f'Qual o sabor do Freegells? \n{Freegells1} \n{Freegells2} \n{Freegells3} \nDigite aqui: ')
    if Freegells in ['1', '2', '3']:
        print('Está reservado')
    else:
        print('Não temos esse sabor')

elif Cantinafood == '08':
    Salgadinho = input(f'Qual o sabor do salgadinho? \n{Salgadinho1} \n{Salgadinho2} \nDigite aqui: ')
    if Salgadinho in ['1', '2']:
        print('Está reservado')
    else:
        print('Não temos esse sabor')

elif Cantinafood == '09':
    print('Sua Barrinha de cereal está reservada')

else:
    print('Opção inválida')
