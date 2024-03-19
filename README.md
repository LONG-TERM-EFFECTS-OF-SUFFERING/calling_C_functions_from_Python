# Calling C functions from Python

## Members

- Calderón Prieto Brandon (2125973).

- Agudelo Hernández Carlos Andrés (2125653).

- Ortiz Rodríguez Nicol Valeria (2241463).

## Instructions

1. Create and enter a Python virtual environment.

	> This step is optional if you do not want to create a Python virtual environment.

	1. `python -m venv .env`.

	2. `source .env/bin/activate`.

2. Install the script dependency: `pip install numpy`.

3. Compile the library: `gcc -fPIC -shared -march=native scalar_multiplication_lib.c -o scalar_multiplication_lib.so`.

4. Run the script: `python main.py`.

> For a better view we, recommend the [Google Colab notebook version](https://drive.google.com/file/d/1tjVNd0iHFuEG1rwo3PSpVyqn2RbdPJXJ/view?usp=sharing).
