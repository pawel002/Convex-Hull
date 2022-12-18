from time import time

def benchmark(hullAlgorithm, timeOfBenchamrk, generator, *args):
    '''Funkcja przyjmuje algorytm tworzacy otoczke, czas po jakim chcemy przeprowadzic benchmark w sekundach oraz
       argumenty generatora. Dzieki temu unikniemy sytuacji zadania za duzego zbioru danych. Wyniki zostają uśrednione.'''

    startTime = time()
    cumTime = 0

    count = 0
    while True:

        if time() - startTime > timeOfBenchamrk:
            break
        
        points = generator(*args)

        benchStart = time()
        hullAlgorithm(points)
        benchEnd = time()

        cumTime += benchEnd - benchStart
        count += 1
    
    print("TESTS FINISHED" + 20*"-")
    print("Executed", count, "tests.")
    print("Average time per test:", cumTime / count)

