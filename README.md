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

---

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

---

- [GloveDataHub](#GloveDataHub)
  - [Introduction](#introduction)
  - [1. Getting started](#1-getting-started)
    - [1.1 Installation guide for SenseGlove Nova 1 haptic glove software](#11-installation-guide-for-senseglove-nova-1-haptic-glove-software)
      - [1.1.1 Requirements for using SenseGlove haptic gloves](#111-requirements-for-using-senseglove-haptic-gloves)
      - [1.1.2 Setup the software needed to capture data from SenseGlove Nova 1 haptic gloves](#112-setup-the-software-needed-to-capture-data-from-senseglove-nova-1-haptic-gloves)
      - [1.1.3 How to connect SenseGlove Nova 1 to your device](#113-how-to-connect-senseglove-nova-1-to-your-device)
    - [1.2 GloveDataHub installation guide](#12-glovedatahub-installation-guide)
      - [1.2.1 Requirements for GloveDataHub](#121-requirements-for-glovedatahub)
      - [1.2.2 Setup the software needed to GloveDataHub](#122-setup-the-software-needed-to-glovedatahub)
  - [2. Code structure](#2-code-structure)
  - [3. Meaning of data acquired by haptic gloves](#3-meaning-of-data-acquired-by-haptic-gloves)
    - [3.1 Anatomy of the human hand](#31-anatomy-of-the-human-hand)
    - [3.2 Variables contained in the HandPose class](#32-variables-contained-in-the-handpose-class)
    - [3.3 How "glove_data_acqusition.cpp" script works](#33-how-glove_data_acqusitioncpp-script-works)
      - [3.3.1 Features acquired](#331-features-acquired)
      - [3.3.2 Constraints and requirements](#332-constraints-and-requirements)
  - [4. How GloveDataHub works](#4-how-glovedatahub-works)
    - [4.1 Welcome Screen](#41-welcome-screen)
    - [4.2 Calibration Screen](#42-calibration-screen)
    - [4.3 Data Entry Screen](#43-data-entry-screen)
    - [4.4 Data Acquisition Screen](#44-data-acquisition-screen)
    - [4.5 Final Screen](#45-final-screen)
  - [Download](#download)
  - [License](#license)

## Introduction

---

GloveDataHub is an APP that allows you to extract raw data from SenseGlove Nova 1 haptic gloves. In addition, GloveDataHub incorporates a third-party application, provided by the glove manufacturer, which manages the connection between the PC and the gloves and facilitates the process of calibration of the devices. 
To capture data from haptic gloves, GloveDataHub uses an executable, obtained from the `glove_data_acquisition.cpp` script, and the `SGCoreCpp.dll` file to link the haptic glove management libraries. This executable is invoked by the action associated with the start measurement button, allowing the user to specify the duration of execution of the task, or not to configure any duration and ensure an infinite measurement time.
At the end of the measurement, the acquired data can be found stored in a file `.CSV`, which was created at the beginning of the data acquisition using the information entered by the user in the compilation fields required by the system.

## 1. Getting started

---

This section shows the procedures to be followed to properly install the software related to data acquisition from the SenseGlove Nova 1 haptic gloves and the GloveDataHub application. In addition, instructions are provided for proper use of the downloaded software.

### 1.1 Installation guide for SenseGlove Nova 1 haptic glove software

---

The process of acquiring data from SenseGlove Nova 1 haptic gloves is very laborious because it requires specific knowledge of C++ programming. This difficulty is overcome by the GloveDataHub application, which prepares files that perform this process.
Nevertheless, data acquisition from haptic gloves can be performed independently of GloveDataHub. Below will be presented the steps to use correctly the software used for this purpose.

#### 1.1.1 Requirements for using SenseGlove haptic gloves

---

*Software Requirements*

- [MSVC v143 compiler](https://aka.ms/vs/17/release/vs_BuildTools.exe)

- [SenseGlove API v1.4.0](https://github.com/Adjuvo/SenseGlove-API/archive/refs/tags/v1.4.0.zip)

- [CMake version 3.29.2 or later](https://cmake.org/download/)

#### 1.1.2 Setup the software needed to capture data from SenseGlove Nova 1 haptic gloves

***

After downloading the various software needed to communicate from your pc with haptic gloves, you can proceed to their installation. Below are instructions to install each software correctly.

##### SenseGlove API installation guide

___

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
  <img alt="VS Build Tools" src="Images\VS_Build_Tools.png" width="769" height="382" style="max-width: 100%; max-height: 100%">
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

#### 1.1.3 How to connect SenseGlove Nova 1 to your device

---

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

### 1.2 GloveDataHub installation guide

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

---

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
  - `gloves_data_acquisition.exe` which is the executable file obtained from the C++ script.;
  - `SGCoreCpp.dll` contains the libraries linked to the executable file. 
  - `CMakeLists.txt`is the cmake file needed to create the executable from the file . cpp using the following command: `cmake -S . -B build -DSGCORECPP_PATH="C:/Users/Username/Downloads/SenseGlove-API-1.4.0/SenseGlove-API-1.4.0/Core/SGCoreCpp" `;
  - `docs` docs is a folder consisting of two subfolders html and latex inside which is contained the documentation related to the script C++ in pdf and html;
- `docs/` contains the HTML files related to the documentation and they are located inside the `build/` folder within the `html/` folder;
- `GUI/` contains the classes for managing the GUI interface;
- `glovedatahub.spec` it's a PyInstaller specification file and it is used to configure the bundling of your Python application into a standalone executable. The file includes the following key configurations:
  - `Main Script`: Specifies `GUI/gui_main.py` as the entry point of the application;
  - `Additional Data`: Includes additional data and directories such as `Data-Acquisition`, `API scripts`, and images from `GUI/images`.
  - `Executable Configuration`: Configures the executable with options like name (`glovedatahub`), icon (`GDH_icon.ico`), and other settings to manage binary exclusion, debugging, and compression.
- `prepare.ps1` is a PowerShell script that automates the setup of a Conda environment on Windows OS. It takes a single parameter, the name of the Conda environment, and performs the following tasks:
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

## 3. Meaning of data acquired by haptic gloves

---

### 3.1 Anatomy of the human hand

---

The hand consists of five fingers and is the main center of the tactile sense. An essential tool of humanity, the hand not only facilitates interaction but also expression, integrating or replacing the word through sign language. 
The five fingers are known as:

- Thumb, derived from the Latin *"pollex-pollicis"*.

- Index, used to provide directions.

- Middle, middle between the other fingers.

- Ring, where the wedding ring is worn.

- Pinky, the smallest, known in Latin as *"digitus minimus"*.

The human hand contains at least 27 bones:

- The carpus, which makes up the wrist, consists of 8 bones arranged in two rows: a proximal and a distal. The proximal row includes: scaphoid, semilunar, pyramidal and pisiform. The distal row includes: trapezium, trapezoid, capitate and hooked. The carpus enters into direct articulation with the distal epiphysis of the radius, the bone of the forearm, with which it establishes the radio-carpal articulation. The ulna, another forearm bone, does not articulate directly with the carpus but is separated by a disc called the triangular ligament of the distal radius-ulnar joint.

- The metacarpal includes 5 long bones, hollow and rich in bone marrow. They articulate proximal with the carpus and distally with the phalanges.

- The phalanges, which make up the fingers, comprise 14 bones. In particular, each finger is formed by three distinct phalanges in: proximal phalanx or first phalanx, which articulates with the corresponding metacarpal bone, middle phalanx or second phalanx, which is articulated with the previous, and distal phalanx or third phalanx or nail phalanx, which contains the nail. An exception is the thumb, in which there are only two distinct phalanges in: proximal phalanx or first phalanx of the thumb and distal phalanx or second phalanx or nail phalanx of the thumb.

<br>
<p align="center">
  <img alt="Hand Anatomy" src="Images\hand_anatomy.png" width="850" height="797" style="max-width: 100%;">
  <br/>
  <br/>
</p>

### 3.2 Variables contained in the HandPose class

---

Variables in the `HandPose` class are contained within vectors, T[ ], or nested vectors, T[ ][ ]. Vectors always have a maximum length of 5 and the first index will always be used to indicate the finger, in order from the thumb [0] to the little finger [4]. In nested vectors, the second index indicates the finger joint, relative to the position closest to the wrist and the one furthest from the wrist. These nested vectors are 5 x 4 in length, except for the `jointAngles` variable, which is 5 x 3 in length, as it does not include fingertips. 

The parameter `handAngles` represents the articulation of finger joints, in radians. It is a vector of size 5 x 3 within which are contained vectors (`Vect3D`), whose quantities represent the Pronation/Supination (x), Bending/Extension (y) and Abduction/Adduction (z) of this joint. The first index indicates the finger, from the thumb (0) to the little finger (4), while the second indicates the articulation of that finger. Doesn’t include fingertips.

The values of these angles are limited to the "normal" human ranges, especially the operating ranges are those shown in the figure below.

The boolean variable `isRight`, if true, indicates that the HandPose object was generated for the right hand, otherwise, for the left hand. It is mainly used to match a glove, via a HandPose object, to the appropriate hand.

<br>
<p align="center">
  <img alt="Joint Angles Ranges" src="Images\joint_angles_ranges.png" width="705" height="371" style="max-width: 100%;">
  <br/>
  <br/>
</p>

The `jointPositions` represent the position of the hand joints in 3D space, in millimetres, relative to the wrist (0, 0, 0). These variables consist of a vector of size 5 x 4 within which are contained vectors (`Vect3D`). The first index of this matrix indicates the finger, from the thumb (0) to the little finger (4), while the second indicates the joint relative to the finger. It also includes fingertips. 
This rotation consists of Euler’s angles [-90,0,0] for the left hand and [90,0,0] for the right hand. 

The `jointRotations` represent the rotation in the 3D space relative to the wrist, they consist of quaternions. Note that being relative to the wrist does not take into account the rotation (IMU) of the glove. `jointRotations` is a vector of size 5 x 4.  The first index indicates the finger, from the thumb (0) to the little finger (4), while the second indicates the articulation of that finger. It also includes fingertips.

### 3.3 How "glove_data_acqusition.cpp" script works

---

For the creation of the `glove_data_acquisition.cpp` script, as previously expressed, the github repository [SenseGlove API v1.4.0](#senseglove-api-installation-guide) was used, in order to capture data from the SenseGlove Nova 1 haptic gloves. The goal of this script is to allow the capture of data regarding the movement of the hand in space. Below is a description of the measured quantities, which are part of the `HandPose` class that contains all the positions and rotations that can be used to represent a hand in 3D space.

#### 3.3.1 Features acquired

---

These quantities measured using SenseGlove Nova 1 haptic gloves are saved in a file .CSV with tabulation character: *";"*. The data are arranged in columns according to the following distribution:

- `Date_Time`: contains the date time in the following aaaammgg_hhmmss format;

- `Hand_Angles_FingerName_Index_Axis_Right/Left`: consists of 15 values;

- `Joint_Positions_FingerName_JointIndex_PositionIndex_Right/Left`: 20 values are reported for this size;

- `Joint_Rotations_FingerName_JointIndex_PositionIndex_Right/Left`: in this case we find 20 values;

#### 3.3.2 Constraints and requirements

---

The script is started correctly, if and only if, both haptic gloves are connected to the system.

In order to ensure that the program works properly, you must ensure that the SenseCom application remains open at all times. If SenseCom is not active when the executable file starts, it will open automatically. If, on the other hand, SenseCom is closed during the execution of the program `glove_data_acqusition.exe`, then the program immediately stops data acquisition and returns a code equal to `5`.

In order to run the C++ script you must input the path to the file .CSV, where the acquired data will be saved, and an integer number, indicating the duration of the test in seconds. If the user prefers an unlimited duration, input `-1` is available. In this case, in order to stop the execution there are several actions you can perform:

- Close the SenseCom application;

- Break the bluetooth connection between the haptic gloves and the device;

- Switching off the gloves by force;

- Stop execution of the executable.

## 4. How GloveDataHub works

---

In this section we will explain the entire operation of the GloveDataHub application starting from the calibration of the haptic gloves to the extraction of data.

### 4.1 Welcome Screen

---

The screen in question plays the role of welcome screen and aims to show the features offered by the GUI , which will be presented in subsequent screens.

<br>
<p align="center">
  <img alt="Welcome Screen" src="Images\1.png" width="800" height="485" style="max-width: 100%;">
  <br/>
  <br/>
</p>

### 4.2 Calibration Screen

---

The screen in question offers the possibility to proceed with the calibration process of haptic gloves. By pressing the Start SenseCom button, you can start an external application, owned by the company that created the gloves, whose primary objective is to ensure the connection and calibration of haptic gloves.

<br>
<p align="center">
  <img alt="Calibration Screen" src="Images\2.1.png" width="800" height="485" style="max-width: 100%;">
  <br/>
  <br/>
</p>

- After connecting the haptic gloves to your computer, you should be able to open SenseCom application by pressing the Start SenseCom Button that is present in the current scrren, click the connect button, and see something like this:

<br>
<p align="center">
  <img alt="SenseCom" src="Images\SenseCom.png" width="400" height="222" style="max-width: 100%;">
  <br/>
  <br/>
</p>

You can also customize the settings of your haptic gloves to improve interaction with them as follows ["Customize SenseGlove interaction"](https://senseglove.gitlab.io/SenseGloveDocs/sensecom/settings.html).

### 4.3 Data Entry Screen

---

This screen allows the user to enter their personal data and the path to the folder where the CSV. file will be stored.
If no path is specified, the Documents folder is selected by default. If the user prefers not to indicate the first name, last name and identification code, the system will automatically generate the latter randomly.

<br>
<p align="center">
  <img alt="Data Entry Screen" src="Images\3.2_sensecom.png" width="800" height="485" style="max-width: 100%;">
  <br/>
  <br/>
</p>

### 4.4 Data Acquisition Screen

---

On the screen in question, the data is acquired. In order to accurately initiate the data capture process, the user is required to specify the test time in minutes. In case the user does not enter the duration, we proceed with the mode with unlimited duration.
In any case, the data acquisition can be interrupted at any time by the user by pressing the specific stop button.
Once the data acquisition is completed, if you are not satisfied with the measurement, you can repeat the process by overwriting the file . CSV previously created.

<br>
<p align="center">
  <img alt="Data Acquisition Screen" src="Images\4.1.2_sensecom.png" width="800" height="485" style="max-width: 100%;">
  <br/>
  <br/>
</p>

### 4.5 Final Screen

---

The screen in question gives the possibility to the user to start a new measurement through the appropriate button, or to proceed to the closure of the application through the *Close* button.

<br>
<p align="center">
  <img alt="Final Screen" src="Images\5.png" width="800" height="485" style="max-width: 100%;">
  <br/>
  <br/>
</p>

## Download

---

You can easily download the application GloveDataHub scanning the qr code below which will take you back to our website `glovedatahub.it`, it from which you can download the app directly.

<br>
<p align="center">
  <img alt="GloveDataHub QR Code" src="Images\glovedatahub_qr_code.png" width="300" height="350" style="max-width: 100%;">
  <br/>
  <br/>
</p>

## License

---

This project is licensed under the terms of the CC BY-NC-ND 4.0 license. You can find the full license in the `LICENSE` file.
