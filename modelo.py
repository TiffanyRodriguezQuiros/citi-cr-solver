from pulp import *

def resolver_citi(analistas=12, min_swift=4, min_cartas=2, cap_min=15):
    """
    Resuelve el modelo LP de asignación de analistas de Citi CR.
    """

    # Crear modelo de minimización
    modelo = LpProblem("Citi_CR", LpMinimize)

    # Variables de decisión
    x1 = LpVariable("SWIFT", lowBound=0)
    x2 = LpVariable("CarCred", lowBound=0)
    x3 = LpVariable("Garantias", lowBound=0)

    # Función objetivo: minimizar tiempo de ciclo
    modelo += 3*x1 + 5*x2 + 4*x3, "Tiempo_total"

    # Restricciones
    modelo += x1 + x2 + x3 <= analistas, "Total_analistas"
    modelo += x1 >= min_swift, "Minimo_SWIFT"
    modelo += x2 >= min_cartas, "Minimo_cartas"
    modelo += 2*x1 + x2 + x3 >= cap_min, "Capacidad_minima"

    # Resolver modelo
    modelo.solve(PULP_CBC_CMD(msg=0))

    # Guardar resultados
    estado = LpStatus[modelo.status]

    if estado != "Optimal":
        return None, None, None, None, estado

    return x1.varValue, x2.varValue, x3.varValue, value(modelo.objective), estado
