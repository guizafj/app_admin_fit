class Cliente:
    def __init__(self,id=None, nombre=None, apellido=None, membresia=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__membresia = membresia

    @property
    def id(self):
        return self.__id    
    @id.setter
    def id(self,id):
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def membresia(self):
        return self.__membresia
    @membresia.setter
    def menbresia(self, membresia):
        self.__membresia =membresia

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}. Membresia: {self.membresia}'