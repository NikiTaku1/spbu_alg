import random
import struct
from copy import deepcopy
from typing import TypedDict


def encode(x: tuple[float, float]) -> tuple[str, str]:
    binary_representation = format(struct.unpack(">Q", struct.pack(">d", x[0]))[0], "064b"), format(struct.unpack(">Q", struct.pack(">d", x[1]))[0], "064b")
    return binary_representation


def decode(binary_str: tuple[str, str]) -> tuple[float, float]:
    float_value1 = struct.unpack(">d", int(binary_str[0], 2).to_bytes(8, "big"))[0]
    float_value2 = struct.unpack(">d", int(binary_str[1], 2).to_bytes(8, "big"))[0]
    return float_value1, float_value2


def initialize_genes(flag: bool, bounds, amount):
    genes = []
    if flag == True:
        for _ in range(amount):
            genes.append(
                (random.randint(bounds[0], bounds[1]+1), random.randint(bounds[0], bounds[1]+1))
            )
    else:
        for _ in range(amount):
            genes.append(
                (random.uniform(bounds[0], bounds[1]), random.uniform(bounds[0], bounds[1]))
            )
    return genes



def func(f, x1, x2):

    return eval(f)


def mutate(gene, bounds) -> tuple[float, float]:
    mutated_gene = list(encode(gene))
    bit_position = random.randint(0, 63)

    for i in range(len(mutated_gene)):
        # Convert binary string to list of characters
        binary_list = list(mutated_gene[i])

        binary_list[bit_position] = "1" if binary_list[bit_position] == "0" else "0"

        # Convert back to a binary string
        mutated_gene[i] = "".join(binary_list)

    # Convert back to binary string and then decode to float values

    mutated_gene = (
        max(bounds[0], min(bounds[1], decode(mutated_gene)[0])),
        max(bounds[0], min(bounds[1], decode(mutated_gene)[1])),
    )
    return mutated_gene


def crossover(gene1, gene2, bounds):
    gene1 = encode(gene1)
    gene2 = encode(gene2)

    crossover_point = random.randint(2, 12)
    new_gene1 = (
        gene1[0][:crossover_point] + gene2[0][crossover_point:],
        gene1[1][:crossover_point] + gene2[1][crossover_point:],
    )
    new_gene2 = (
        gene2[0][:crossover_point] + gene1[0][crossover_point:],
        gene2[1][:crossover_point] + gene1[1][crossover_point:],
    )
    gene1 = (
        max(bounds[0], min(bounds[1], decode(new_gene1)[0])),
        max(bounds[0], min(bounds[1], decode(new_gene1)[1])),
    )

    gene2 = (
        max(bounds[0], min(bounds[1], decode(new_gene2)[0])),
        max(bounds[0], min(bounds[1], decode(new_gene2)[1])),
    )
    return gene1, gene2


def algorithm(flag: bool, genes, generations, f, mutation, bounds):
    history = [deepcopy(sorted(genes, key=lambda x: func(f, *x)))]
    for _ in range(generations):
        for i in range(len(genes)):
            if random.uniform(0, 1) > mutation / 100:
                genes[i] = mutate(genes[i], bounds)
        for i in range(0, len(genes) - len(genes) % 2, 2):
            genes[i], genes[i + 1] = crossover(genes[i], genes[i + 1], bounds)

        if flag == True:    
            genes = (
                sorted(genes, key=lambda x: func(f, *x))[
                : len(genes) // 10 * 9 + len(genes) % 10
                ]
                + history[-1][: len(genes) // 10]
            )

        genes = sorted(genes, key=lambda x: func(f, *x))
        history.append(deepcopy(genes))
    return history