EJER = {
    "ejercicio1":"sentadilla",
    "ejercicio2":"lagartija",
    "ejercicio3":"abdomilas",
    "ejercicio4":"levantamiento"
}

longitud = len(EJER)

def test_not_equal():
   ejercicio = "sentadilla"
   assert ejercicio == "patadas"

def test_equal():
   ejercicio = "abdominales"
   assert ejercicio == "abdominales"

def test_quantity():
   cantidad = 4
   assert cantidad == longitud

