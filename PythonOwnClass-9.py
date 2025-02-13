valid_sport_types = [
    'Football', 'Basketball', 'Baseball', 'Soccer', 'Tennis', 'Volleyball', 'Cricket',
    'Rugby', 'Hockey', 'Golf', 'Swimming', 'Cycling', 'Boxing', 'MMA', 'Running',
    'Skiing', 'Snowboarding', 'Skating', 'Surfing', 'Badminton', 'Table Tennis',
    'Handball', 'Squash', 'Rowing', 'Kayaking', 'Canoeing', 'Climbing',
    'Mountaineering', 'Horse Racing', 'Equestrian', 'Wrestling', 'Judo', 'Karate',
    'Taekwondo', 'Fencing', 'Archery', 'Shooting', 'Gymnastics', 'Figure Skating',
    'Weightlifting', 'Powerlifting', 'Bodybuilding', 'Triathlon', 'Marathon',
    'Sailing', 'Diving', 'Water Polo', 'Bobsleigh', 'Luge', 'Skeleton', 'Biathlon',
    'Curling', 'Ice Hockey', 'Lacrosse', 'Netball', 'Softball', 'Field Hockey',
    'Polo', 'Rodeo', 'Motorsport', 'Auto Racing', 'Motorcycle Racing',
    'BMX', 'Skateboarding', 'Roller Skating', 'Parkour', 'Cheerleading',
    'Dance', 'Aerobics', 'CrossFit', 'Fishing', 'Hunting', 'Darts',
    'Snooker', 'Billiards', 'Bowling', 'Petanque', 'Shuffleboard',
    'Ultimate Frisbee', 'Disc Golf', 'Kickboxing', 'Muay Thai', 'Brazilian Jiu-Jitsu',
    'Capoeira', 'Sambo', 'Sumo', 'Paddleboarding', 'Wakeboarding', 'Windsurfing',
    'Kitesurfing', 'Base Jumping', 'Paragliding', 'Skydiving', 'Hang Gliding', 'Gliding',
    'Model Aeroplane', 'Bocce', 'Croquet', 'Jai Alai', 'Sepak Takraw', 'Kabaddi'
]

sport_types = []


class Sport:
    def __init__(self, type=None):
        if type and type in valid_sport_types:  #In Python, any non-zero number,
            # non-empty string, non-empty list, etc., are considered True.
            # Conversely, None, 0, '' (empty string), [] (empty list), etc., are considered False.
            self.type = type
            sport_types.append(type)
        else:
            self.type = None

    def display_sport_type(self):
        print(sport_types)
        if len(sport_types) != 0:
            print('\nList of Sports:')
            print('-' * 35)
            print('{:<10} {:<10}'.format('ID', 'Name'))
            for id, sport in enumerate(sport_types, start=1):
                print(f'{id}.         {sport:<10}')
            print('-' * 35)
            print(f'Total number of sports: {len(sport_types)}')
        else:
            print('\nThe list of sports is empty!')

    def add_sport_type(self):
        add_sport = input('\nType in a sport type to add: ').capitalize()
        if add_sport in valid_sport_types:
            if add_sport in sport_types:
                print(f'\n"{add_sport}" is already in the list of Sports!')
            elif add_sport not in sport_types and add_sport.isalpha():
                sport_types.append(add_sport)
                print(f'"{add_sport}" sport type successfully added!')
            else:
                print('\nError: invalid symbol!')
            self.display_sport_type()
        else:
            print('\nError: invalid symbol!')

    def delete_sport_type(self):
        self.display_sport_type()
        delete_sport = input('\nType in a type of sport to delete: ').capitalize()
        if delete_sport in sport_types:
            sport_types.remove(delete_sport)
            print(f'"{delete_sport}" is successfully deleted!')
        else:
            print('\nNo such type of sport found!')
        self.display_sport_type()

    def replace_sport_type(self):
        self.display_sport_type()
        replace_sport = input('\nType in a type of sport to replace: ').capitalize()
        if replace_sport in sport_types:
            sport_types.remove(replace_sport)
            self.add_sport_type()
        else:
            print('\nNo such type of sport found!')
        self.display_sport_type()


while True:
    user = input('\nType in:\n'
                 '"1" To see the list of sports\n'
                 '"2" To add a new type of sport\n'
                 '"3" To delete a type of sport\n'
                 '"4" To replace a type of sport\n'
                 '"0" To exit\n'
                 '::: ')
    if user == '1':
        Sport().display_sport_type()
    elif user == '2':
        Sport().add_sport_type()
    elif user == '3':
        Sport().delete_sport_type()
    elif user == '4':
        Sport().replace_sport_type()
    elif user == '0':
        print('\nExit')
        break
    else:
        print('\nError: invalid option!')
