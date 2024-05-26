@echo off

:: Verifica se viene passato un argomento per il nome dell'ambiente
if "%~1"=="" (
    echo Uso: %0 <nome_ambiente_conda>
    exit /b 1
)

:: Nome dell'ambiente Conda
set ENV_NAME=%~1

:: Path del file gui_main.py
set MAIN_PATH=GUI\gui_main.py

:: Crea l'ambiente Conda (se non esiste)
conda env list | findstr /C:"%ENV_NAME%" >nul
if errorlevel 1 (
    echo Creazione dell'ambiente Conda '%ENV_NAME%'...
    conda create -y -n %ENV_NAME% python=3.8
)

:: Attiva l'ambiente Conda
echo Attivazione dell'ambiente Conda '%ENV_NAME%'...
call conda activate %ENV_NAME%

:: Installa le dipendenze
echo Installazione delle dipendenze dal file requirements.txt...
pip install -r requirements.txt

:: Esegui il file gui_main.py
echo Esecuzione del file %MAIN_PATH%...
python %MAIN_PATH%

:: Messaggio di completamento
echo Ambiente '%ENV_NAME%' creato e dipendenze installate con successo!
