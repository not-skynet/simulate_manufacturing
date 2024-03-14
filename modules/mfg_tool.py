class tool:
    # parameters used in class
    loaded_parts = []
    available_spot = True
    
    def __init__(self, name, batch_size):
        self.name = name
        self.batch_size = batch_size
        

    def cycletime(self):
        print('hello')
    
    def load_part(self, part):
        self.part = part
        if len(self.loaded_parts) < self.batch_size:
            self.loaded_parts.append(part)
            print(f'{self.part} loaded')
        if len(self.loaded_parts) >= self.batch_size:
            self.available_spot = False
            print(f'{self.name} system full')

    def list_loaded_parts(self):
        print(self.loaded_parts)

    def check_available_slot(self):
        return self.available_spot

class clock:
    x = 5