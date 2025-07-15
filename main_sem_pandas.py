import csv
import os

def cruzar_dados_csvs_sem_pandas():
    """
    Faz o cruzamento dos dados entre produtos_fornecedor_vendor_dev.csv e produtos.csv
    para preencher corretamente a coluna produtos_id
    
    Esta versão usa apenas bibliotecas padrão do Python (sem pandas)
    """
    
    print("Iniciando o cruzamento de dados (versão sem pandas)...")
    
    # Verificar se os arquivos existem
    arquivo_fornecedor = "produtos_fornecedor_vendor_dev.csv"
    arquivo_produtos = "produtos.csv"
    
    if not os.path.exists(arquivo_fornecedor):
        print(f"Erro: Arquivo {arquivo_fornecedor} não encontrado!")
        return
    
    if not os.path.exists(arquivo_produtos):
        print(f"Erro: Arquivo {arquivo_produtos} não encontrado!")
        return
    
    try:
        # Ler o arquivo produtos.csv para criar o mapeamento
        print("Lendo arquivo produtos.csv...")
        mapeamento_produtos = {}
        total_produtos = 0
        
        with open(arquivo_produtos, 'r', encoding='utf-8', newline='') as arquivo:
            reader = csv.DictReader(arquivo, delimiter=';')
            for linha in reader:
                produtos_vendor_id = linha['produtos_vendor_id'].strip()
                produto_id = linha['id'].strip()
                
                # Só mapear se os valores não estiverem vazios
                if produtos_vendor_id and produto_id and produtos_vendor_id != '' and produto_id != '':
                    mapeamento_produtos[produtos_vendor_id] = produto_id
                total_produtos += 1
        
        print(f"Produtos carregados: {total_produtos} registros")
        print(f"Mapeamento criado com {len(mapeamento_produtos)} produtos únicos")
        
        # Processar o arquivo fornecedor e gerar o resultado
        print("Processando arquivo produtos_fornecedor_vendor_dev.csv...")
        arquivo_saida = "produtos_fornecedor_vendor_atualizado.csv"
        
        mapeados = 0
        nao_mapeados = 0
        total_registros = 0
        
        with open(arquivo_fornecedor, 'r', encoding='utf-8', newline='') as entrada, \
             open(arquivo_saida, 'w', encoding='utf-8', newline='') as saida:
            
            reader = csv.DictReader(entrada, delimiter=',')
            
            # Preparar o writer com as mesmas colunas
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(saida, fieldnames=fieldnames)
            writer.writeheader()
            
            # Processar cada linha
            for linha in reader:
                produtos_vendor_id = linha['produtos_vendor_id'].strip()
                
                # Fazer o mapeamento: usar produtos_vendor_id para buscar o id correspondente
                if produtos_vendor_id in mapeamento_produtos:
                    linha['produtos_id'] = mapeamento_produtos[produtos_vendor_id]
                    mapeados += 1
                else:
                    linha['produtos_id'] = '0'  # Manter padrão original
                    nao_mapeados += 1
                
                writer.writerow(linha)
                total_registros += 1
        
        print("✅ Cruzamento concluído com sucesso!")
        print(f"📄 Arquivo gerado: {arquivo_saida}")
        print(f"📊 Total de registros: {total_registros}")
        print(f"✅ Produtos mapeados: {mapeados}")
        print(f"❌ Produtos não mapeados: {nao_mapeados}")
        
        # Mostrar algumas linhas do resultado
        print("\n📋 Primeiras 5 linhas do resultado:")
        with open(arquivo_saida, 'r', encoding='utf-8') as arquivo:
            for i, linha in enumerate(arquivo):
                if i < 6:  # Header + 5 linhas
                    print(linha.strip())
                else:
                    break
        
        print(f"\n💯 Taxa de sucesso: {(mapeados/total_registros)*100:.1f}%")
        
    except Exception as e:
        print(f"❌ Erro durante o processamento: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    cruzar_dados_csvs_sem_pandas() 