pets = dict()  
pet_name = input("��� �������: ")  
pet_view = input(f"������� ��� ������� {pet_name}: ")  
pet_age = int(input(f"������� ������� ������� {pet_name}: "))  
pet_user = input(f"������� ��� ��������� ������� {pet_name}: ")  
if pet_age % 10 == 1 and pet_age % 100 != 11:  
    suffix = "���"  
elif pet_age % 10 in [2, 3, 4] and not (pet_age % 100 in [12, 13, 14]):  
    suffix = "����"  
else:  
    suffix = "���"  
pet_info = {  
    "��� ������� ": pet_view,  
    "������� ������� ": f"{pet_age} {suffix}",  
    "��� ��������� ": pet_user  
}  
pets[pet_name] = pet_info  
print(pets)  