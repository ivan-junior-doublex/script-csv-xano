# Script de Cruzamento de Dados - Produtos e Fornecedores

Este script faz o cruzamento de dados entre dois arquivos CSV para atualizar a coluna `produtos_id` com base na relação `produtos_vendor_id`.

## Arquivos Necessários

1. **produtos_fornecedor_vendor_dev.csv** - Arquivo principal com as colunas:

   - `id`
   - `created_at`
   - `produtos_vendor_id`
   - `fornecedor_id`
   - `produtos_id` (será preenchida pelo script)

2. **produtos.csv** - Arquivo de referência com as colunas:
   - `id`
   - `produtos_vendor_id`
   - `nome_padronizado`
   - **Importante:** Delimitador é ";" (ponto e vírgula)

## Como Executar

### Opção 1: Executar com Python diretamente

**Versão com pandas (recomendada - mais rápida):**

1. Certifique-se de que o Python está instalado
2. Instale a dependência pandas:
   ```bash
   pip install pandas
   ```
3. Execute o script:
   ```bash
   python main.py
   ```

**Versão sem pandas (usa apenas bibliotecas padrão):**

1. Certifique-se de que o Python está instalado
2. Execute o script alternativo:
   ```bash
   python main_sem_pandas.py
   ```

### Opção 2: Usar o arquivo batch (Windows)

1. Dê duplo clique no arquivo `executar.bat`
2. O script verificará se o Python está instalado
3. Você poderá escolher entre:
   - Versão com pandas (mais rápida, mas requer instalação)
   - Versão sem pandas (usa apenas bibliotecas padrão do Python)
4. Executará o cruzamento de dados

## O que o Script Faz

1. **Lê os dois arquivos CSV** respeitando os delimitadores corretos
2. **Cria um mapeamento** `produtos_vendor_id` → `id` do arquivo produtos.csv
3. **Faz o cruzamento** preenchendo a coluna `produtos_id` no arquivo principal
4. **Gera um novo arquivo** `produtos_fornecedor_vendor_atualizado.csv` com os dados atualizados
5. **Mostra estatísticas** sobre quantos registros foram mapeados com sucesso

## Resultado

O script gera um arquivo chamado `produtos_fornecedor_vendor_atualizado.csv` com:

- Todas as colunas originais do arquivo `produtos_fornecedor_vendor_dev.csv`
- A coluna `produtos_id` preenchida corretamente com base no cruzamento
- Registros que não puderam ser mapeados ficam com `produtos_id = 0`

## Estatísticas

Ao final da execução, o script mostra:

- Total de registros processados
- Quantos produtos foram mapeados com sucesso
- Quantos não puderam ser mapeados
- Exemplo das primeiras 5 linhas do resultado
