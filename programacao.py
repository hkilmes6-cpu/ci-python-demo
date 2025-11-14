import pandas as pd

dados_praia = {
    'praia': ['Praia do Sancho', 'Praia do Rosa', 'Praia dos Carneiros', 'Praia do Espelho'],
    'cidade': ['Fernando de Noronha', 'Imbituba', 'Tamandaré', 'Trancoso'],
    'estado': ['PE', 'SC', 'PE', 'BA'],
    'avaliacao': [4.9, 4.8, 4.7, 4.8]
}

df_praia = pd.DataFrame(dados_praia)

df_praia.to_csv('praia.csv', index=False)
print("Arquivo 'praia.csv' salvo com sucesso (sem índice).")

df_praia.to_csv('praia_br.csv', sep=';')
print("Arquivo 'praia_br.csv' salvo com sucesso (separado por ';').")

df_praia.to_csv('praias_lindas.csv', encoding='latin1')
print("Arquivo 'praias_lindas.csv' salvo com sucesso (encoding 'latin1').")
