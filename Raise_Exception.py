

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):  # input'tan gelen değer tipi int mi değil mi
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise  ValueError("Only even numbers can be added")
        super().append(integer)

# Yukarıdaki örnekte koşullardan herhangş biri tutmadığı taktirde "raise" anahtar kelimesi ile özel bir durum oluşturulacak. Hatırlarsanız bu tarz özel durumları geçtiğimiz derslerde "try-except" bloğu ile ele almıştık. Burada raise bizi bu bloğu kullanmaktan ve onun belli sınırlılıklarından kurtardı. Tabiki raise tek başına try-except'in görevini sergiileyemez. Sadece satır aralarındaki hatalar konusunda bize yardımcı olur.

# isinstance() => Bu method belirtilen nesne belirtilen türde is "True" önecektir. Aksi taktridde "False" dönecektir. Bu örnekte paramtreye gelencek değeri "int" olup olmadığı kontrol edilecek. Gelen değer "int" tipinde ise boolen bir değer yani "True" dönülecek. Aksi taktirde "False" dönülecek. Bu metodun type prametresi bir "tuple" ise nesne tuplekdaki türlerden biriyse bu işlev gene True döner.

e= EvenOnly()

# Örnek Çalıştırıldığında aşağıdaki hata alınacaktır:
# Senaryo 1
# e.append("a string")
# TypeError: Only integers can be added

# Senaryo 2
# e.append(3)
# ValueError: Only even numbers can be added

# Senaryo 3
e.append(2)
# Son senaryoda herhangi bir exception furlatılmadı. Çünkü karar mekanizmalarımdaki şartlar tutmadı.

def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised") # Her hangi bir şart olamdığı için bu raise herzaman fırlatılacak
    print("This line will never execute")
    return  "I won't be returned"

# call_exceptor() metodunu test ederken açağıdaki satırı comment'te aldık.
# no_return()

def call_exceptor():
    print("call_exceptor starts here..!")
    no_return()
    print("This line and so on never excecute")
    print("an exception was raised..!")
    print("... so these lines don't run...!")
call_exceptor()

# try-except içerisinde kendi oluşturduğumuz raise yapılarını kullanabilirilz
try:
    no_return()
except:
    print("I caught a exception")
    print("executed after the exception")