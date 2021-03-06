# Datos #
sinonimos = {
    'abundante': 'mucho',
    'acabar': 'terminar',
    'advertir': 'notar',
    'alterado': 'nervioso',
    'altura': 'elevación',
    'amplificar': 'agrandar',
    'angustia': 'malestar',
    'anteojos': 'gafas',
    'apto': 'hábil',
    'armonía': 'calma',
    'avaro': 'amarrete',
    'barato': 'económico',
    'batalla': 'guerra',
    'bobo': 'necio',
    'boleto': 'billete',
    'bonito': 'hermoso',
    'cabello': 'pelo',
    'cálido': 'caliente',
    'calmar': 'atenuar',
    'cama': 'lecho',
    'camino': 'sendero',
    'cantina': 'bar',
    'castigar': 'sancionar',
    'cola': 'rabo',
    'combate': 'contienda',
    'cómodo': 'confortable',
    'comprar': 'adquirir',
    'comprender': 'entender',
    'constitución': 'estatuto',
    'crear': 'inventar',
    'cumbre': 'cima',
    'dadivoso': 'desprendido',
    'danza0': 'baile',
    'decir': 'pronunciar',
    'defecto': 'imperfección',
    'demente': 'loco',
    'desobediente': 'indisciplinado',
    'destruir': 'eliminar',
    'dicha': 'alegría',
    'ebrio': 'borracho',
    'economizar': 'ahorrar',
    'edén': 'paraíso',
    'educar': 'enseñar',
    'elegir': 'escoger',
    'elevar': 'subir',
    'embrujar': 'hechizar',
    'embuste': 'mentira',
    'enfurecer': 'enojar',
    'enigma': 'incógnita',
    'enseñanza': 'educación',
    'entero': 'completo',
    'escrito': 'nota',
    'escuchar': 'atender',
    'estudiante': 'alumno',
    'expresar': 'exponer',
    'extraño': 'raro',
    'fácil': 'sencillo',
    'fallecer': 'morir',
    'famoso': 'célebre',
    'fiel': 'leal',
    'flaco': 'delgado',
    'flecha': 'saeta',
    'formación': 'instrucción',
    'fotografía': 'retrato',
    'fragmento': 'pedazo',
    'frizar': 'congelar',
    'garaje': 'cochera',
    'generoso': 'dadivoso',
    'gigante': 'enorme',
    'gordo': 'obeso',
    'humildad': 'modestia',
    'humo': 'humareda',
    'idéntico': 'igual',
    'idioma': 'lengua',
    'iluminar': 'alumbrar',
    'importe': 'valor',
    'increíble': 'impresionante',
    'indicio': 'pista',
    'insolencia': 'arrogancia',
    'insulto': 'agravio',
    'inteligencia': 'sabiduría',
    'invariabilidad': 'uniformidad',
    'junta': 'delegación',
    'labor': 'trabajo',
    'lanzar': 'arrojar',
    'llano': 'plano',
    'lucha': 'pelea',
    'maestro': 'profesor',
    'magnate': 'poderoso',
    'magnífico': 'espléndido',
    'matar': 'asesinar',
    'matrimonio': 'boda',
    'miedo': 'pánico',
    'misericordia': 'piedad',
    'momento': 'instante',
    'monarca': 'rey',
    'montar': 'cabalgar',
    'naipe': 'baraja',
    'nombrar': 'designar',
    'norma': 'regla',
    'nunca': 'jamás',
    'oir': 'escuchar',
    'óleo': 'aceite',
    'orar': 'rezar',
    'página': 'hoja',
    'parar': 'detener',
    'partir': 'dividir',
    'paz': 'tranquilidad',
    'pedagogía': 'enseñanza',
    'pelo': 'cabello',
    'penumbra': 'tiniebla',
    'plano': 'llano',
    'poco': 'escaso',
    'posible': 'factible',
    'preocupación': 'inquietud',
    'previo': 'anterior',
    'profundo': 'hondo',
    'queja': 'lamento',
    'querer': 'pretender',
    'raro': 'extraño',
    'razón': 'motivo',
    'reposo': 'quietud',
    'robar': 'hurtar',
    'rostro': 'cara',
    'saber': 'conocer',
    'sabio': 'erudito',
    'sabroso': 'rico',
    'sanar': 'curar',
    'sano': 'saludable',
    'satisfacer': 'saciar',
    'silbar': 'pitar',
    'silueta': 'contorno',
    'soberbia': 'altanería',
    'sombra': 'oscuridad',
    'sumar': 'agregar',
    'tacaño': 'avaro',
    'tal vez': 'quizás',
    'tomar': 'beber',
    'transcribir': 'manuscribir',
    'triunfo': 'victoria',
    'valiente': 'aventurado',
    'valioso': 'preciado',
    'veloz': 'rápido',
    'vereda': 'senda',
    'vivir': 'habitar',
    'volver': 'regresar'
}

# Preguntas #
# 1
# Texto de ejemplo
texto = 'En la penumbra vio su silueta con anteojos y un bonito cabello y sintió miedo y ganas de volver a su casa'
texto += ' ' # Se agrega un espacio extra para simplificar la busqueda de palabras
modificado = '' # Aca guardaremos el texto modificado
palabra = '' # Aqui guardaremos las palabras para cambiar por su sinonimo
i = 0
while i < len(texto): # Recorremos el texto por indice
    if texto[i] == ' ': # Buscamos el espacio
        # Cuando encontremos el espacio, ya tenemos una palabra para buscar su sinonimo
        if palabra in sinonimos:  # Si la palabra tiene sinonimo
            modificado += sinonimos[palabra] + ' ' # Reemplazamos el texto
        else: # Si no tiene sinonimo
            modificado += palabra + ' ' # Mantenemos el texto con la palabra tal cual estaba en un principio
        palabra = ''
    else: # Mientras no sea espacio, simplemente concatenamos los caracteres a palabra
        palabra += texto[i]
    i += 1 # Indice del texto
print(modificado)
# 2
sinonimos_2 = {} # Simplemente cambiamos la llave por el valor del primero diccionario
for palabra in sinonimos:
    sinonimos_2[sinonimos[palabra]] = palabra
print(sinonimos_2)
