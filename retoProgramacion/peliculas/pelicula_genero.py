from mrjob.job import MRJob

class MRPeliculaGenero(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        
        
        pelicula = fields[1]
        rating = float(fields[2])
        genero = fields[3]
        
        yield genero, (rating, pelicula)

    def reducer(self, genero, values):
        mejor_pelicula = None
        mejor_rating = float('-inf')
        peor_pelicula = None
        peor_rating = float('inf')
        

        for value in values:
            rating, pelicula = value
            if rating > mejor_rating:
                mejor_rating = rating
                mejor_pelicula = pelicula

            if rating < peor_rating:
                peor_rating = rating
                peor_pelicula = pelicula
        
        yield genero, (mejor_pelicula, peor_pelicula) 


if __name__ == '__main__':
    MRPeliculaGenero.run()
