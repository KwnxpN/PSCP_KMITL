'''ball'''
def main():
    '''calnumberoftimes'''
    count = -1
    height = float(input())
    while height >= 0.01:
        next_height = height*0.6
        height = next_height
        count += 1
    print(count)
main()
