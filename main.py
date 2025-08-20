class Dog:

    def __init__(self, dog_bark, dog_sniff):
        self.dog_bark = dog_bark
        self.dog_sniff = dog_sniff

    def bark(self):
        print(f'{self.dog_bark}!')

    def sniff(self):
        print(f'{self.dog_sniff}!')

class Cat:

    def __init__(self, cat_meow, cat_purr):
        
        self.cat_meow = cat_meow
        self.cat_purr = cat_purr

    def meow(self):
        print(f'{self.cat_meow}!')

    def purr(self):
        print(f'{self.cat_purr}!')


dog = Dog(dog_bark='Bark', dog_sniff='Sniff')
cat = Cat(cat_meow='Meow', cat_purr='Purr')

running = True

def dog_actions(current_running_state):
    command = input(f'What would you like the {animal} to do? bark or sniff. Type quit to exit: ')

    if command == 'quit':
        current_running_state = False
        return current_running_state
    
    if command == 'bark':
        dog.bark()
    
    elif command == 'sniff':
        dog.sniff()

    return current_running_state

def cat_actions(current_running_state):
    command = input(f'What would you like the {animal} to do? meow or purr. Type quit to exit: ')

    if command == 'quit':
        current_running_state = False
        return current_running_state

    if command == 'meow':
        cat.meow()

    elif command == 'purr':
        cat.purr()

    return current_running_state

while running:

    animal = input('What animal would you like? Dog or Cat. type quit to exit: ')

    if animal == 'quit':
        break

    if animal == 'dog':
        running = dog_actions(running)

    elif animal == 'cat':
        running = cat_actions(running)