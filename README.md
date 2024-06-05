<!---
Copyright 2024. All rights reserved.

Licensed under the CC BY-NC-ND 4.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://creativecommons.org/licenses/by-nc-nd/4.0/

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
# GloveDataHub

<p align="center">
  <img alt="GloveDataHub" src="GUI\images\GDH.webp" width="300" height="300" style="max-width: 100%;">
  <br/>
  <br/>
</p>

This is an APP that allows you to extract raw data from your haptic gloves SenseGlove Nova 1, using the SenseGlove-API repository and the connection and calibration services provided by the SenseCom application.

<p align="center">
    <a href="https://www.glovedatahub.it">
        <img alt="SenseGlove" src="https://img.shields.io/badge/Our-website-brightgreen">
    </a>
    <a href="https://linktr.ee/glovedatahub">
        <img alt="Contact-us" src="https://img.shields.io/badge/Contact-us%20-blue">
    </a>
</p>


| | |
| --- | --- |
| **Description** | GloveDataHub is an APP that allows you to extract raw data from your haptic gloves SenseGlove Nova 1|
| **Authors** |Giovanni Fanara and Alfredo Giaocchino MariaPio Vecchio|
| **License** | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.it) |

---

## Table of Contents

- [GloveDataHub](#GloveDataHub)
  - [Introduction](#introduction)
  - [Getting started](#Getting-started)
  - [Code structure](#code-structure)
  - [License](#license)

---

## Introduction
GloveDataHub is an APP that allows you to extract raw data from SenseGlove Nova 1 haptic gloves. In addition, GloveDataHub incorporates a third-party application, provided by the glove manufacturer, which manages the connection between the PC and the gloves and facilitates the process of calibration of the devices. 
To capture data from haptic gloves, GloveDataHub uses an executable, obtained from the `glove_data_acquisition.cpp` script, and the `SGCoreCpp.dll` file to link the haptic glove management libraries. This executable is invoked by the action associated with the start measurement button, allowing the user to specify the duration of execution of the task, or not to configure any duration and ensure an infinite measurement time.
At the end of the measurement, the acquired data can be found stored in a file `.CSV`, which was created at the beginning of the data acquisition using the information entered by the user in the compilation fields required by the system.

## 1. Getting started

This section shows the procedures to be followed to properly install the software related to data acquisition from the SenseGlove Nova 1 haptic gloves and the GloveDataHub application. In addition, instructions are provided for proper use of the downloaded software.

### 1.1 How to acquire data from SenseGlove Nova 1 haptic gloves



#### 1.1.1 Requirements for acquiring data from SenseGlove Nova 1 haptic gloves

*Software Requirements*

- [MSVC v143 compiler](https://aka.ms/vs/17/release/vs_BuildTools.exe)

- [SenseGlove API v1.4.0](https://github.com/Adjuvo/SenseGlove-API/archive/refs/tags/v1.4.0.zip)

- [CMake version 3.29.2 or later](https://cmake.org/download/)

#### 1.2

In this section will be explained all the necessary software to install in order to use GloveDataHub on your computer.

*Software Requirements*

- Windows 10 or above

- Bluetooth 4.2 or above




To ensure the connection of your haptic gloves SenseGlove Nova 1 to your computer you must take the following steps:

- Go to to [SenseGlove](https://github.com/Adjuvo/SenseGlove-API/releases/tag/v1.4.0) and proceed with the installation of the SenseCcom application.
- Then go to the settings of your computer, make sure that both gloves are turned on and connect them to the pc via bluethoot.
    - if your pc is equipped with the Windows 11 operating system and you cannot find your Nova Glove in the list of possible devices
      you might need to change your Bluetooth Devices Discovery setting to “Advanced” as opposed to “Default”.

      <p align="center">
        <img alt="Win11BTConnection" src="GUI\images\winBT_adv.png" width="800" height="500" style="max-width: 100%;">
        <br/>
        <br/>
      </p>
      
      *Other Helpful Resources :*
      
      Here you can find information about ["How to Connect SenseGlove"](https://senseglove.gitlab.io/SenseGloveDocs/connecting-devices.html) to the system.

- After downloading the SenseCom application and connecting the SenseGlove by the bluetooth protocol to your computer, you should be able to open SenseCom application, click the connect button, and see something like this:

<p align="center">
  <img alt="SenseCom" src="GUI\images\SenseCom.png" width="512" height="287" style="max-width: 100%;">
  <br/>
  <br/>
</p>

You can also customize the settings of your haptic gloves to improve interaction with them as follows ["Customize SenseGlove interaction"](https://senseglove.gitlab.io/SenseGloveDocs/sensecom/settings.html).

### 1.2 Requirements for GloveDataHub

*Software Requirements*

The project is based on **Python 3.12.3** - one of the latest versions of Python at the time of writing. 

-  It is recommended to use a virtual environment to manage the dependencies of the project. For example [conda](https://docs.conda.io/en/latest/) ;
- The requirements are listed in the `requirements.txt` file;
  
  Inside the file `requirements.txt` you can find the following modules:

  - comtypes (1.4.2)
  - pillow (10.3.0)
  - psutil (5.9.8)
  - PyGetWindow (0.0.9)
  - PyQt6 (6.7.0)
  - PyQt6-Qt6 (6.7.0)
  - PyQt6-sip (13.6.0)
  - PyRect (0.2.0)
  - pywin32 (306)
  - pywinauto (0.6.8)
  - setuptools (69.5.1)
  - six (1.16.0)
  - wheel (0.43.0)

- The requirements can be installed on Windows by using the `prepare.ps1` script in this way : `.\prepare.ps1 -envName "name_conda_enviroment"` ;
- The requirements can be installed on Unix/linux by using the `prepare.sh` script in this way : `./prepare.sh name_conda_enviroment` ;

#### 1.2.1

#### 1.2.2


## Code structure

The code is structured as follows:

```
GDH_repository/
│
├── API/
│   ├── duration_time.py
│   ├── exe_manager.py
│   ├── main_manager.py
│   ├── main.py
│   └── user_data.py
├── build/
│   ├── glovedatahub/
│       ├── localpycs/
│
├── Data-Acquisition/
│   ├── docs/
│   │   ├── html/   
│   │   ├── latex/
│   ├── CMakeLists.txt
│   ├── gloves_data_acquisition.cpp
│   ├── gloves_data_acquisition.exe
│   └── SGCoreCpp.dll
│
├── Dist/
│   ├── glovedatahub/
│       ├── _internal/
│       ├── glovedatahub.exe
│
├── docs/
│   ├── build/
│   │   ├── doctrees/
│   │   │   ├── api.doctree
│   │   │   ├── enviroment.pickle
│   │   │   ├── gui.doctree
│   │   │   └── index.doctree
│   │   │
│   │   └── html/
│   │       ├── _sources/
│   │       │   ├── api.rst.txt
│   │       │   ├── gui.rst.txt
│   │       │   └── index.rst.txt
│   │       ├── _static/
│   │       │   ├── alabaster.css
│   │       │   ├── basic.css
│   │       │   ├── custom.css
│   │       │   ├── doctools.js
│   │       │   ├── documentation_options.js
│   │       │   ├── file.png
│   │       │   ├── langauage_data.js
│   │       │   ├── minus.png
│   │       │   ├── plus.png
│   │       │   ├── pygments.css
│   │       │   └── sphninx_highlight.js
│   │       ├── .buildinfo
│   │       ├── api.html
│   │       ├── genidex.html
│   │       ├── gui.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       └── searchindex.js
│   │
│   ├── source/
│   │   ├── _static/
│   │   ├── _templates/
│   │   ├── api.rst
│   │   ├── conf.py
│   │   ├── gui.rst
│   │   └── index.rst
│   ├── make.bat
│   └── Makefile
│   
├── GUI/
│   ├── images/
│   │   ├── GDH.ico 
│   │   ├── GDH.png
│   │   ├── GDH.webp
│   │   ├── glovedatahub_qr_code.png
│   │   ├── kore.png
│   │   ├── qr_code_github_repo_glovedatahub.jpg
│   │   └── SenseCom.png
│   │
│   ├── calibration_screen.py
│   ├── custom_button.py
│   ├── data_acquisition_screen.py
│   ├── data_entry_screen.py
│   ├── final_screen.py
│   ├── gui_main.py
│   ├── welcome_screen.py
│   └── window_manager.py
│
├── output/
│   ├── setup.exe
│   
├── screenshot/
│   ├── 1.png
│   ├── 2.1.png
│   ├── 2.2.png
│   ├── 3.1.png
│   ├── 3.2.png
│   ├── 4.1.1.png
│   ├── 4.1.2.png
│   ├── 4.2.png
│   ├── 4.3.png
│   ├── 5.png
│
├── glovedatahub.spec
│   
├── LICENSE
├── prepare.ps1
├── prepare.sh
├── README.md
├── requirements.txt
├── setup.iss
└── version.txt
```
- `API/` contains the classes for managing the executable file;
- `Data-Acquisition/` contains:
  - `gloves_data_acquisition.cpp` that is the C++ script;
  - `gloves_data_acquisition.exe` which is the executable file obtained from the c++ script.;
  - `SGCoreCpp.dll` contains the libraries linked to the executable file. 
  - `CMakeLists.txt`is the cmake file needed to create the executable from the file . cpp using the following command: `cmake -S . -B build -DSGCORECPP_PATH="C:/Users/Username/Downloads/SenseGlove-API-1.4.0/SenseGlove-API-1.4.0/Core/SGCoreCpp" `;
  - `docs` docs is a folder consisting of two subfolders html and latex inside which is contained the documentation related to the script c++ in pdf and html;
- `docs/` contains the HTML files related to the documentation and they are located inside the `build/` folder within the `html/` folder;
- `GUI/` contains the classes for managing the GUI interface;
- `glovedatahub.spec` it's a PyInstaller specification file and it is used to configure the bundling of your Python application into a standalone executable. The file includes the following key configurations:
  - `Main Script`: Specifies `GUI/gui_main.py` as the entry point of the application;
  - `Additional Data`: Includes additional data and directories such as `Data-Acquisition`, `API scripts`, and images from `GUI/images`.
  - `Executable Configuration`: Configures the executable with options like name (`glovedatahub`), icon (`GDH_icon.ico`), and other settings to manage binary exclusion, debugging, and compression.
- `prepare.ps1` is a PowerShell script that automates the setup of a Conda environment on Windows OS . It takes a single parameter, the name of the Conda environment, and performs the following tasks:
  - Checks if the environment name is provided; if not, it displays usage instructions and exits;
  - Creates the specified Conda environment with `Python 3.12.3` if it does not already exist;
  - Activates the Conda environment;
  - Installs the dependencies listed in `requirements.txt`;
  - Executes the gui_main.py script located in the `GUI directory`;
- `prepare.sh` this bash script automates the setup of a Conda environment on Unix-like operating systems. It takes a single parameter, the name of the Conda environment, and performs the following tasks:
  - Checks if the environment name is provided; if not, it displays usage instructions and exits;
  - Creates the specified Conda environment with `Python 3.12.3` if it does not already exist;
  - Activates the Conda environment;
  - Installs the dependencies listed in `requirements.txt`;
  - Executes the gui_main.py script located in the `GUI directory`;
- `requirements.txt` contains the list of dependencies for the project;
- `README.md` is the file you are currently reading;

---

## Download
You can easily download the application GloveDataHub scanning the qr code below which will take you back to our website `glovedatahub.it`, it from which you can download the app directly.

<p align="center">
  <img alt="GloveDataHub" src="GUI\images\glovedatahub_qr_code.png" width="400" height="450" style="max-width: 100%;">
  <br/>
  <br/>
</p>

## License

This project is licensed under the terms of the CC BY-NC-ND 4.0 license. You can find the full license in the `LICENSE` file.
