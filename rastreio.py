from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Pode-se remover o input e atribuir-se valor diretamente ao rastreio;
rastreio = input('Para inserir mais de um código separe os códigos por ponto e vírgula (ex: QH123456789BR;QH987654321BR)'
                 '\nAgora por favor digite o código(s) para o(s) rastreio(s)')

# Usado para alterar o local de instalação do Google Chrome; pode ser removido.
options = Options()
options.binary_location = "D:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
navegador = webdriver.Chrome(options=options, executable_path=r"d:\documentos\python\chromedriver.exe")

url = 'https://rastreamento.correios.com.br/app/index.php'
codigo = '//*[@id="objeto"]'
pesquisar = '//*[@id="b-pesquisar"]'
encontrar = '/html/body/main/div[1]/form/div[2]/div/div/div[3]'

def procurarpedidos(numero):
    navegador.get(url)

    navegador.find_element_by_xpath(codigo).click()
    navegador.find_element_by_xpath(codigo).send_keys(numero)
    navegador.find_element_by_xpath(pesquisar).click()

    encontrado = navegador.find_element_by_xpath(encontrar).get_attribute('innerHTML')

    if encontrado:
        navegador.close()
        print(f'O código "{numero}" não foi encontrado.\nOu o número está incorreto, ou o objeto ainda não foi postado.')


procurarpedidos(rastreio)
