from mrjob.job import MRJob

class MRSalaryEmp(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        emplo = fields[0]
        salary = float(fields[2])

        yield emplo, salary

    def reducer (self, emplo, salary):
            total_salaries = list(salary)
            average_salaries = sum(total_salaries) / len(total_salaries)
            yield emplo, average_salaries
        
if __name__ == '__main__':
    MRSalaryEmp.run()