import os

def main():
    usuario = os.getenv("USERNAME")
    print(f"Hola, {usuario} desde Github")

if __name__ == "__main__":
    main()