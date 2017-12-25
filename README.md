# Método de Romberg para integração de funções

## Descrição do problema

O método de Romberg é usado para o cálculo da integral definida de uma dada função, esse método usa como base o método de n-trapézios, cujas propriedades foram analisadas em detalhe nas aulas da disciplina.

O objetivo desse trabalho consistiu em desenvolver duas funções:

```python
romb(a,b,n,ε,ITMAX,fx)
```

Para cálculo da integral da função fx, onde os parâmetros são: *a* e *b*, extemos do intervalo de integração; *n*, número inteiro especificando quantos valores são usados na coluna *k* = 0 (*n* + 1 valores); *ε*, tolerância; e *ITMAX*, número máximo de iterações.

```python
trapz(a,b,T,i,fx)
```

Para uso da fórmula dos trapézios e usada pela rotina do método de Romberg, onde os novos parâmetros de entrada são: *i*, referente ao número de intervalos dos trapézios; e *T* valor calculado anteriormente pela fórmula dos trapézios.

Para ler a descrição completa do problema, acessar o documento [Enunciado.pdf](https://github.com/matheusrmorgado/Romberg-Integration/blob/master/Enunciado.pdf).

## Testes

<p align="left">
  <img src="https://github.com/matheusrmorgado/Romberg-Integration/blob/master/equations/eq.png">
</p>