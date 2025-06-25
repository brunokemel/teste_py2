from main import opendocx, getdocumenttext

# Caminho do arquivo .docx nos Downloads
caminho = r"C:\Users\Bruno\Downloads\Artigo_Desmatamento_Amazonia_Adria.docx"

doc = opendocx(caminho)
texto = getdocumenttext(doc)

print("Conteúdo do arquivo Word:")
for paragrafo in texto:
    print(paragrafo)
