from mrjob.job import MRJob

class MRPrecioFecha(MRJob):

    def mapper (self, _, line):
        fields = line.split(',') 

        accion = fields[0]
        precio = float(fields[1])
        fecha = fields[2]

        yield accion, (precio, fecha)


    def reducer (self, accion, precio):
            
            precios = sorted(precio, key=lambda x: x[0])
            min_precio= precios[0]
            max_precio= precios[-1]
            
            yield accion, (min_precio, max_precio)

        
if __name__ == '__main__':
    MRPrecioFecha.run()