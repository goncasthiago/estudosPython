class DefaultList:
    def __init__(self,lista,valor_default):
        self.lista = []
        for item in lista:
            self.lista.append(item)
        self.valor_default = valor_default
    
    def __getitem__(self, i):
        try: 
            return self.lista[i]
           
        except:
            return self.valor_default
    
    def __len__(self):
        return len(self.lista)
    
    def append(self, valor):
        self.lista.append(valor)
        
    
    def remove(self, valor):
        
        self.lista.remove(valor)
        
        
    def insert(self, local, valor):
        
        self.lista.insert(local, valor)
        
        
    def extend(self, valor):
        
        self.lista.extend(valor)
        
    def pop(self,i):
        self.lista.pop(i)  
        
    def clear(self):
        self.lista.clear()
