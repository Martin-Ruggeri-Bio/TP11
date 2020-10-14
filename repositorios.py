class Repositorios():
    palabraList2 = {'animales': {'abeja', 'aguila', 'araña', 'avispa', 'ballena', 'bisonte', 'bufalo', 'burro', 'caballo',
                                 'camello', 'cangrejo', 'canguro', 'caracol', 'cebra', 'cerdo', 'chimpance', 'ciervo',
                                 'cocodrilo', 'elefante', 'escarabajo', 'escorp', 'foca', 'gallina', 'gallo', 'gato',
                                 'hipopotamo', 'hormiga', 'jabali', 'jirafa', 'leon', 'loro', 'mosca', 'mosquito', 'oveja',
                                 'perdiz', 'perro', 'pollo', 'serpiente', 'tigre', 'toro', 'tortuga', 'vaca', 'zorro'},
                     'frutas': {'Arandano', 'Frambuesa', 'Fresa', 'Mandarina', 'Naranja', 'Limon', 'Pomelo', 'Melon', 'Sandía',
                                'Plátano', 'palta', 'Coco', 'Kiwi', 'Mango', 'Papaya', 'Piña', 'Uva', 'Cereza', 'Ciruela', 'Higo',
                                'Manzana', 'Melocotón', 'Pera', 'Almendra', 'Avellana', 'Castaña', 'Nuez', 'Mani'},
                     'verduras': {'zanahoria', 'brócoli', 'espárragos', 'coliflor', 'maíz', 'pepino', 'berenjena', 'pimiento',
                                  'lechuga', 'champiñones', 'cebolla', 'patata', 'calabaza', 'tomate', 'remolacha', 'guisantes',
                                  'calabacín', 'rábano', 'batata', 'alcachofa', 'puerro', 'repollo', 'apio', 'chile', 'ajo', 'cilantro',
                                  'perejil', 'eneldo', 'romero', 'orégano', 'canela', 'azafrán', 'frijol', 'garbanzo', 'lenteja'},
                     'electrodomestico': {'Plancha', 'Lavarropas', 'Exprimidor', 'Licuadora', 'Batidora', 'Sandwichera',
                                          'Tostadora', 'Horno', 'Microondas', 'Lavaplatos', 'Heladera', 'Cocina', 'Ventilador',
                                          'Cafetera', 'Teléfono', 'Freezer', 'Multiprocesadora'},
                     'paises': {'México', 'Argentin', 'España', 'Colombia', 'Francia', 'Brasil', 'Italia', 'Perú', 'Japón', 
                                'Alemania', 'Inglaterra', 'Canada', 'China', 'Rusia', 'Ecuador', 'Australia', 'Egipto', 'Grecia',
                                'Cuba', 'India', 'Israel', 'Sudafrica', 'Madagascar', 'Haiti'}}
    palabraList = dict()
    jugadorList = dict()
    palabraElegida = "torta"
    intentos = 0
    aciertos = 0
    partida_anterior = {}
