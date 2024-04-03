# NumerosATexto 📚

NumerosATexto es una pequeña biblioteca escrita en Python que convierte números en su representación textual en español.

## Uso 🖥️

```python
from numero_a_texto import numero_a_texto

print(numero_a_texto("12345"))  # Salida: "doce mil trescientos cuarenta y cinco pesos"
```

La función `numero_a_texto` toma un número como una cadena y devuelve su representación textual en español.

La función numero_a_texto toma un número como una cadena y devuelve su representación textual en español. El rango de uso es de 0.9999999 a 9999999.9999999.

**Revisa el archivo [Ejemplos](/ejemplos.py) para ver las salidas que ofrece esta biblioteca** 📝

## Contribuir 🚀

¡Siéntete libre de contribuir! Puedes abrir un problema o enviar una solicitud de extracción con tus mejoras.

## Errores a corregir ❗

Si encuentras algún error, por favor, háznoslo saber abriendo un problema en el repositorio. Uno de los errores conocidos es cuando se intenta ejecutar con el número "1", donde el output esperado es "Uno" pero el output real es "Un".

