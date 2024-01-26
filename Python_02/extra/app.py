from game import Game
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Game")

    parser.add_argument('--count', type=int, required=True, help='number of array elements')    
    return parser.parse_args()

def main():
    args = parse_args()
    print(Game(count=args.count))    

if __name__ == '__main__':
    while True:
        main()
        opt = input("Enter 'q' To Exit : ")
        if opt == 'q':
            break
        else:
            continue
