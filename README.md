# CEP Lookup (Python)
A simple Python script to search for address data based on Brazilian ZIP codes (CEP), using a public API — all without external dependencies.
## 📌 What It Does
This script receives a CEP (Brazilian postal code) as input and returns formatted address details, using the [ViaCEP API](https://viacep.com.br/).
## 🛠 How to Run
Make sure Python is installed and accessible via terminal. Then run:
```bash
py cep-lookup.py
```
You'll be prompted to enter a CEP. Example:
```
Enter the CEP (only numbers): 01001000
```
And the result will look like:
```
Address found:
Street: Praça da Sé
Neighborhood: Sé
City: São Paulo
State: SP
```
## 🔍 Why This Project?
This project was created to demonstrate basic usage of:
- Python input/output
- Handling HTTP requests with built-in libraries (`urllib`)
- Parsing JSON
- Simple CLI applications
It’s lightweight, educational, and requires **no dependencies**.
## 📁 Files
- `cep-lookup.py` – Main Python script
- `README.md` – Documentation
- `.gitignore` – Ignores `__pycache__/` and other environment files
- `LICENSE` – MIT License
