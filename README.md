# Arithmetic Formatter

Los estudiantes de primaria a menudo organizan los problemas aritméticos de forma vertical para que sean más fáciles de resolver. Por ejemplo, "235 + 52" se convierte en:

  235
+ 52
-----
Cree una función que reciba una lista de cadenas que son problemas aritméticos y devuelva los problemas ordenados verticalmente y uno al lado del otro. La función debe tomar opcionalmente un segundo argumento. Cuando el segundo argumento se establece en Verdadero, se deben mostrar las respuestas.

Ejemplo
Llamada de función:

arreglo_aritmético(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Producción:

   32 3801 45 123
+ 698 - 2 + 43 + 49
----- ------ ---- -----
Llamada de función:

arreglo_aritmético(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], Verdadero)
Producción:

  32 1 9999 523
+ 8 - 3801 + 9999 - 49
---- ------ ------ -----
  40 -3800 19998 474
Normas
La función devolverá la conversión correcta si los problemas proporcionados tienen el formato adecuado; de lo contrario, devolverá una cadena que describe un error significativo para el usuario.

Situaciones que devolverán un error:
Si hay demasiados problemas suministrados a la función. El límite es cinco, cualquier cosa más devolverá: Error: Demasiados problemas.
Los operadores apropiados que aceptará la función son suma y resta. La multiplicación y la división devolverán un error. No será necesario probar otros operadores no mencionados en este punto. El error devuelto será: Error: el operador debe ser '+' o '-'.
Cada número (operando) solo debe contener dígitos. De lo contrario, la función devolverá: Error: los números solo deben contener dígitos.
Cada operando (también conocido como número a cada lado del operador) tiene un máximo de cuatro dígitos de ancho. De lo contrario, la cadena de error devuelta será: Error: los números no pueden tener más de cuatro dígitos.
Si el usuario proporcionó el formato correcto de los problemas, la conversión que devuelvas seguirá estas reglas:
Debe haber un solo espacio entre el operador y el más largo de los dos operandos, el operador estará en la misma línea que el segundo operando, ambos operandos estarán en el mismo orden proporcionado (el primero será el de arriba y el el segundo será el inferior).
Los números deben estar alineados a la derecha.
Debe haber cuatro espacios entre cada problema.
Debe haber guiones al final de cada problema. Los guiones deben correr a lo largo de cada problema individualmente. (El ejemplo anterior muestra cómo debería verse).
Desarrollo
Escribe tu código en aritmetic_arranger.py. Para el desarrollo, puede usar main.py para probar su función aritmetic_arranger(). Haga clic en el botón "ejecutar" y main.py se ejecutará.

***********************************************************************************

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
Development
Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.