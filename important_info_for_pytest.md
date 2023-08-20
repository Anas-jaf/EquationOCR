Dictionary Data to LaTeX Equations

Here's a summary of the dictionary data you provided along with their corresponding LaTeX representations:

Addition:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "1"
            },
            {
                "type": "const",
                "value": "1"
            }
        ],
        "type": "add"
    }
}
```
LaTeX: 1+11+1

Subtraction:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "1"
            },
            {
                "type": "const",
                "value": "1"
            }
        ],
        "type": "sub"
    }
}
```
LaTeX: 1−11−1

Multiplication:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "2"
            },
            {
                "type": "const",
                "value": "3"
            }
        ],
        "type": "mul"
    }
}
```
LaTeX: 2×32×3

Division:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "1"
            },
            {
                "type": "const",
                "value": "2"
            }
        ],
        "type": "div"
    }
}
```
LaTeX: 1221​

Fraction:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "3"
            },
            {
                "type": "const",
                "value": "4"
            }
        ],
        "type": "frac"
    }
}
```
LaTeX: 3443​

Power:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            },
            {
                "type": "const",
                "value": "2"
            }
        ],
        "type": "pow"
    }
}
```
LaTeX: x2x2

Equals:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "5"
            },
            {
                "type": "const",
                "value": "6"
            }
        ],
        "type": "equals"
    }
}
```
LaTeX: 5=65=6

Negative Value:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "10"
            }
        ],
        "type": "negative"
    }
}
```
LaTeX: −10−10

Absolute Value:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "abs"
    }
}
```
LaTeX: ∣x∣∣x∣

Exponential Function:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "exp"
    }
}
```
LaTeX: exex

Function Call:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "f"
            },
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "function"
    }
}
```
LaTeX: f(x)f(x)

Derivative:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            },
            {
                "type": "const",
                "value": "1"
            }
        ],
        "type": "derivation"
    }
}
```
LaTeX: ddx(x)dxd​(x)

Integral:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "integral"
    }
}
```
LaTeX: ∫x dx∫xdx

Definite Integral:
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "1"
            },
            {
                "type": "const",
                "value": "2"
            },
            {
                "type": "const",
                "value": "3"
            },
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "definiteintegral"
    }
}
```
LaTeX: ∫12x dx∫12​xdx

Definite Summation (Sigma):
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            },
            {
                "type": "const",
                "value": "2"
            },
            {
                "type": "const",
                "value": "1"
            }
        ],
        "type": "definitesigma"
    }
}
```
LaTeX: ∑x=21x∑x=21​x

Derivative with Respect to Different Variable:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            },
            {
                "type": "var",
                "value": "y"
            }
        ],
        "type": "derivation_diff"
    }
}
```
LaTeX: ddy(x)dyd​(x)

Differential:
```python
{
    "node": {
        "children": [
            {
                "type": "var",
                "value": "x"
            }
        ],
        "type": "differential"
    }
}
```
LaTeX: dxdx

Derivative Prime:
```python
{
    "node": {
        "type": "derivationprime"
    }
}
```
LaTeX: y′y′

Variable anan​:
```python
{
    "node": {
        "type": "var",
        "value": "a_n"
    }
}
```
LaTeX: anan​

Binomial Coefficient (Choose):
```python
{
    "node": {
        "children": [
            {
                "type": "const",
                "value": "1"
            },
            {
                "type": "const",
                "value": "2"
            }
        ],
        "type": "choose"
    }
}
```
LaTeX: (12)(21​)