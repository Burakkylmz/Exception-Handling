
"""
def funny_division(divider):
    try: # try içerisine hata alabileceğimiz yada hata oluşabilecek kod bloklarını yazıyoruz
        return  100 / divider
    except ZeroDivisionError: # Nokta atışı yuani spesific bir hata yoklanıyor
        return  "Zero is not good idea for in this case"
    except TypeError: # Nokta atışı yuani spesific bir hata yoklanıyor
        return "Check your self mate..! You can to type only a number"
    except: # Gelebilecek her türlü excep burada bakıalcak
        return "Something going wrong..!"

print(funny_division(
    int(input("Type into a number: "))
))

class Divider:
    def funny_divison_2(self, number):
        try:
            if number == 13:
                raise ValueError("13 is an unluck number..!")
            return  100 / number
        except (ZeroDivisionError, TypeError):
            return "Enter a number other than zero..!"

bolucu = Divider()
for val in(0, "hello", 50.0, 13):
    print("Testing: {}\nResult:".format(val), end=" ")
    print(bolucu.funny_divison_2(val))

def funny_divison_3(number):
    try:
        if number == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / number
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return  "Enter a numerical value"
    except ValueError:
        print("No no, not 13..!")
        raise

for val in (0, "hello", 50.0, 13):
    print("Testing: {}\nResult:".format(val), end=" ")
    print(funny_divison_3(val))
"""


# Aşağıdaki gibi Exception Type'lardan oluşan bir liste oluşturun
# some_exception = [ValueError, TypeError, IndexError, None]
# Random olarak bu liste den bir hata seçin ve türüne bağlı
# olarak exception içerisinde mesaj verin

import  random
some_exception = [ValueError, TypeError, IndexError, None]
try:
    choisce = random.choice(some_exception)
    print("rasing {}".format(choisce))
    if choisce:
        raise choisce("An error")
except ValueError:
    print("I caught a value error..!")
except TypeError:
    print("Caught type error..!")
except IndexError:
    print("Caught index error..!")
except Exception as e:
    print("Caught some other error..!")
else:
    print("This code called if there is no exception")
finally:
    print("No matter what this block called..!")