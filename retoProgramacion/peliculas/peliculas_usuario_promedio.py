from mrjob.job import MRJob

class MRPeliculasUsuarios(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        usuario = fields[0]
        pelicula = fields[1]
        rating = float(fields[2])

        yield usuario, (1, rating)

    def reducer (self, usuario, valores):
            peliculas = 0
            rating_total = 0

            for value in valores:
                 peliculas += value[0]
                 rating_total += value[1]
                 
            average_rating = rating_total / peliculas
            yield usuario, (peliculas, average_rating)
        
if __name__ == '__main__':
    MRPeliculasUsuarios.run()