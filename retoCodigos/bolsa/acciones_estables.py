from mrjob.job import MRJob

class MRAccionesEstables(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        accion = fields[0]
        precio = float(fields[1])
        

        yield accion, precio


    def reducer (self, accion, precio):
            
            precios = list(precio)
            if all(precios[i] <= precios[i + 1] for i in range(len(precios) - 1)):
                resultado = "se mantuvo o subio"

                yield accion, resultado

        
if __name__ == '__main__':
    MRAccionesEstables.run()