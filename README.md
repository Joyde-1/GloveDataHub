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
  <img alt="GloveDataHub" src="Images\GDH.webp" width="300" height="300" style="max-width: 100%;">
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
  - [1. Getting started](#1-getting-started)
  - [2. Code structure](#2-code-structure)
  - [License](#license)

---

## Introduction
GloveDataHub is an APP that allows you to extract raw data from SenseGlove Nova 1 haptic gloves. In addition, GloveDataHub incorporates a third-party application, provided by the glove manufacturer, which manages the connection between the PC and the gloves and facilitates the process of calibration of the devices. 
To capture data from haptic gloves, GloveDataHub uses an executable, obtained from the `glove_data_acquisition.cpp` script, and the `SGCoreCpp.dll` file to link the haptic glove management libraries. This executable is invoked by the action associated with the start measurement button, allowing the user to specify the duration of execution of the task, or not to configure any duration and ensure an infinite measurement time.
At the end of the measurement, the acquired data can be found stored in a file `.CSV`, which was created at the beginning of the data acquisition using the information entered by the user in the compilation fields required by the system.

## 1. Getting started

This section shows the procedures to be followed to properly install the software related to data acquisition from the SenseGlove Nova 1 haptic gloves and the GloveDataHub application. In addition, instructions are provided for proper use of the downloaded software.

### 1.1 How to acquire data from SenseGlove Nova 1 haptic gloves

---

The process of acquiring data from SenseGlove Nova 1 haptic gloves is very laborious because it requires specific knowledge of C++ programming. This difficulty is overcome by the GloveDataHub application, which prepares files that perform this process.
Nevertheless, data acquisition from haptic gloves can be performed independently of GloveDataHub. Below will be presented the steps to use correctly the software used for this purpose.

#### 1.1.1 Requirements for using SenseGlove Nova 1 haptic gloves

---

*Software Requirements*

- [MSVC v143 compiler](https://aka.ms/vs/17/release/vs_BuildTools.exe)

- [SenseGlove API v1.4.0](https://github.com/Adjuvo/SenseGlove-API/archive/refs/tags/v1.4.0.zip)

- [CMake version 3.29.2 or later](https://cmake.org/download/)

#### 1.1.2 Setup the software needed to capture data from SenseGlove Nova 1 haptic gloves

---

After downloading the various software needed to communicate from your pc with haptic gloves, you can proceed to their installation. Below are instructions to install each software correctly.

##### SenseGlove API installation guide

---

The main repository for interfacing with haptic gloves is SenseGlove API. It contains various libraries that allow you to perform many functions, including managing communication with gloves and capture data.
Also included are the installation files of SenseCom, the main application for connecting with haptic gloves.

- Download (or clone) the [SenseGlove API v1.4.0](https://github.com/Adjuvo/SenseGlove-API/archive/refs/tags/v1.4.0.zip) repository from github.
The SenseCom folder contains the SenseCom installation file.

- Run the SenseCom installation file suitable for your operating system.
  - *On Windows 10/11*:

    If you want to use the GloveDataHub application, be sure to install SenseCom for all users.

  - *On Linux*:
    
    Right click on `SenseCom.x86_64`, in the `SenseCom/Linux` folder, and go to the permission tab by selecting: *"Allow the file to run as a program"*.
    Make sure that you have set permissions for SenseCom, so that you can use serial ports using the `sudo adduser $USER dialout` command.

<br>

##### MSVC v143 compiler installation guide

---

To compile the files . cpp, where the libraries contained in the Core folder on SenseGlove API are imported, it is highly recommended to use the MSVC v143 compiler.

Below are the steps for installation:

- Install [Build Tools for Visual Studio 2022](https://aka.ms/vs/17/release/vs_BuildTools.exe).

- Download and install *"Desktop Application Development with C++"*, which contains the MSVC v143 compiler.

*Please note* : [Build Tools for Visual Studio 2022](https://aka.ms/vs/17/release/vs_BuildTools.exe) is not fully compatible with ARM architectures.

<br>
<p align="center">
  <img alt="VS_Build_Tools" src="Images\VS_Build_Tools.png" width="769" height="382" style="max-width: 100%; max-height: 100%">
  <br/>
  <br/>
</p>

##### CMake installation guide

---

If you have edited the `gloves_data_acquisition.cpp` file or created a C++ file, which uses the libraries contained in SenseGlove API, you will need to compile it to create its executable counterpart. Because you are using a third-party API, you must link libraries to code written using files that only software like cmake can generate.
The steps to do this step of compiling the C++ code will be described below.

- Install [CMake](https://cmake.org/download/).

- If you have written a new C++ file:

  - Create a file, which must be called `CMakeLists.txt`, in the same folder as the C++ file. Inside this file you must write the cmake code to include the file `LinkSGCoreCpp.cmake`. The latter is contained in the `Core/SGCoreCpp` folder in the SenseGlove API and links the .lib and .dll files.
  Run the following commands in order: `cmake -S . -B build` and `cmake --build build`.

  If you have modified and now want to compile the `gloves_data_acquisition.cpp` file in this repository:

  - Placed on powershell/terminal in the directory where the `gloves_data_acquisition.cpp` and `CMakeLists.txt` files are located.
  
  - Run the following commands, making sure to change the path of the SGCoreCpp folder: `cmake -S . -B build -DSGCORECPP_PATH="C:/Users/Username/Downloads/SenseGlove-API-1.4.0/SenseGlove-API-1.4.0/Core/SGCoreCpp"` and `cmake --build build`.

- You will find the executable file inside the `build/Debug` folder.

### 1.1.3 How to connect SenseGlove Nova 1 to your device

To ensure the connection of your haptic gloves SenseGlove Nova 1 to your computer you must take the following steps:

- Go to the settings of your computer, make sure that both gloves are turned on and connect them to the PC via bluetooth.
    - if your pc is equipped with the Windows 11 operating system and you cannot find your Nova Glove in the list of possible devices
      you might need to change your Bluetooth Devices Discovery setting to “Advanced” as opposed to “Default”.

      <br>
      <p align="center">
        <img alt="Win11BTConnection" src="Images\winBT_adv.png" width="800" height="500" style="max-width: 100%;">
        <br/>
        <br/>
      </p>
      
      *Other Helpful Resources :*
      
      Here you can find information about ["How to Connect SenseGlove"](https://senseglove.gitlab.io/SenseGloveDocs/connecting-devices.html) to the system.

### 1.2 GloveDataHub application guide

---

The GloveDataHub application consists of several files that you can view and edit.
The following paragraphs describe the steps to access and execute the code.

#### 1.2.1 Requirements for GloveDataHub

---

This section will explain all the software needed to install, use, edit and recreate GloveDataHub on your computer.

*Software Requirements*

- [Python 3.12.3](https://www.python.org/downloads/release/python-3123/)

- [Conda 24.4.0](https://docs.conda.io/en/latest/)

- [SenseGlove API v1.4.0](#senseglove-api-installation-guide)

- [MSVC v143 compiler](#msvc-v143-compiler-installation-guide)

- [Inno Setup Compiler 6.2.2](https://jrsoftware.org/download.php/is.exe)

#### 1.2.2 Setup the software needed to GloveDataHub

---

GloveDataHub is an application based on **Python 3.12.3** - one of the latest versions of Python at the time of writing.

Below are the steps to configure the Python project on your PC.

- It is recommended to use a virtual environment to manage the dependencies of the project. For example [Conda](https://docs.conda.io/en/latest/).
- The requirements are listed in the `requirements.txt` file.
  
  Inside the file `requirements.txt` you can find the following modules:

  - alabaster (0.7.16)
  - altgraph (0.17.4)
  - Babel (2.15.0)
  - certifi (2024.2.2)
  - charset-normalizer (3.3.2)
  - colorama (0.4.6)
  - comtypes (1.4.2)
  - docutils (0.21.2)
  - idna (3.7)
  - imagesize (1.4.1)
  - Jinja2 (3.1.4)
  - MarkupSafe (2.1.5)
  - packaging (24.0)
  - pefile (2023.2.7)
  - pillow (10.3.0)
  - pockets (0.9.1)
  - psutil (5.9.8)
  - PyGetWindow (0.0.9)
  - Pygments (2.18.0)
  - pyinstaller (6.7.0)
  - pyinstaller-hooks-contrib (2024.6)
  - PyQt6 (6.7.0)
  - PyQt6-Qt6 (6.7.0)
  - PyQt6-sip (13.6.0)
  - PyRect (0.2.0)
  - pywin32 (306)
  - pywin32-ctypes (0.2.2)
  - pywinauto (0.6.8)
  - requests (2.32.3)
  - setuptools (69.5.1)
  - six (1.16.0)
  - snowballstemmer (2.2.0)
  - Sphinx (7.3.7)
  - sphinxcontrib-applehelp (1.0.8)
  - sphinxcontrib-devhelp (1.0.6)
  - sphinxcontrib-htmlhelp (2.0.5)
  - sphinxcontrib-jsmath (1.0.1)
  - sphinxcontrib-napoleon (0.7)
  - sphinxcontrib-qthelp (1.0.7)
  - sphinxcontrib-serializinghtml (1.1.10)
  - urllib3 (2.2.1)
  - wheel (0.43.0)

- Depending on operating system usage: 

  - On Windows 10/11: 
  
    The requirements can be installed by using the `prepare.ps1` script in this way: `.\prepare.ps1 -envName "name_conda_enviroment"`.

  - On Linux:

    The requirements can be installed by using the `prepare.sh` script in this way: `./prepare.sh name_conda_enviroment`.

To run GloveDataHub correctly, you must install the [SenseGlove API](#senseglove-api-installation-guide) and the [MSVC v143 compiler](#msvc-v143-compiler-installation-guide). If they have not been installed yet, please review the corresponding guide to their installation in the previous sections.

If you want to recreate the GloveDataHub application, you need to follow these steps:
- Edit the `glovedatahub.spec` file and compile it using the appropriate command: `pyinstaller glovedatahub.spec`.
- Installing [Inno Setup Compiler](https://jrsoftware.org/download.php/is.exe).
- Edit the `setup.iss` file, open the Inno Setup Compiler application and compile the question file.

## 2. Code structure

The files inside the repository have the following structure:

```
GDH_repository/
|
├── API/
│   ├── duration_time.py
│   ├── exe_manager.py
│   ├── main_manager.py
│   ├── main.py
│   └── user_data.py
|
├── Application/
│   └── GloveDataHub-installer.exe
|
├── build/
│   └── glovedatahub/
│       ├── localpycs/
│
├── Data-Acquisition/
│   ├── docs/
│   │   ├── html/   
│   │   └── latex/
│   ├── CMakeLists.txt
│   ├── gloves_data_acquisition.cpp
│   ├── gloves_data_acquisition.exe
│   └── SGCoreCpp.dll
│
├── Dist/
│   └── glovedatahub/
│       ├── _internal/
│       └── glovedatahub.exe
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
│   │   └── kore.png
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
├── Images/
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
|   ├── GDH.webp
│   ├── glovedatahub_qr_code.png
│   ├── qr_code_github_repo_glovedatahub.jpg
│   ├── SenseCom.png
|   ├── VS_Build_Tools.png
|   └── winBT_adv.png
│
├── glovedatahub.spec
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
- `setup.iss` is the file to create the GloveDataHub application installer;
- `version.txt` is the file that contains information about the released version of GloveDataHub.

## 3. How GloveDataHub works

In this section we will explain the entire operation of the GloveDataHub application starting from the connection of the haptic gloves to the extraction of data.

### 3.1 Welcome Screen

### 3.2 Calibration Screen



- After connecting the haptic gloves to your computer, you should be able to open SenseCom application, click the connect button, and see something like this:

<br>
<p align="center">
  <img alt="SenseCom" src="Images\SenseCom.png" width="400" height="222" style="max-width: 100%;">
  <br/>
  <br/>
</p>

You can also customize the settings of your haptic gloves to improve interaction with them as follows ["Customize SenseGlove interaction"](https://senseglove.gitlab.io/SenseGloveDocs/sensecom/settings.html).

### 3.3 Data Entry Screen

### 3.4 Data Acquisition Screen

### 3.5 Final Screen

## Download
You can easily download the application GloveDataHub scanning the qr code below which will take you back to our website `glovedatahub.it`, it from which you can download the app directly.

<br>
<p align="center">
  <img alt="GloveDataHub" src="Images\glovedatahub_qr_code.png" width="300" height="350" style="max-width: 100%;">
  <br/>
  <br/>
</p>

## License

This project is licensed under the terms of the CC BY-NC-ND 4.0 license. You can find the full license in the `LICENSE` file.