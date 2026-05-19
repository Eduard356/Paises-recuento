import requests

from concurrent.futures import ThreadPoolExecutor

from country import Country


class CountryAPI:

    BASE_URL = "https://restcountries.com/v3.1/name/"

    def obtener_pais(self, nombre):

        try:

            respuesta = requests.get(
                self.BASE_URL + nombre,
                timeout=10
            )

            respuesta.raise_for_status()

            datos = respuesta.json()[0]

            return Country(datos)

        except Exception as e:

            print(
                f"Error consultando "
                f"{nombre}: {e}"
            )

            return None