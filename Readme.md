# Generator transakcji - PYTHON

Parametry

- ilość kart
- ilośc użytkowników
- max ilośc kart per użytkownik

1. generacja transackji z zadanym rozkładem normalnym
2. zachowanie relacji One-To-Many dla uzytkownik-karty
3. generowanie skrajnie dużych i skrajnie małych transakcji dla UŻYTKOWNIKA - procentowo
4. generowanie podejrzanych częstotliwości transakcji dla jednej / wszystkich kart

5. generownie transakcji z poza obszaru akceptowalnego - np ocean
6. generowanie trnasakcji na obszarze dopuszczalnym o zwiększonej częstotliwości w wielu obszarach różniących sie
7. nagłe generowanie dopuszczalnych ale nie standardowych wartości transakcji (percentile analysis, mean standard deviation)
8. generowanie dwóch kolejnych transakcji w krótkim odstępie czasowym

## tryby

### Zadany scenariusz

100 popranych
10 ze skrajnymi wartościami
10 transackji odbiegających od progu
10 transackj poza obszarem
10 transackj poza percentylami lokalizacji
10 transackji percentylowe

### Generacja real time na podstawie prawdopodobienstwa

# Detekcja anomalii - JAVA

Complexity - 1-3

1. Analiza progowa (Treshold Analysis)

   - wykrywanie skrajnie małych i skrajnie dużych transakcji na podstawie tresholdu dla wszystkich transackji (1)
   - wykrywanie odbiegających od zadanego progu częstotliwości wykonywania transakcji dla wszystkich transakcji(2)

2. Analiza lokalizacji (Pattern-Based Anomaly Detection)
   - transakcje wykonywane w obszarze poza treshold i po za terytorium stanów zjedoczonych (1) - wszystkie transakcje
   - badanie percentyli lokalizacji transakcji oraz limitów odległości - wszystkie transakcje (3)
3. Analiza statystyczna (Statistical Analysis)
   - analiza percentylowa- np. detekcja wartości transakcji w 95 centylu - wszystkie transakcje (3)
   - analiza stępli czasowych - wykrywanie czy dwie transakcje nie zostąły wykonane w za krótkim odstepie czasowym - wszystkie transackje (3)
   - analiza średniej wartości transakcji i odchylenia standardowego - wszystkie transakcje (3)
