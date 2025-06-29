def main ():
    print("👋 Hola, soy Sami. Escribe algo para comenzar (escribe salir para terminar).")

    while True: 
        entrada = input("Tú").strip().lower()

        if entrada == "salir":
            print("👋 ¡Hasta luego!")
            break

        print("🤖 Sami: Te escucho, pero aún no entiendo qué hacer.")

if __name__ == "__main__":
    main()        