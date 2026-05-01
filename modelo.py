from pulp import *

def resolver_citi(analistas=12, min_swift=4, min_cartas=2, cap_min=15):
    """Resuelve el LP de asignación de analistas de Citi CR"""
    modelo = LpProblem('Citi_CR', LpMinimize)

    x1 = LpVariable('SWIFT', lowBound=0)
    x2 = LpVariable('CarCred', lowBound=0)
    x3 = LpVariable('Garantias', lowBound=0)

    modelo += 3*x1 + 5*x2 + 4*x3

    modelo += x1 + x2 + x3 <= analistas, 'total'
    modelo += x1 >= min_swift, 'min_SWIFT'
    modelo += x2 >= min_cartas, 'min_cartas'
    modelo += 2*x1 + x2 + x3 >= cap_min, 'capacidad'

    modelo.solve(PULP_CBC_CMD(msg=0))

    return x1.varValue, x2.varValue, x3.varValue, value(modelo.objective)
