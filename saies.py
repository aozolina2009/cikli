SpeletajaVards=input("Ievadi savu vārdu: ")

SpeletajaVards=SpeletajaVards.lower()
#"mainīgais.lower()" - konvertē visus burtu simbolus par mazajiem burtiem.

SpeletajaVards=SpeletajaVards.capitalize()
#"mainīgais.capitalize" - Simbolu virknē pirmo burtu konvertē par lielo burtu.
print(SpeletajaVards)

vards1="čība"

burtuSk=len(vards1)
# len - saskaita virknē simbolu skaitu.
minējums=input(f"Uzraksti vārdu pareizi- {vards1[3]}{vards1[0]}{vards1[2]}{vards1[1]}:")
# mainīgais[burta pozīcija]- simbolu virkne sākās ar indeksu -0.

minējums=minējums.lower()

if minējums==vards1:
   print("Uzminēji vārdu!")
else:
   print(" Neuzminēji vārdu!")