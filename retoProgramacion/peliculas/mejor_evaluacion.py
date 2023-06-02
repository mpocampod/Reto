from mrjob.job import MRJob

class MRPeorEvaluacion(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 
        
        rating = float(fields[2])
        fecha = fields[4]

        yield fecha, rating

    def reducer (self, fecha, ratings):
            total_ratings = max(ratings)

            yield fecha, total_ratings
        
if __name__ == '__main__':
    MRPeorEvaluacion.run()