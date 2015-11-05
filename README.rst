Modelos
=======

Rule
====

Define una regla de tipo "Campo igual a Valor"
Field define el campo del modelo de datos a verificar
Operator especifica un comparador definido como subclase en nabu.operators y registrado en nabu.operator.__init__
Value es el valor que se desea verificar en Field a través de Operator

El método evaluate toma como parametro al modelo de datos y ejecuta la lógica para devolver un Bool de acurdo a lo definido en field, operator y value

Action
======


Ruleset
=======
