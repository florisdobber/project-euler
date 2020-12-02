def main():
    pyramid = read_txt_file("resources/p67.txt")

    for row in range(len(pyramid)-2, -1, -1):
        for index in range(len(pyramid[row])):
            best_choice = max(pyramid[row+1][index], pyramid[row+1][index+1])
            pyramid[row][index] += best_choice

    print(pyramid[0][0])

def read_txt_file(path):
    f = open(path, "r")
    pyramid = [line.replace("\n", "").split(" ") for line in f]
    pyramid = [[int(n) for n in line] for line in pyramid]
    f.close()
    return pyramid
    

main()