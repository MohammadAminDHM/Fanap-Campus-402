from utils import make_array
from utils import identify

def game(count):
    array = make_array.array_generator(count)     
    return array, identify.judge(array)

def main():
    count = input("Enter Your Number : ")
    array, result = game(int(count))
    print(f'\nyour Count : {count:>2}\n')
    print(f'Your Random Array : {array}\n')
    print(f'You Are {result}')

if __name__ == '__main__':
    while True:
        main()
        opt = input("Enter 'q' To Exit : ")
        if opt == 'q':
            break
        else:
            continue

