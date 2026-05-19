class country:

    def __init__(self, data):

        self.nombre = data["name"]["common"]

        capital = data.get("capital", ["No disponible"])
        self.capital = capital[0]

        self.poblacion = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "Desconocida")

    def __str__(self):

        return (
            f"País: {self.nombre}"
            f"Capital: {self.capital}"
            f"Población: {self.poblacion:,}"
            f"Área: {self.area:,} km²"
            f"Región: {self.region}"
        )

    def density(self):

        if self.area == 0:
            return 0

        return self.poblacion / self.area

    def comparar(self, otros):

        paises = [self] + otros

        print("\n" + "=" * 80)
        print(
            f"{'PAÍS':15}"
            f"{'POBLACIÓN':15}"
            f"{'ÁREA':15}"
            f"{'DENSIDAD':15}"
        )
        print("=" * 80)

        for pais in paises:

            print(
                f"{pais.nombre:15}"
                f"{pais.poblacion:<15,}"
                f"{pais.area:<15,.0f}"
                f"{pais.density():<15.2f}"
            )

        mayor_poblacion = max(
            paises,
            key=lambda p: p.poblacion
        )

        mayor_area = max(
            paises,
            key=lambda p: p.area
        )

        mayor_densidad = max(
            paises,
            key=lambda p: p.density()
        )

        print("\n" + "-" * 80)

        print(
            f"Mayor población : {mayor_poblacion.nombre}"
        )

        print(
            f"Mayor área      : {mayor_area.nombre}"
        )

        print(
            f"Mayor densidad  : {mayor_densidad.nombre}"
        )