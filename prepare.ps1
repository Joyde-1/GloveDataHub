param (
    [string]$envName
)

if (-not $envName) {
    Write-Host "Usage: .\prepare.ps1 <nome_ambiente_conda>"
    exit 1
}

$mainPath = "GUI\gui_main.py"

Write-Host "Environment name: $envName"
Write-Host "Path of the main: $mainPath"

# Create the Conda environment (if it does not exist)
if (-not (conda env list | Select-String -Pattern $envName)) {
    Write-Host "Creation of the Conda environment '$envName'..."
    conda create -y -n $envName python=3.12.3
}

# Activate the Conda environment
Write-Host "Activation of the Conda environment '$envName'..."
conda activate $envName

# Install the dependencies
Write-Host "Installing dependencies from the requirements.txt file..."
pip install -r requirements.txt

Write-Host "Created '$envName' environment and successfully installed dependencies!"

# Run the file gui_main.py
Write-Host "Running the $mainPath file..."
python $mainPath