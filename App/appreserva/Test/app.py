import requests

# Define la URL de la API GraphQL
url = "http://localhost:3000/graphql"

# Define la consulta GraphQL que deseas ejecutar
query = """
{
  books {
    id
    title
  }
}
"""

# Define las cabeceras para la solicitud
headers = {
    "Content-Type": "application/json",
}

# Define el cuerpo de la solicitud GraphQL
data = {
    "query": query,
}

# Realiza la solicitud HTTP POST a la API GraphQL
response = requests.get(url, headers=headers, json=data)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Analiza la respuesta JSON
    result = response.json()
    # Accede a los datos de la respuesta
    data = result.get("data")
    print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
