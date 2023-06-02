from mrjob.job import MRJob

class MRDiaMenosPeliculas(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        fecha = fields[4]

        yield fecha , 1 


    def reducer (self, fecha, pelicula):
            peliculas_totales  = min(pelicula)

            yield fecha, peliculas_totales

        
if __name__ == '__main__':
    MRDiaMenosPeliculas.run()