import random
from copy import deepcopy
from typing import TypedDict


class Particle(TypedDict):
    x1: float
    x2: float
    v1: float
    v2: float
    lbest_x1: float
    lbest_x2: float


# Инициализация частиц со случайными значениями в указанных пределах
def initialize_particles(bounds, n):
    return [
        Particle(
            x1=random.uniform(bounds[0], bounds[1]),
            x2=random.uniform(bounds[0], bounds[1]),
            v1=random.uniform(0, 1),
            v2=random.uniform(0, 1),
            lbest_x1=random.uniform(0, 1),
            lbest_x2=random.uniform(0, 1),
        )
        for _ in range(n)
    ]


# Вызов целевой функции
def func(fitness_func, x1, x2):
    return eval(fitness_func)


# Реализация алгоритма оптимизации на основе PSO
def algorithm(flag: bool, particles, generations, fitness_func):
    history = [
        deepcopy(sorted(particles, key=lambda x: func(fitness_func, x["x1"], x["x2"])))
    ]

    for _ in range(generations):
        gbest = (history[-1][0]["x1"], history[-1][0]["x2"])

        for particle in particles:
            f_was = func(fitness_func, particle["x1"], particle["x2"])

            if flag == True:
                k = 0.1 #от 0 до 1
                rp, rg = random.uniform(0, 1), random.uniform(0, 1)
                fp, fg = 5, 5
                f = fp*rp + fg*rg # должен быть больше 4
                norm = (2*k)/(abs(2 - f - ((f**2) - (4*f))**(0.5)))
                particle["v1"] = norm * (particle["v1"] + fp * rp *(particle["lbest_x1"] - particle["x1"]) + fg * rg * (gbest[0] - particle["x1"]))
                particle["v2"] = norm * (particle["v2"] + fp * rp *(particle["lbest_x2"] - particle["x2"]) + fg * rg * (gbest[1] - particle["x2"]))
            else:
                rp, rg = random.uniform(0, 1), random.uniform(0, 1)
                fp, fg = 0.5, 0.5
                particle["v1"] = (particle["v1"] + fp * rp *(particle["lbest_x1"] - particle["x1"]) + fg * rg * (gbest[0] - particle["x1"]))
                particle["v2"] = (particle["v2"] + fp * rp *(particle["lbest_x2"] - particle["x2"]) + fg * rg * (gbest[1] - particle["x2"]))

            particle["x1"] += particle["v1"]
            particle["x2"] += particle["v2"]

            f_now = func(fitness_func, particle["x1"], particle["x2"])

            if f_now < f_was:
                particle["lbest_x1"] = particle["x1"]
                particle["lbest_x2"] = particle["x2"]

        particles = sorted(
            particles, key=lambda x: func(fitness_func, x["x1"], x["x2"])
        )
        history.append(deepcopy(particles))

    return history