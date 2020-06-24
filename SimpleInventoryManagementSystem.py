

class Inventory:
    def lock(self, item_type):
        '''
            Aynı envanteri iki farklı müşteriye satılmasını önlemek istiyoruz.
            Ürün değişimi yapıldığında değişltirilecek envanter türünü seçtireceğiz
            Bir method vasıtasıyla kimse envanteri iade edilene kadar değiştiremeyecek
        '''
        return item_type


    def unlock(self, item_type):
        '''
            Diğer müşterilerin herhangi bir ürüne erişebilmesi içn verilen
            envanteri serbest bırakacak method
        '''
        pass

    def purchase(self, item_type):
        '''
            Envanteri kilitli değilse, bir istisna oluşturualcak.
            1.item_type bir istisna oluşturun.
            2.Envanter şu anda stokta yoksa bir istisna oluşturun.
            3.Envanter mevcutsa bir envater çıakrın ve kalan envanter sayısını döndürün.
        '''
        pass

inventory = Inventory()
item_type = inventory.lock(
    input("Please type into a item type info: ")
)

try:
    num_left = inventory.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock")
else:
    print("Purchase process completed. Thera are {} {}s left".format(num_left, item_type))
finally:
    inventory.unlock(item_type)









