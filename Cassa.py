class Cassa:

    summa=25125 # ���������� ����� � �����

    def top_up(self, pokup):

       self.pokup=pokup

       pokup+=Cassa.summa

       return f"� ����� {pokup}"

    def count_1000(self):

       print(Cassa.summa//1000)

    def take_away(self, x):

         if x<=self.summa:

          self.summa-=x

         else:

          return f"�� ���������� �����"
r=Cassa()
print(r.top_up(125))























