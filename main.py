import pandas as pd
import os

def cruzar_dados_csvs():
    """
    Faz o cruzamento dos dados entre produtos_fornecedor_vendor_dev.csv e produtos.csv
    para preencher corretamente a coluna produtos_id
    """
    
    print("Iniciando o cruzamento de dados...")
    
    # Verificar se os arquivos existem
    arquivo_fornecedor = "produtos_fornecedor_vendor_prod.csv"
    arquivo_produtos = "produtos.csv"
    
    if not os.path.exists(arquivo_fornecedor):
        print(f"Erro: Arquivo {arquivo_fornecedor} não encontrado!")
        return
    
    if not os.path.exists(arquivo_produtos):
        print(f"Erro: Arquivo {arquivo_produtos} não encontrado!")
        return
    
    try:
        # Ler o arquivo produtos.csv (delimitador ;)
        print("Lendo arquivo produtos.csv...")
        df_produtos = pd.read_csv(arquivo_produtos, delimiter=';', encoding='utf-8')
        print(f"Produtos carregados: {len(df_produtos)} registros")
        
        # Ler o arquivo produtos_fornecedor_vendor_dev.csv (delimitador ,)
        print("Lendo arquivo produtos_fornecedor_vendor_dev.csv...")
        df_fornecedor = pd.read_csv(arquivo_fornecedor, delimiter=',', encoding='utf-8')
        print(f"Fornecedores carregados: {len(df_fornecedor)} registros")
        
        # Criar mapeamento produtos_vendor_id -> id do arquivo produtos
        print("Criando mapeamento de produtos...")
        # Remove linhas com valores vazios ou nulos antes de criar o mapeamento
        df_produtos_limpo = df_produtos.dropna(subset=['produtos_vendor_id', 'id'])
        df_produtos_limpo = df_produtos_limpo[df_produtos_limpo['produtos_vendor_id'] != '']
        
        mapeamento_produtos = dict(zip(df_produtos_limpo['produtos_vendor_id'], df_produtos_limpo['id']))
        print(f"Mapeamento criado com {len(mapeamento_produtos)} produtos únicos")
        
        # Fazer o cruzamento - preencher produtos_id baseado no produtos_vendor_id
        print("Fazendo o cruzamento dos dados...")
        df_resultado = df_fornecedor.copy()
        
        # Mapear produtos_id usando o mapeamento criado
        df_resultado['produtos_id'] = df_resultado['produtos_vendor_id'].map(mapeamento_produtos)
        
        # Verificar quantos registros foram mapeados com sucesso
        mapeados = df_resultado['produtos_id'].notna().sum()
        nao_mapeados = df_resultado['produtos_id'].isna().sum()
        
        print(f"Registros mapeados com sucesso: {mapeados}")
        print(f"Registros não mapeados: {nao_mapeados}")
        
        # Preencher valores não mapeados com 0 (manter o padrão original)
        df_resultado['produtos_id'] = df_resultado['produtos_id'].fillna(0).astype(int)
        
        # Salvar o resultado em um novo arquivo
        arquivo_saida = "produtos_fornecedor_vendor_atualizado.csv"
        print(f"Salvando resultado em {arquivo_saida}...")
        
        df_resultado.to_csv(arquivo_saida, index=False, encoding='utf-8')
        
        print("✅ Cruzamento concluído com sucesso!")
        print(f"📄 Arquivo gerado: {arquivo_saida}")
        print(f"📊 Total de registros: {len(df_resultado)}")
        print(f"✅ Produtos mapeados: {mapeados}")
        print(f"❌ Produtos não mapeados: {nao_mapeados}")
        
        # Mostrar alguns exemplos dos dados resultantes
        print("\n📋 Primeiras 5 linhas do resultado:")
        print(df_resultado.head().to_string(index=False))
        
        return df_resultado
        
    except Exception as e:
        print(f"❌ Erro durante o processamento: {str(e)}")
        return None

if __name__ == "__main__":
    resultado = cruzar_dados_csvs()
