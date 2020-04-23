def party_planner(cookies, people):
    """This function will calculate how many cookies each person will get in the party
    and also gives out leftovers
    ARGS:
    cookies: int, no of cookies is going to be baked
    people: int, no of people are attending this party_planner
    Returns:
    tuple of cookies per person and leftovers"""
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e:
        print('People cannot be zero. {}'.format(e))

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")
