Modelos
=======

Rule
====

Define una regla de tipo "Campo igual a Valor"

- **Field** define el campo del modelo de datos a verificar
- **Operator** especifica un comparador definido como subclase en nabu.operators y registrado en nabu.operator.__init__
- **Value** es el valor que se desea verificar en Field a través de Operator

El método evaluate toma como parametro al modelo de datos y ejecuta la lógica para devolver un Bool de acurdo a lo definido en field, operator y value

Action
======

Define una acción a realizar

- **provider** especifica el proveedor para realizar la acción. El mismo es una instancia de nabu.providers.BaseProvider y se regstra en nabu.providers.__init__
- **data** Json especificando los datos requeridos para cada proveedor (varia según el tipo de Provider)

El método **execute** toma como parámetro un contexto. En geral ctx va a ser igual al objeto evaluado por **Rule**. Ctx (externo) y data (interno) son las dos fuentes de datos para un provider


Ruleset
=======

Integra varias reglas (AND) y las víncula con acciones.

Atributos:
- **when_creating** si es verdadero el Ruleset se evaluá solo si el objeto se creó al momento de evaluar Rule
- **content_type** FK a ContentType. Si se define el Ruleset se evalua sólo si el objeto a evaluar es una instancia de content_type.

Métodos:
- **evaluate** recorre todas las instancias de **Rule** vinculadas y espera que todas den True. Devuelve un Bool
- **run_acctions** recorre todas las acciones vinculadas y las ejecuta.
- **evaluate_all** (class method) Evalua todas las instancias de Ruleset. Toma los mismos parámetros que un event listener de Django (cls, model, instance, created)
