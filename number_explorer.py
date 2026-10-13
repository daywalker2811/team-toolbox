''' Trainee mod for numbers stats '''

def get_divisors(n : int) -> list[int]:
    ''' get integers divisors for an integer '''
    divisors = []
    for i in range (1, n+1):
        if n % i == 0 :
           divisors.append(i)
    return divisors 

def is_prime(n : int) -> bool:
    '''tell if a integer is prime or not'''
    return True if get_divisors(n) == [1, n] else False

def run() -> None :
    ''' demo run '''
    user_input = int(input("Enter a positive integer : "))
    print(f"{user_input} is {"Even" if user_input % 2 == 0 else "Odd"}")
    print(f"Divisors : {get_divisors(user_input)}")
    print(user_input, "is a prime number" if is_prime(user_input) else "is not a prime number")
    for i in range(1,11):
        print(f"{user_input} x {i} = {i*user_input}")


if __name__ == "__main__":
    run()
            
