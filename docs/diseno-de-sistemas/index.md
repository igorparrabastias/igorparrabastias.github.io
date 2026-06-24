# Diseño de sistemas

Apuntes propios sobre **diseño de sistemas a gran escala**: cómo se piensa, dimensiona y construye software que debe atender a millones de usuarios sin caerse. La idea no es memorizar arquitecturas "correctas" —no existen—, sino entrenar un método: partir de requisitos, estimar la escala, elegir piezas (servicios, bases de datos, colas, caché, CDN) y razonar los *trade-offs* de cada decisión.

Cada caso de estudio sigue la misma plantilla para que sea fácil compararlos:

1. **Requisitos** funcionales, no funcionales y escala estimada.
2. **Estimaciones de capacidad** (usuarios, QPS, almacenamiento, ancho de banda).
3. **API principal** con los endpoints clave.
4. **Modelo de datos** y dónde vive cada entidad.
5. **Arquitectura de alto nivel** con un diagrama por capas.
6. **Componentes y decisiones clave**, justificadas.
7. **Cuellos de botella y trade-offs**.

> [!NOTE]
> Estos son apuntes personales de estudio. El temario y varios casos están inspirados en *Grokking the System Design Interview*, el repositorio **system-design-primer** y el libro *Designing Data-Intensive Applications* de Martin Kleppmann; el contenido está **reescrito por completo** y ampliado. Las fuentes se citan al final de cada página.

## Casos de estudio

<div class="grid cards" markdown>

-   :material-car: __Uber__

    ---

    Emparejar pasajeros y conductores en tiempo real: geoíndice, sharding
    geográfico, despacho y cálculo de ETA a escala global.

    [:octicons-arrow-right-24: Entrar](uber.md)

-   :material-television-play: __Netflix__

    ---

    Streaming de video a cientos de millones: CDN propia (Open Connect),
    streaming adaptativo, transcodificación masiva y recomendaciones.

    [:octicons-arrow-right-24: Entrar](netflix.md)

-   :material-fire: __Tinder__

    ---

    Descubrimiento y emparejamiento geoespacial, *swipes* a gran escala y
    feed de candidatos.

    [:octicons-arrow-right-24: Entrar](tinder.md)

-   :material-instagram: __Instagram__

    ---

    Publicación de fotos, generación de *feed* y *fan-out*, almacenamiento de
    objetos y CDN de imágenes.

    [:octicons-arrow-right-24: Entrar](instagram.md)

-   :material-whatsapp: __WhatsApp__

    ---

    Mensajería en tiempo real, entrega garantizada, presencia y cifrado
    extremo a extremo a escala de miles de millones.

    [:octicons-arrow-right-24: Entrar](whatsapp.md)

-   :material-video: __Zoom__

    ---

    Videoconferencia multipunto, SFU/MCU, baja latencia y selección de
    servidores cercanos.

    [:octicons-arrow-right-24: Entrar](zoom.md)

-   :material-shield-key: __Auth0__

    ---

    Identidad como servicio: OAuth2/OIDC, tokens, multi-tenant y verificación
    de credenciales a alta tasa.

    [:octicons-arrow-right-24: Entrar](auth0.md)

</div>

## Conceptos transversales

Las piezas que se repiten en casi todos los casos —consistent hashing, balanceo de carga, colas, estrategias de caché, teorema CAP— viven en una página aparte para no repetirlas en cada sistema:

[:octicons-arrow-right-24: Conceptos y building blocks](conceptos.md)

## Referencias

- [Grokking the System Design Interview — DesignGurus](https://www.designgurus.io/course/grokking-the-system-design-interview)
- [system-design-primer — Donne Martin (GitHub)](https://github.com/donnemartin/system-design-primer)
- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly, 2017.
