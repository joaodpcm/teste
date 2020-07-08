#calculadora
#importing librarys
import argparse

parser = argparse.ArgumentParser(description='calcular molaridade')
parser.add_argument("-MM","--massamolar", type=int, help="massa molar")
parser.add_argument("-c","--concentração", type=int, help="concentração grama/litro")
args = parser.parse_args()

def molaridade (massamolar, concentração):
    molaridade = concentração/massamolar
    return molaridade
if __name__ == '__main__':
    print molaridade(args.massamolar, args.concentração)