def sum(*numbers):
    result=0
    for n in numbers:
        result += n
    print(f"sum = {result}") 

def main():
    sum(1,2,41,24,51)