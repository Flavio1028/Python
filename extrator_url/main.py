from extrator_url import ExtratorUrl

url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

extrator_url = ExtratorUrl(url)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)

valor = extrator_url.get_valor_parametro("quantidade")
print(valor)

