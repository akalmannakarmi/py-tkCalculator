from calculator import Calculator
import time

tests = {
    "1-1":0,
    "1+1":2,
    "2*3":6,
    "6/3":2,
    "2^3":8,
    "5\\2":1,
    "25%":0.25,
    "4!":24,
    "p(4,3)":3,
    "c(4,3)":1,
    "Sin(90)":1,
    "log2(4)":2,
    "(2+2)":4,
    "1-1+1+1+2*3+6/3+2^3+5\\2+25%+4!+p(4,3)+c(4,3)+Sin(90)+log2(2+2)":54.25,
}


def run():
    print("Running")
    calc = Calculator()
    for q,a in tests.items():
        result = calc.calculate(q)
        print(f"{q}\t= {a} \tgot {result}")


if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"Time taken : {(time.time()-startTime)*1000}ms")