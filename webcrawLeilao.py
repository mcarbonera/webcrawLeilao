import requests
from bs4 import BeautifulSoup
import json

# Associação Brasileira dos Criadores de Zebuínos
siteABCZ = 'https://www.abcz.org.br/'
# Consulta de Animais: 
consultaAnimais = 'produtos-e-servicos/consulta-publica-de-animais'

# eRural
siteERural = 'https://www.erural.net/'
# Consulta de Leilões: 
consultaLeiloes = 'agenda_leiloes'

# consultar site de leiloes:
pagLeiloes = requests.get(siteERural+consultaLeiloes)
html_page = pagLeiloes.content
soupERural = BeautifulSoup(html_page, "html.parser")

# A partir das tags html:
#soupERural.select('div > div.inner-wrap > div.crawled-auction-page > crawled-auction-content-featured')[0]

# Pelo filtro da API:
urlConsultaLeiloesBovinos = 'https://www.erural.net/agenda_leiloes/filtrar?&page=1&breeds[]=Brahman&breeds[]=Nelore&breeds[]=Senepol&breeds[]=Tabapu%C3%A3&breeds[]=Angus&breeds[]=Brangus&breeds[]=Guzer%C3%A1&categories[]=bovine'
leiloesFiltradosBovinos = requests.get(urlConsultaLeiloesBovinos).content.decode('UTF-8')
listaLeiloesPorMes = json.loads(leiloesFiltradosBovinos)

leiloes = listaLeiloesPorMes.values()

listaLeiloes = []
for value in listaLeiloesPorMes.values():
    for item in value:
        listaLeiloes.append(item)
    
# Filtrar pelos leilões que não são virtuais:
def isNotVirtual(leilao):
    return not leilao['is_virtual']
    
leiloesPresenciais = list(filter(isNotVirtual, listaLeiloes))

print('Qtd de leilões: ' + str(len(listaLeiloes)))
print('Leilões presenciais: ' + str(len(leiloesPresenciais)))
