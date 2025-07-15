@echo off
echo Verificando se o Python está instalado...
python --version 2>nul
if errorlevel 1 (
    echo Python não encontrado. Por favor, instale o Python primeiro.
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Escolha a versão do script para executar:
echo 1. Versão com pandas (recomendada - mais rápida)
echo 2. Versão sem pandas (usa apenas bibliotecas padrão)
echo.
set /p opcao="Digite sua escolha (1 ou 2): "

if "%opcao%"=="1" (
    echo.
    echo Instalando pandas...
    pip install pandas
    echo.
    echo Executando script com pandas...
    python main.py
) else if "%opcao%"=="2" (
    echo.
    echo Executando script sem pandas...
    python main_sem_pandas.py
) else (
    echo Opção inválida. Executando versão sem pandas por padrão...
    python main_sem_pandas.py
)

echo.
echo Script finalizado. Pressione qualquer tecla para sair.
pause 