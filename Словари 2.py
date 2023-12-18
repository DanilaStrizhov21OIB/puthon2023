def main():
    my_dict = {}
    for i in range(10, -6, -1):
        my_dict[i] = i ** i
    
    print(my_dict)

if __name__ == "__main__":
    main()
