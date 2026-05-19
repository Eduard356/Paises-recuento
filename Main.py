from country_api import CountryAPI


def main():

    api = CountryAPI()

    nombres = [

        "japan",
        "argentina",
        "mexico",
        "ecuador",
        "spain",

        "egypt",
        "denmark",
        "uganda",
        "india",
        "sweden"
    ]

    paises = api.by_names(nombres)

    if len(paises) > 0:

        paises[0].comparar(
            paises[1:]
        )


if __name__ == "__main__":
    main()