#You can make your own decorators
#Decorators alter functions

def cough(func):

    def func_wrapper():
    #stuff that happens before the function
        print("*cough*")
        func()

    #any stuff that happens after our function
        print("*cough*")
    return func_wrapper


@cough
def awkward():
    print("Can I get a discount?")


@cough
def answer():
    print("This is a dollar tree. . .")


awkward()
answer()
