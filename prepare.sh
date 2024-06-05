# Check if an argument for the environment name is passed
if [ -z "$1" ]; then
  echo "Usage: $0 <nome_ambiente_conda>"
  exit 1
fi

# Name of the Conda environment
ENV_NAME=$1

# Path of the file gui_main.py
MAIN_PATH="GUI/gui_main.py"

# Create the Conda environment (if it does not exist)
if ! conda env list | grep -q "$ENV_NAME"; then
  echo "Creation of the Conda environment '$ENV_NAME'..."
  conda create -y -n $ENV_NAME python=3.12.3
fi

# Activate the Conda environment
echo "Activation of the Conda environment '$ENV_NAME'..."
source activate $ENV_NAME

# Install the dependencies
echo "Installing dependencies from the requirements.txt file..."
pip install -r requirements.txt

# Completion message
echo "Created '$ENV_NAME' environment and successfully installed dependencies!"

# Run the file gui_main.py
echo "Running the $MAIN_PATH file..."
python $MAIN_PATH