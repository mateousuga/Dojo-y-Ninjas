from flask_app.config.mysqlconnection import connectToMySQL

from .ninjas import Ninja

class Dojo:
    
    def __init__(self, data):
        #data = {id: 1, name: colombia, created_at:0000-00-00, updated_at:0000-00-00}
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        #una lista con todos los ninjas 
        self.ninjas = []
    
    @classmethod
    def save(cls, formulario):
        #formulario = {name: Colombia}
        query = "INSERT INTO dojos(name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        #results = [{id: 1, name: "colombia", created_at:0000-00-00, updated_at:0000-00-00}
        # {id: 2, name: "Perú", created_at:0000-00-00, updated_at:0000-00-00}
        # {id: 3, name: "Mexico", created_at:0000-00-00, updated_at:0000-00-00}]
        dojos = []
        for d in results:
            #i = {id: 1, name: "colombia", created_at:0000-00-00, updated_at:0000-00-00}
            dojos.append(cls(d)) #1. cls(i)->crea una instancia de Dojo en base al diccionario
                                #2. dojos.append agrega la instacia a la lista de dojos
        return dojos
    
    @classmethod
    def get_dojo_with_ninja(cls, data):
        #data = {id: 1}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        
        dojo = cls(results[0]) #creamos una instancia  de dojo
        
        for row in results:
            #row = {diccionario con todas las columnas de dojo y todas las columnas de ninja}
            ninja_diccionario = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'dojo_id': row['dojo_id'],}
            
            intancia_ninja = Ninja(ninja_diccionario)
            dojo.ninjas.append(intancia_ninja) 
        return dojo