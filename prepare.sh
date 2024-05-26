#!/bin/bash

# Verifica se viene passato un argomento per il nome dell'ambiente
if [ -z "$1" ]; then
  echo "Uso: $0 <nome_ambiente_conda>"
  exit 1
fi

# Nome dell'ambiente Conda
ENV_NAME=$1

# Path del file gui_main.py
MAIN_PATH="GUI/gui_main.py"

# Crea l'ambiente Conda (se non esiste)
if ! conda env list | grep -q "$ENV_NAME"; then
  echo "Creazione dell'ambiente Conda '$ENV_NAME'..."
  conda create -y -n $ENV_NAME python=3.12.3
fi

# Attiva l'ambiente Conda
echo "Attivazione dell'ambiente Conda '$ENV_NAME'..."
source activate $ENV_NAME

# Installa le dipendenze
echo "Installazione delle dipendenze dal file requirements.txt..."
pip install -r requirements.txt

# Esegui il file gui_main.py
echo "Esecuzione del file $MAIN_PATH..."
python $MAIN_PATH

# Messaggio di completamento
echo "Ambiente '$ENV_NAME' creato e dipendenze installate con successo!"
