# Referencia: Google Cloud `nodejs-docs-samples` 🔵

Esta página documenta una **referencia externa** que estudié, no código propio. Se trata de `nodejs-docs-samples`, la colección oficial de ejemplos de Node.js de **Google Cloud Platform**.

> [!NOTE]
> **Crédito y origen.** `nodejs-docs-samples` es propiedad de **Google LLC / Google Cloud Platform** y se publica bajo licencia **Apache 2.0**. Yo no soy autor de este código: lo clamé como material de referencia para aprender a desplegar y operar servicios de Google Cloud con Node.js. Todo el mérito es de sus autores originales.
>
> - Repositorio original: <https://github.com/GoogleCloudPlatform/nodejs-docs-samples>

## Qué es

Es el repositorio oficial donde Google reúne ejemplos ejecutables de Node.js para **prácticamente todos sus productos cloud**. Cada subcarpeta es un caso de uso autocontenido con su `package.json`, sus tests y su README. Es, básicamente, la documentación de Google Cloud convertida en código que puedes correr.

## Por qué lo estudié

Leer documentación está bien, pero los ejemplos *reales y probados* enseñan mucho más rápido. Usé este repo como **mapa de referencia** para entender cómo se estructura una aplicación Node desplegable en Google Cloud: cómo se autentica contra los servicios, cómo se definen las funciones serverless, cómo se contenedoriza un servicio, etc. Cuando dudaba de "¿cómo se hace X en GCP con Node?", aquí casi siempre había una respuesta funcionando.

## Áreas que me sirvieron de referencia

La colección cubre, entre muchas otras, estas áreas (cada una en su carpeta):

- **App Engine** (`appengine/`) — desplegar aplicaciones web en la plataforma PaaS de Google.
- **Cloud Functions** (`functions/`) — funciones serverless dirigidas por eventos.
- **Cloud Run** (`run/`) — servicios en contenedores que escalan a cero.
- **Cloud Tasks**, **Cloud SQL**, **Datastore**, **Workflows**, **Eventarc**, **Monitoring**, **Healthcare**, **Memorystore**, **Endpoints**, **Composer**... y un largo etcétera.

## Cómo encaja en estos apuntes

Mientras que mis páginas de [Event Loop](event-loop.md) y [Fundamentos](fundamentos.md) miran *hacia dentro* (cómo funciona el runtime), esta referencia mira *hacia fuera*: cómo se lleva Node.js a producción en una nube real. Es el puente entre "entiendo Node" y "sé desplegar Node".

> [!TIP]
> Por respeto a la licencia y a los autores, aquí **no embebo** su código. Si quieres verlo, ve directo al repositorio original de Google enlazado arriba: está mucho mejor mantenido allí. 😉
