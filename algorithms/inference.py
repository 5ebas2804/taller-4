"""Punto 5. Inferencia mediante encadenamiento hacia adelante."""
from models.logic import match_premises, substitute


def forward_chain(kb):
    """Retorna una tupla con los hechos originales y derivados, sin duplicados.

    Cada ronda usa los hechos disponibles al comenzarla. La base de entrada
    debe conservarse.
    kb.facts contiene objetos Atom; kb.rules contiene objetos Rule con los
    atributos premises y conclusion. Los hechos se comparan directamente.

    Tips:
    - match_premises(regla.premises, hechos) genera (sustitución, hechos usados).
      Si no hay coincidencias, no genera resultados. La sustitución es un
      diccionario, por ejemplo {'?p': 'ana'}.
    - substitute(regla.conclusion, sustitución) retorna un nuevo objeto Atom
      con las variables reemplazadas por los valores de la sustitución.
    """
    known = list(dict.fromkeys(kb.facts))    #kb no se modifica
    known_set = set(known)

    while True:
        snapshot = tuple(known)              # hechos disponibles al inicio
        new_facts = []

        for rule in kb.rules:
            for substitution, nousar in match_premises(rule.premises, snapshot):
                conclusion = substitute(rule.conclusion, substitution)
                if conclusion not in known_set and conclusion not in new_facts:
                    new_facts.append(conclusion)

        if not new_facts:                    # ronda sin hechos nuevos
            return tuple(known)

        known.extend(new_facts)              # se agregan al terminar la ronda
        known_set.update(new_facts)
