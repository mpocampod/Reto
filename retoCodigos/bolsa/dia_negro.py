from mrjob.job import MRJob

class MRDiaNegro(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        accion = fields[0]
        precio = float(fields[1])
        fecha = fields[2]


        yield fecha, (accion, precio)


    def reducer (self, fecha, valor):
            min_precio_accion = []
            min_precio = float('inf')
            
            for accion, precio in valor:
                 if precio < min_precio:
                    min_precio = precio
                    min_precio_accion = [accion]
                 elif precio == min_precio:
                    min_precio_accion.append(accion)
            
            yield fecha, min_precio_accion

        
if __name__ == '__main__':
    MRDiaNegro.run()