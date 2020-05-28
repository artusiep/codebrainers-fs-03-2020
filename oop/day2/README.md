## Dzień 2
### Powtórki
#### Filter, Map, Reduce
Super podsumowanie funkcji `filter`, `map`, `reduce` znajduje się tutaj: https://book.pythontips.com/en/latest/map_filter.html
#### Comprehension
Super podsumowanie z comprehension znajduje się tutaj: https://book.pythontips.com/en/latest/comprehensions.html
I bardzo rozbudowane podsumowanie na temat dict comprehension: https://www.programiz.com/python-programming/dictionary-comprehension
#### Lambdy:
Tutaj tez polece tą samą stronę: https://book.pythontips.com/en/latest/lambdas.html ale poza częścią _Parallel sorting of lists_
#### Lazy Evaluation:
- https://pl.wikipedia.org/wiki/Wartościowanie_leniwe
- https://www.tutorialspoint.com/functional_programming/functional_programming_lazy_evaluation.htm
### Bullet Pointy:
* `[{expression} for {elem} in {sequence/iterable} if {condition}]`
* `lambda`
* `filter`
* `map`
* `reduce`
### Zadania
1, Ze strony https://www.w3resource.com/python-exercises/lambda/index.php Zadania:
* 3 prosze zobaczyć jak to robią na stronie z powtórką https://book.pythontips.com/en/latest/lambdas.html 
* 6, 
* 13, 
* 17, 
* 18 można użyć `x==x[::-1]` i założyć, że pędziemy tylko sprawdzać słowa a nie zdania. Przykładowa lista: `texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]` 
2. W repozytorium znajduje się zadanie z list comprehension: https://github.com/artusiep/codebrainers-fs-03-2020/tree/master/oop/day2/homework/homework_01.py
Kod wystarczy przekopiować do własnego repozytorium do nowego pliku i odpalić. Na samym początku 22 testów powinno zfailować.
```
***Test Failed*** 22 failures.
```
Jeżeli pojawią się problemy z odpaleniem pliku odezwać się na slacku.
Efekt ma być taki:
```
*** ALL TESTS PASSED!
```