### BUGS REPORT ### (en español para clarificar mejor)

ESTA ES UNA LISTA CON TODOS LOS PROBLEMAS (LA MAYORÍA SOLUCIONABLES), A
LOS QUE NO HEMOS ENCONTRADO UNA SOLUCIÓN CLARA.

##PROBLEMAS SIN RESOLVER(BUGS)

    
    -BUG CON SHOVEL: LA PLATAFORMA DE ABAJO "DESAPARECE" PERO SE SIGUE DIBUJANDO
    -A VECES LA ANIMACIÓN DEL LEMMING CAMINANDO CUANDO CAMBIA DE DIRECCIÓN NO SE IMPLEMENTA CORRECTAMENTE
    -BUG CON EL SONIDO DEL UMBRELLA(POCOS CANALES DE SONIDO)
    
    -BUG AL ACTIVAR EL ZAWARUDO: LOS LEMMINGS ES POSIBLE QUE SE ACUMULEN EN LA PUERTA
    AL IR GENERÁNDOSE AUTOMÁTICAMENTE MIENTRAS EL TIEMPO ESTÁ PARADO

# BUGS ENCONTRADOS EN EL SPRINT 1

NINGUNO

NOTA: Una cosa que no se especificó en el pdf fue la posibilidad bastante alta de generar niveles imposibles debido a la aleatoridad de los mismos.

# BUGS ENCONTRADOS EN EL SPRINT 2

1. BUG CUANDO UN LEMMING LLEGA AL EXTREMO DERECHO DE LA PANTALLA CUANDO ESTÁ EN UNA SUELO FLOTANTE: La plataforma de la derecha del todo no la detecta, por lo que el lemming, en vez de caerse, rebota.
    ORIGEN DEL PROBLEMA: el lemming rebota cuando su posicion x es igual a WIDTH-16, por lo que da igual que haya una plataforma debajo o no, rebotará igual. No se puede poner sólo WIDTH porque el programa crashea.

2. BUG CUANDO UN LEMMING LLEGA AL EXTREMO IZQUIERDO DE UN SUELO (conjunto de plataformas): LA PLATAFORMA DEL EXTREMO NO LA DETECTA Y LA ATRAVIESA, SIN EMBARGO LAS HERRAMIENTAS COMO LOS PARAGUAS Y LAS ESCALERAS FUNCIONAN CORRECTAMENTE SI SE PONEN EN SU LUGAR ADECUADO.
    ORIGEN DEL PROBLEMA: la posición del lemming funciona en función de su valor x e y, que son en realidad la esquina superior izquierda del sprite. Por eso, cuando el lemming avanza hacia la izquierda va detectando según esa posición que se contiene en las celdas adyacentes, y en cuanto hay 1 sólo pixel del lemming en la celda de su izquierda pasa a detectar cosas distintas, cosa que cuando va hacia la derecha no ocurre. Por lo tanto, automáticamente detecta que debajo no tiene una plataforma y atraviesa la plataforma real, pero como el lemming está un pixel desplazado hacia la izquierda en la celda siguiente detecta correctamente el paraguas. Una potencial solución sería que detectase lo que hay en su celda abajo y derecha para que así no la atravesase.

# BUGS ENCONTRADOS EN EL SPRINT 3

BÁSICAMENTE EL BUG 2 DEL SPRINT 2, APLICADO A LAS ESCALERAS CUANDO LAS DETECTA YENDO HACIA LA IZQUIERDA: EN CUANTO UN PIXEL DEL LEMMING ESTÁ EN LA CELDA DE LA ESCALERA, LA DETECTA Y SUBE. ADEMÁS, SI SE PONEN VARIAS ESCALERAS SEGUIDAS, LA ÚLTIMA NO LA DETECTA POR LA MISMA RAZÓN. ADEMÁS, DA IGUAL EN QUÉ DIRECCIÓN VAYA EL LEMMING, QUE SIEMPRE DETECTARÁ UNA LADDERD DE CUALQUIER DIRECCIÓN, LO QUE PROVOCA MÁS BUGS A LA HORA DE SUBIR.

Las escaleras teóricamente funcionan, pero cuando suben y se encuentran con una plataforma, en vez de ponerse a caminar, se mueren. Eso no ocurre, sin embargo, cuando se pone una escalera para bajar: ahí, el lemming no se muere al llegar al suelo objetivo.



# BUGS ENCONTRADOS EN EL SPRINT 4

1. BUG CUANDO UN LEMMING CHOCA CON UN BLOCKER TOOL CUANDO VA CAMINANDO A SU IZQUIERDA: EL LEMMING FUNCIONA CORRECTAMENTE, ACTUANDO COMO UN OBSTÁCULO, PERO LA BLOCKER TOOL DESAPARECE. 
    ORIGEN DEL PROBLEMA: De nuevo, la detección de plataformas del lemming cuando va caminando hacia la izquierda, que hace que en cuanto un pixel toque la blocker tool se cambia el sprite de esa misma celda por el sprite del Blocker Lemming

2. BUG CUANDO UN LEMMING TOCA UN BLOCKER TOOL CUANDO ESTÁ CAYENDO; ES DECIR TAMBIÉN, CUANDO ESTÁ CAYENDO 
ENCIMA DE UN BLOCKER LEMMING YA PUESTO: SE TRANSFORMA EN OTRO BLOCKER LEMMING SUPERPUESTO ENCIMA DEL OTRO.
Esto no es un bug en sí, sino más bien un fallo de las reglas del juego en sí.

NOTA: Otra cosa que no es un bug, ya que no se especificó en el pdf, pero si un lemming se queda en modo blocker, ya no
puede salir de ahí nunca, y por lo tanto la partida nunca se va acabar, ya que siempre quedará algún lemming sin salvar vivo. Y también, si por algún casual se quiere eliminar el blocker tool ya usado (cosa un poco inútil), el blocker lemming seguirá ahí parado.

3. BUG EN LA ANIMACIÓN DE MOVIMIENTO DE LOS LEMMINGS: CUANDO CAMBIÁN DE DIRECCIÓN HACIA LA IZQUIERDA, HAY VECES QUE SE DIBUJAN LOS SPRITES DE CUANDO CAMINAN HACIA LA DERECHA (EFECTO MICHAEL JACKSON)
    NO SABEMOS EL ORIGEN DEL PROBLEMA

# BUGS ENCONTRADOS EN EL SPRINT 5

1. BUG CON LA PALA: CUANDO SE USA LA PALA, EL SPRITE DE LA PLATAFORMA DE ABAJO NO SE QUITA. SIN EMBARGO, LA CELLCLASS SI, PUESTO QUE CAMBIA A Destroyed_Platform, PERMITIENDO A LOS LEMMINGS ATRAVESARLA Y BAJAR MIENTRAS SE CAEN.
    ORIGEN DEL PROBLEMA: Las plataformas se crean en el __init__(). Suponemos que al inicializarlas ahí y no en el update() se quedan ahí para siempre los sprites (también ocurre con las entry gates y las exit gates), y puedes poner cosas en esas cells, pero no se verán
    POTENCIAL SOLUCIÓN: Inicializar las plataformas en el update en vez del __init__()

Nota: no son un bug como tal, pero el ZAWARUDO (parar el tiempo), al no pararse el tiempo del juego como tal, sino el movimiento de los lemmings, estos se siguen generando, por lo que a veces es posible que los lemmings generados se superpongan, pero no ocurre siempre

Nota: también otra cosa que no es un bug es que a veces se cortan los sonidos que suenan en el juego, pero ocurre porque pyxel tiene pocos canales de sonido y no permite que suenen demasiadas cosas a la vez.







