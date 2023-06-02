from mrjob.job import MRJob

class MRUsuariosPeliculasPro(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        pelicula = fields[1]
        rating = float(fields[2])

        yield pelicula, (1, rating)

    def reducer (self, pelicula, valores):
            usuarios_totales = 0
            rating_total = 0

            for value in valores:
                 usuarios_totales += value[0]
                 rating_total += value[1]
                 
            average_rating = rating_total / usuarios_totales
            yield pelicula, (usuarios_totales, average_rating)
        
if __name__ == '__main__':
    MRUsuariosPeliculasPro.run()