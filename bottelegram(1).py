import telebot

CHAVE_API = "6815919052:AAE7YoypiBfkEpWOvmhNRfRewjGUo-DdfzY"

bot = telebot.TeleBot(CHAVE_API)

#______________________________________________________________________________________________



#*******funcoes que tratam as opcoes inseridas pelo usuario********


#  subrotinas da funcao "fazer Orcamento  " 
#   funcionando perfeitamente

#opcao de programa contabil
@bot.message_handler(commands=["Programa"])
def Programa(mensagem):
    texto = """ Perfeito, te redirecionaremos para nossa equipe da area contabil"""
    bot.send_message(mensagem.chat.id, texto)

#opcao Automatizacao da orcamento
@bot.message_handler(commands=["Automatizacao"])
def Automatização(mensagem):
    texto = """ Te redirecionaremos para nossa equipe de Automaitzação, Aguarde"""
    bot.send_message(mensagem.chat.id, texto)

#Opcao Orcamento programa personalizado
@bot.message_handler(commands=["personalizado"])
def personalizado(mensagem):
    texto = """Entre em contato com nossa equipe para um Programa personalizado, Email: gianpablo500@gmail.com"""
    bot.send_message(mensagem.chat.id, texto)

#funcao sair padrao



#______________________________________________________________________________________________




#subrotinas da funcao "Suporte"

#opcao "problema1" da funcao suporte:
@bot.message_handler(commands=["Problema1"])
def problema1(mensagem):
    texto = """ Nossa equipe entrará em contato para saber melhor do que se trata o bug"""
    bot.send_message(mensagem.chat.id, texto)


#opcao "problema2" da funcao suporte:
@bot.message_handler(commands=["Problema2"])
def problema2(mensagem):
    texto ="Encaminharemos a nossa equipe responsavel pelo servidor, Aguarde!"
    bot.send_message(mensagem.chat.id, texto)

#opcao "problema3" da funcao suporte
@bot.message_handler(commands=["Problema3"])
def problema3(mensagem):
    texto ="Abriremos um chamado a nossa equipé para verificarmos o Hardware!"
    bot.send_message(mensagem.chat.id, texto)


#______________________________________________________________________________________________



     #Funcoes primarrias de atendimento
    
#opcao 1 / Orçamentos e suas opcoes
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """Selecione a opcao desejada
    /Programa contabil
    /Automatizacao de Residencias ou Empresas
    /personalizado
    /retornar
    """
    bot.send_message(mensagem.chat.id, texto)


#opção 2 suporte e suas opcoes
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """ Qual das opções se encaixa melhor no problema: 
    /Problema1 Bugs e erros no sistema
    /Problema2 Sistema fora do ar
    /Problema3 Hardware danificado (aplicado somente em Automatização)
    /retornar"""
    
    bot.reply_to(mensagem, texto)


#opcao 3 e suas opcoes
#opcao consultoria
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id,"Agendaremos sua consultoria em breve")

@bot.message_handler(commands=["opcao4"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Tudo bem, se precisar de algo e so chamar :)")



#______________________________________________________________________________________________


#Funcao que responde qualquer mensagem de incio rapidamente
#*********mensagem padrao*********
    
def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """ 
    Escolha uma opção para continuar seu atendimento
     /opcao1 Fazer um orçamento
     /opcao2 Suporte
     /opcao3 Consultoria
     /opcao4 fechar atendimento
     Selecione uma das opções """
    bot.reply_to(mensagem, texto)

bot.polling()

