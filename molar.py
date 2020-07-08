#calculadora
#importing librarys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("massamolar","-MM", type=int, help="massa molar")
parser.add_argument("concentração","-c", type=int, help="concentração grama/litro")
args = parser.parse_args()

def molaridade (massamolar, concentração):
    molaridade = concentração/massamolar
    return molaridade
if __name__ == '__main__':
    print molaridade(args.massamolar, args.concentração)