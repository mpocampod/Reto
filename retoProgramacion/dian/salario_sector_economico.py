from mrjob.job import MRJob

class MRSalarySE(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        sector = fields[1]
        salary = float(fields[2])

        yield sector, salary

    def reducer (self, sector, salary):
            total_salaries = list(salary)
            average_salaries = sum(total_salaries) / len(total_salaries)
            yield sector, average_salaries

        
if __name__ == '__main__':
    MRSalarySE.run()