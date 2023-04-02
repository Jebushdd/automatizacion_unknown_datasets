Other Languages: <kbd>[<img title="Leer en inglés" alt="Leer en inglés" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/gb.svg" height="15">](translations/README.en.md)</kbd>  &emsp;
Follow me on <kbd>[<img title="Mi perfil en LinkedIn" alt="Mi perfil en LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="15">](https://www.linkedin.com/in/martinezjesusfl/)</kbd>

# Unknown Datasets downloader script

**Tech Stack:**  
<img title="Python" alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" height="20"> &emsp;
<img title="HTML" alt="HTML" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" height="20"> &emsp;

## Description
This project automatically downloads datasets provided by [Unknown Datasets](https://linktr.ee/unknow.datasets) and redirects you to their Cafecito so you can show them your support!  
In this initial version you only have the Python script. In my free time I'll work on making this process more robust.  
For now, I'm not working on a GUI because you already have [Unknown Datasets](https://linktr.ee/unknow.datasets) web page. However, we can orchestrate the automation process with [Prefect](https://www.prefect.io/). 

## Files
In this repo you'll find the following files:
- ```requirements.txt``` To install the python script libraries
- ```exportar_unknown_datasets.py``` to run the script
- ```exportar_unknown_datasets.ipynb``` is the jupyter notebook with the notes on the development process
- ```.gitignore``` to ignore generated files and the virtual environment folder.

## Instructions
1. Set up the environment:  
``````powershell
python -m venv unknown_datasets_env
``````

2. Install libraries
``````powershell
pip install -r requirements.txt
``````

3. Run the script
``````powershell
python exportar_unknown_datasets.py
``````
