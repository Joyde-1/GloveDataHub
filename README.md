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
## GloveDataHub

<p align="center">
  <img alt="GloveDataHub" src="GUI\images\logo GloveDataHub.webp" width="300" height="300" style="max-width: 100%;">
  <br/>
  <br/>
</p>

This is an API that allows you to extract data from your SenseGlove haptic gloves, leveraging your PC's Bluetooth protocol and the gloves to establish the connection between devices, and utilizing the glove calibration service provided by the SenseCom API.

<p align="center">
    <a href="https://github.com/Adjuvo/SenseGlove-API.git">
        <img alt="SenseGlove" src="https://img.shields.io/badge/Download-SenseGlove-brightgreen">
    </a>
    <a href="https://www.senseglove.com/developer/">
        <img alt="Buy Haptic Gloves" src="https://img.shields.io/badge/Buy-Haptic%20Gloves-blue">
    </a>
</p>


| | |
| --- | --- |
| **Description** | GloveDataHub is an API that allows you to extract data from your SenseGlove haptic gloves |
| **Authors** |Giovanni Fanara and Alfredo Giaocchino MariaPio Vecchio|
| **License** | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.it) |

---

### Table of Contents

- [GloveDataHub](#GloveDataHub)
  - [Introduction](#introduction)
  - [Getting started](#Getting-started)
  - [Code structure](#code-structure)
  - [License](#license)

---

### Introduction
GloveDataHub is an API that allows you to extract data from your SenseGlove haptic gloves, which can be purchased through the button in the previous section. It ensures the connection of these gloves to your PC utilizing the Bluetooth protocol present in the devices. Additionally, the GloveDataHub API embeds a third-party application provided by the glove manufacturer, which manages the connection between the PC and the gloves and also facilitates the calibration process of the devices. Within the GloveDataHub API, it is further possible to extract data from your gloves using the executable obtained from a C++ script `glove_data_acquisition.exe` and the `.dll` file `SGCoreCpp.dll` of the haptic glove management libraries, now linked. This executable is invoked as an action associated with the start measurement button, allowing the user to specify a specific time to use during task execution, or the user can choose not to specify any time and ensure an infinite measurement time. At the end of the measurement, the results stored in a `.CSV` file are saved in the specified folder entered during the entry of the user's personal information fields.

### Getting started

#### 1.1 Getting the SenseCom application your computer

*Software Requirements*

- Windows 10 or above

- [SenseGlove](https://github.com/Adjuvo/SenseGlove-API.git)

To ensure the connection of your haptic senseglove gloves to your computer you must take the following steps:
- Go to to [SenseGlove](https://github.com/Adjuvo/SenseGlove-API.git) and proceed with installation of the sensecom application.
- Then go to the settings of your computer, make sure that both gloves are turned on and connect them to the pc via bluethoot.

#### 1.2 Requirements

The project is based on **Python 3.12.3** - one of the latest versions of Python at the time of writing. A few considerations:
- It is recommended to use a virtual environment to manage the dependencies of the project. For example [conda](https://docs.conda.io/en/latest/).
- The requirements are listed in the `requirements.txt` file and can be installed using the `prepare.ps1` for windows and the the user can run the prepare.bat script by passing the environment name conda as argument as follow:  `.\prepare.ps1 -envName "name_conda_enviroment" `, or on Unix/linux by running the `prepare.sh` file and the user can run the `prepare.sh`  script and pass the environment name conda as argument, in the following way: `./prepare.sh name_conda_enviroment`.

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

*Other Helpful Resources :*

Here you can find information about ["How to Connect SenseGlove"](https://senseglove.gitlab.io/SenseGloveDocs/connecting-devices.html) to the system.

- After downloading the SenseCom application and connecting the SenseGlove by the bluethoot protocol to your computer, you should be able to open SenseCom application, click the connect button, and see something like this:

<p align="center">
  <img alt="SenseCom" src="GUI\images\SenseCom.png" width="512" height="287" style="max-width: 100%;">
  <br/>
  <br/>
</p>

You can also customize the settings of your haptic gloves to improve interaction with them as follows ["Customize SenseGlove interaction"](https://senseglove.gitlab.io/SenseGloveDocs/sensecom/settings.html).


### Code structure

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
│
├── Datat-Acquisition/
│   ├── glove_data_acquisition.exe
│   └── SGCoreCpp.dll
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
│   │   ├── kore_Logo.png
│   │   ├── logo GloveDataHub.webp
│   │   ├── logo_GloveDataHub_new.png
│   │   ├── logo_GloveDataHub.png    
│   │   └── qr_code_github_repo_glovedatahub.jpg
│   ├── calibration_screen.py
│   ├── custom_button.py
│   ├── data_acquisition_screen.py
│   ├── data_entry_screen.py
│   ├── final_screen.py
│   ├── gui_main.py
│   ├── welcome_screen.py
│   └── window_manager.py
│
├── LICENSE
├── prepare.bat
├── prepare.sh
├── README.md
└── requirements.txt
```
- `API/` contains the classes for managing the executable file.
- `Data-Acquisition/` contains the executable of the C++ script `glove_data_acquisition.exe` and the linked .dll file `SGCoreCpp.dll` of the libraries.
- `docs/` contains the HTML files related to the documentation and they are located inside the `build/` folder within the `html/` folder.
- `GUI/` contains the classes for managing the GUI interface.
- `prepare.bat` is a script for setting up the environment on Windows OS - at the moment it only installs the requirements.
- `prepare.sh` is a script for setting up the environment on Unix/Linux OS - at the moment it only installs the requirements.
- `requirements.txt` contains the list of dependencies for the project.
- `README.md` is the file you are currently reading.

---

### License

This project is licensed under the terms of the CC BY-NC-ND 4.0 license. You can find the full license in the `LICENSE` file.