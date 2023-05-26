from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def index(): 
        return "Hola :)"

@app.get("/Conversor_CaF/{C}")
def conversorCaf(C):
       try: 
                C=float(C)
                TF=C*(9/5) + 32
                return f"La temperatura es de {TF} grados farenheit"
            except: 
                     return "Entrada invalida"
