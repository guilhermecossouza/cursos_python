def fibonacci(quantidade=0, sequencia=(0, 1)):
    # obs: importantíssimo condição de parada.
    return sequencia if len(sequencia) == quantidade else fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib, end=",")
    print("")
