import random

def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    soma = num1 + num2
    print(f"Números gerados: {num1} e {num2}")
    print(f"Soma: {soma}")

if __name__ == "__main__":
    main()