#bycripton
import phonenumbers, argparse  
from phonenumbers import carrier, geocoder, timezone

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

parse = argparse.ArgumentParser("Ingrese un numero de telefono con el codigo del pais")
parse.add_argument('-n', '--number', help="Numero de telefono")
parse = parse.parse_args()

try:
    if parse.number:

        banner = """

 ██████╗██████╗ ██╗██████╗ ████████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗████╗  ██║
██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║██╔██╗ ██║
██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║██║╚██╗██║
╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                  
         """
        print(RED + banner + RESET)

        parse.number = phonenumbers.parse(parse.number)
        hora = timezone.time_zones_for_number(parse.number)
        operadora = carrier.name_for_number(parse.number, "es")
        pais = geocoder.description_for_number(parse.number, "es")
        n_valido = phonenumbers.is_valid_number(parse.number)
        n_existe = phonenumbers.is_possible_number(parse.number)
        print(YELLOW + "Zona horaria: " + RESET, hora[0])
        print(YELLOW + "Operadora: " + RESET, operadora)
        print(YELLOW + "Pais: " + RESET, pais)
        if n_valido:
            print(YELLOW + "El numero es valido: " + RESET, "SI")
        else:
            print(YELLOW + "El numero es valido: " + RESET, "NO")
        if n_existe:
            print(YELLOW + "Posibilidad que el numero exista: " + RESET, "SI")
        else:
            print(YELLOW + "Posibilidad que el numero exista: " + RESET, "NO")
    else:
        print(RED + "\n[!] No ha ingresado un numero de telefono")
except Exception as e:
    print(RED + "[!] La cadena proporcionada no parecía ser un número de teléfono.")