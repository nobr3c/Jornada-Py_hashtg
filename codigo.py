# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui --no terminal
import pyautogui
import time


# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
    #aperta a tecla do windows(command + barra de espaço)
pyautogui.press("win")
    #digita o nome do programa (chrome)
pyautogui.write("chrome ")
    # aperta enter
pyautogui.press("enter")

    # entrar no link 
        # com variavel
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.write(link)
        # sem variavel
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

    # aperta o enter
pyautogui.press("enter")

    # Esperar 5 segundos
time.sleep(5)

# Passo 2: Fazer login    
    # selecionar o campo de email
pyautogui.click(x=685, y=451)

    # digitar o e-mail
pyautogui.write("pythonimpressionador@gmail.com")
    
    # passando pro próximo campo, o campo da senha
pyautogui.press("tab") 

    # Digitar senha
pyautogui.write("sua senha")

    # clique no botao de login
pyautogui.click(x=955, y=638) 

time.sleep(3)



# Passo 3: Importar a base de produtos pra cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim