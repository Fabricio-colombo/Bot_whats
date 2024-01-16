'''
BOT de aquecimento de WhatsApp - A ideia é deixar 2 whats conversando de forma aleatoria para aquecer o numero e não ser banido.
Se sentir que o bot está muito rapido ou lento, basta modificar o tempo de espera entre as mensagens com o time.sleep()
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import openpyxl

# Configurando o serviço do Chrome
servico = Service(ChromeDriverManager().install())

# Configurando opções para abrir uma aba anônima
opcoes_anonimas = Options()
opcoes_anonimas.add_argument('--incognito')

# Criando instâncias do driver para a janela normal e janela anônima
navegador = webdriver.Chrome(service=servico)
navegador_anonimo = webdriver.Chrome(service=servico, options=opcoes_anonimas)

# Abrindo o navegador normal
navegador.get('https://web.whatsapp.com/')
time.sleep(5)  # Aumentando o tempo para garantir que o usuário tenha tempo de fazer login

# Abrindo a página inicial do WhatsApp Web na janela anônima
navegador_anonimo.get('https://web.whatsapp.com/')
time.sleep(15)  # Aumentando o tempo para garantir que o usuário tenha tempo de fazer login

# Esperando até que o campo de pesquisa esteja disponível na janela normal
campo_pesquisa_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, campo_pesquisa_xpath)))

# Esperando até que o campo de pesquisa esteja disponível na janela anônima
campo_pesquisa_xpath_anonimo = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
WebDriverWait(navegador_anonimo, 60).until(EC.presence_of_element_located((By.XPATH, campo_pesquisa_xpath_anonimo)))

# Abrindo a planilha com openpyxl
planilha = openpyxl.load_workbook('bot_numeros.xlsx')

# Detectando automaticamente o nome da folha
nome_folha = planilha.active.title

# Criando a lista de mensagens
lista_mensagens = [
    'Olá, tudo bem?',
    'Como vai?',
    'Estou entrando em contato para te mostrar uma coisa',
    'O produto é muito bom... falta só tudo',
    'Estou enviando o link do produto...',
    'Se tiver alguma dúvida...não fale cmg kkkk',
    'ai é com o suporte',
    'abraços',
    'pode creeee',
    'kk',
    'foi ela que fez isso por mim',
    'vamo jogar então?',
    'calculadora de eleição tlgd?',
    'tu é mais feio que bate em mãe',
    'agora vou te falar uma parada, o cabeça de serrote é o mais feio',
    'A vida é feita de escolhas',
    'Nunca desista dos seus sonhos',
    'Aproveite cada momento',
    'A simplicidade é a chave da felicidade',
    'Viva intensamente',
    'Acredite em você mesmo',
    'Nada é impossível',
    'Seja a mudança que você quer ver no mundo',
    'O sucesso é a soma de pequenos esforços repetidos dia após dia',
    'A paciência é amarga, mas seus frutos são doces',
    'Sorria, você está sendo observado',
    'O importante não é vencer todos os dias, mas lutar sempre',
    'A melhor maneira de prever o futuro é criá-lo',
    'Amar é encontrar na felicidade de outrem a própria felicidade',
    'A vida é curta, aproveite cada momento',
    'Não espere por uma crise para descobrir o que é importante em sua vida',
    'Faça mais coisas que te fazem feliz',
    'Nunca é tarde demais para ser quem você poderia ter sido',
    'O sucesso nasce do querer, da determinação e persistência',
    'A verdadeira amizade é como a saúde; seu valor é raramente reconhecido até que seja perdido',
    'Não espere por pessoas extraordinárias. Seja você a extraordinária',
    'O amor é a força mais sutil do mundo',
    'A felicidade está nas pequenas coisas',
    'Seja grato por hoje, porque amanhã tudo pode mudar',
    'A vida é como andar de bicicleta. Para manter o equilíbrio, você deve continuar em movimento',
    'A mente é tudo. Você se torna aquilo que pensa',
    'Nada é permanente, exceto a mudança',
    'Cada dia é uma nova chance de ser melhor que ontem',
    'A sorte favorece a mente preparada',
    'A jornada de mil milhas começa com um único passo',
    'A vida é uma aventura ousada ou nada',
    'A simplicidade é a última sofisticação',
    'A beleza está nos olhos de quem vê',
    'Siga seu coração, mas leve seu cérebro junto',
    'A gratidão é a chave para a felicidade',
    'A educação é a arma mais poderosa que você pode usar para mudar o mundo',
    'O que não te desafia, não te faz mudar',
    'A imaginação é mais importante que o conhecimento',
    'O sucesso não é a chave para a felicidade. A felicidade é a chave para o sucesso',
    'Seja a mudança que você deseja ver no mundo',
    'Nunca é tarde demais para ser o que você poderia ter sido',
    'O amor não tem idade, não tem limites e não tem fim',
    'A vida é 10 o que acontece conosco e 90 como reagimos a isso',
    'O maior prazer na vida é fazer aquilo que as pessoas dizem que você não pode fazer',
    'Seja a mudança que você deseja ver no mundo',
    'O importante não é vencer todos os dias, mas lutar sempre',
    'A vida é feita de escolhas',
    'O sucesso é a soma de pequenos esforços repetidos dia após dia',
    'Nunca desista dos seus sonhos',
    'A paciência é amarga, mas seus frutos são doces',
    'Sorria, você está sendo observado',
    'O sucesso nasce do querer, da determinação e persistência',
    'A verdadeira amizade é como a saúde; seu valor é raramente reconhecido até que seja perdido',
    'Não espere por pessoas extraordinárias. Seja você a extraordinária',
    'A vida é como andar de bicicleta. Para manter o equilíbrio, você deve continuar em movimento',
    'A mente é tudo. Você se torna aquilo que pensa',
    'Nada é permanente, exceto a mudança',
    'Cada dia é uma nova chance de ser melhor que ontem',
    'A sorte favorece a mente preparada',
    'A jornada de mil milhas começa com um único passo',
    'A vida é uma aventura ousada ou nada',
    'A simplicidade é a última sofisticação',
    'A beleza está nos olhos de quem vê',
    'Siga seu coração, mas leve seu cérebro junto',
    'A gratidão é a chave para a felicidade',
    'A educação é a arma mais poderosa que você pode usar para mudar o mundo',
    'O que não te desafia, não te faz mudar',
    'A imaginação é mais importante que o conhecimento',
    'O sucesso não é a chave para a felicidade. A felicidade é a chave para o sucesso',
    'Seja a mudança que você deseja ver no mundo',
    'Nunca é tarde demais para ser o que você poderia ter sido',
    'O amor não tem idade, não tem limites e não tem fim',
    'A vida é 10 o que acontece conosco e 90 como reagimos a isso',
    'O maior prazer na vida é fazer aquilo que as pessoas dizem que você não pode fazer',
    'bora jogar um tibia entones kkkkk',
    'tu é mais feio que bate em mãe',
    'tiririca te passou a perna',
]


# Loop infinito
while True:
    # Lendo a planilha com openpyxl
    for linha in planilha[nome_folha]:
        if linha[0].value is not None:
            nome = linha[0].value
            numero = str(linha[0].value)  # Convertendo para string diretamente

            # Esperando até que o campo de pesquisa esteja disponível na janela normal
            WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.XPATH, campo_pesquisa_xpath)))

            # Abrindo a conversa com o cliente na janela normal
            campo_pesquisa = navegador.find_element(By.XPATH, campo_pesquisa_xpath)
            campo_pesquisa.click()
            campo_pesquisa.send_keys(numero)
            campo_pesquisa.send_keys(Keys.RETURN)  # Pressiona Enter para iniciar a conversa
            time.sleep(5)  # Tempo adicional para garantir que a conversa esteja carregada

            # Atualizando o campo de mensagem XPath na janela normal
            campo_mensagem_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

            # Esperando até que o campo de mensagem esteja clicável na janela normal
            campo_mensagem = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, campo_mensagem_xpath)))

            # Clicando no campo de digitação na janela normal
            campo_mensagem.click()
            time.sleep(2)

            # Escolhendo a mensagem aleatória
            mensagem = random.choice(lista_mensagens)

            while True:
                try:
                    # Atualizando o campo de mensagem XPath após clicar na janela normal
                    campo_mensagem = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, campo_mensagem_xpath)))

                    # Digitando a mensagem na janela normal
                    campo_mensagem.send_keys(mensagem)
                    time.sleep(1)

                    # Enviando a mensagem pressionando Enter na janela normal
                    campo_mensagem.send_keys(Keys.RETURN)
                    break  # Saindo do loop se a mensagem for enviada com sucesso
                except Exception as e:
                    print(f"Erro ao enviar mensagem na janela normal: {e}")
                    time.sleep(2)  # Aguardando 2 segundos antes de tentar novamente

                time.sleep(10)  # Tempo adicional após o envio da mensagem na janela normal

            # Esperando até que o campo de pesquisa esteja disponível na janela anônima
            campo_pesquisa_xpath_anonimo = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
            WebDriverWait(navegador_anonimo, 60).until(EC.presence_of_element_located((By.XPATH, campo_pesquisa_xpath_anonimo)))

            # Abrindo a conversa com o cliente na janela anônima
            campo_pesquisa_anonimo = navegador_anonimo.find_element(By.XPATH, campo_pesquisa_xpath_anonimo)
            campo_pesquisa_anonimo.click()
            campo_pesquisa_anonimo.send_keys(numero)
            campo_pesquisa_anonimo.send_keys(Keys.RETURN)  # Pressiona Enter para iniciar a conversa
            time.sleep(5)  # Tempo adicional para garantir que a conversa esteja carregada

            # Atualizando o campo de mensagem XPath na janela anônima
            campo_mensagem_xpath_anonimo = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

            # Esperando até que o campo de mensagem esteja clicável na janela anônima
            campo_mensagem_anonimo = WebDriverWait(navegador_anonimo, 20).until(EC.element_to_be_clickable((By.XPATH, campo_mensagem_xpath_anonimo)))

            # Clicando no campo de digitação na janela anônima
            campo_mensagem_anonimo.click()
            time.sleep(2)

            # Escolhendo a mensagem aleatória
            mensagem_anonima = random.choice(lista_mensagens)

            while True:
                try:
                    # Atualizando o campo de mensagem XPath após clicar na janela anônima
                    campo_mensagem_anonimo = WebDriverWait(navegador_anonimo, 20).until(EC.element_to_be_clickable((By.XPATH, campo_mensagem_xpath_anonimo)))

                    # Digitando a mensagem na janela anônima
                    campo_mensagem_anonimo.send_keys(mensagem_anonima)
                    time.sleep(1)

                    # Enviando a mensagem pressionando Enter na janela anônima
                    campo_mensagem_anonimo.send_keys(Keys.RETURN)
                    break  # Saindo do loop se a mensagem for enviada com sucesso
                except Exception as e:
                    print(f"Erro ao enviar mensagem na janela anônima: {e}")
                    time.sleep(2)  # Aguardando 2 segundos antes de tentar novamente

                time.sleep(10)  # Tempo adicional após o envio da mensagem na janela anônima
