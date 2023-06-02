from mrjob.job import MRJob

class MRSectorEmp(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        emplo = fields[0]
        sector = fields[1]

        yield emplo, sector

    def reducer (self, emplo, sector):
            sectors = set(sector)
            num_sector = len(sectors)
            
            yield emplo, num_sector
        
if __name__ == '__main__':
    MRSectorEmp.run()