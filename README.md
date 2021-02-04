# List.G4

Antlr4 List project - Transpiler from List to Python3

## List Language Definition
### types
The list language supports only two types:
- integers
- lists

A list can have many elements of different types (integers or others lists)

### Assignment
To create variables do:

```
a = 1
b = a + 2
c = [1, 2, a]
...
```

### Printing
You can print any literal value or variable using the print statement, in the form: `print X`

### Integer Operations
List supports only one operation for integers, the sum. To sum two or more integers just do:

```
1+2+5
```

### List Operations
List support two different operation over lists:

- sum, in the form: `[1,2,3] + [1,2,3]`, that gives you another list `[2, 4, 6]`
- concatenation, in the form: `[1,2,3] . [1,2,3]`, that gives you another list: `[1,2,3,1,2,3]`
