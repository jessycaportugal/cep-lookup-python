import urllib.request
import json
def get_cep_info(cep):
   url = f'https://viacep.com.br/ws/{cep}/json/'
   try:
       with urllib.request.urlopen(url) as response:
           data = response.read()
           json_data = json.loads(data)
           if 'erro' in json_data:
               print("CEP not found.")
           else:
               print(f"CEP: {json_data.get('cep')}")
               print(f"Street: {json_data.get('logradouro')}")
               print(f"Neighborhood: {json_data.get('bairro')}")
               print(f"City: {json_data.get('localidade')}")
               print(f"State: {json_data.get('uf')}")
   except Exception as e:
       print(f"Error fetching data: {e}")
if __name__ == '__main__':
   cep = input("Enter the CEP (only numbers): ")
   get_cep_info(cep)