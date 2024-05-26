param (
    [string]$envName
)

if (-not $envName) {
    Write-Host "Uso: .\prepare.ps1 <nome_ambiente_conda>"
    exit 1
}

$mainPath = "GUI\gui_main.py"

Write-Host "Nome dell'ambiente: $envName"
Write-Host "Path del main: $mainPath"

# Crea l'ambiente Conda (se non esiste)
if (-not (conda env list | Select-String -Pattern $envName)) {
    Write-Host "Creazione dell'ambiente Conda '$envName'..."
    conda create -y -n $envName python=3.12.3
}

# Attiva l'ambiente Conda
Write-Host "Attivazione dell'ambiente Conda '$envName'..."
conda activate $envName

# Installa le dipendenze
Write-Host "Installazione delle dipendenze dal file requirements.txt..."
pip install -r requirements.txt

# Esegui il file gui_main.py
Write-Host "Esecuzione del file $mainPath..."
python $mainPath

Write-Host "Ambiente '$envName' creato e dipendenze installate con successo!"
