import logging
import math
logging.basicConfig(level=logging.DEBUG)

def calculator(variables, operation):
    if operation == '+':
        result = sum(variables)
        logging.info("Dodajesz %s. Oto wynik: %s" % (variables, result))
    elif operation == '-':
        result = variables[0] - variables[1]
        logging.info("Odejmujesz %s. Oto wynik: %s" % (variables, result))
    elif operation == '*':
        result = math.prod(variables)
        logging.info("Mnożysz %s. Oto wynik: %s" % (variables, result))
    elif operation == '/':
        result = variables[0]/variables[1]
        logging.info("Dzielisz %s. Oto wynik: %s" % (variables, result))
    else:
        logging.info("Zly wybor dzialania")
        return(1)
    
if __name__ == "__main__":
    operation = input("Witaj w moim kalkulatorze. Podaj żądane działanie do wykonania wpisując odpowiedni znak tj. + - * albo /: ")
    variables_input = input("Teraz wpisz liczby, które chcesz objąć powyższym działaniem. Oddziel je przecinkiem. " 
                           "W przypadku dodawania i mnożenia to mogą być więcej niż dwie liczby: ")
    variables = variables_input.split(',')
    for i in range(len(variables)):
        
        variables[i] = float(variables[i])
    calculator(variables, operation)

    
