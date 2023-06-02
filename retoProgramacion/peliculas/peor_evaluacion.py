from mrjob.job import MRJob

class MRPeorEvaluacion(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 
        
        rating = float(fields[2])
        fecha = fields[4]

        yield fecha, rating

    def reducer (self, fecha, ratings):
            total_ratings = list(ratings)
            average_rating = sum(total_ratings)/ len(total_ratings)
            yield fecha, average_rating
        
if __name__ == '__main__':
    MRPeorEvaluacion.run()