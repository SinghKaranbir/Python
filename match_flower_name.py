def create_dict(filename):
    if not filename:
        return None

    flowers_dict = {}
    with open(filename) as file:
        for line in file:
            flower = line.split(':')
            flowers_dict[flower[0]] = flower[1]
    return flowers_dict


def main():
    first_name, last_name = None, None
    try:
        user_input = input("Enter your first name [space] last name: ").split()
        first_name = user_input[0]
        last_name = user_input[1]
    except ValueError as e:
        print("Please enter your valid first name and last name {}".format(e))

    flower_dict = create_dict('files/flowers.txt')
    if not flower_dict:
        print('Something wrong has happened, please check me')
        return

    if first_name[0].upper() in flower_dict:
        print(flower_dict[first_name[0].upper()])
    else:
        print('No flower found with start letter as same as user\'s first name')

if __name__ == '__main__':
    main()
