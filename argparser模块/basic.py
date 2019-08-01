import argparse

def main():
 parser = argparse.ArgumentParser(description = 'How can i help you')
 parser.add_argument("-a", help = 'type: interager', type = int)
 parser.add_argument("-b", help = 'ypye: interager', type = int)
 args = parser.parse_args()
 print('The mutlipcation of this two numbers are %d '%(args.a * args.b))

if __name__ == '__main__':
 main()

