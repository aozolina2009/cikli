vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu="saies"

minejums=None

while UzminiVardu!=minejums:
  #Cikls strādā, kamēr netiek ievadīts vārds "saies"
  # != nav vienāds
    minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[2]+UzminiVardu[3]}: ")
print("Pareizi!")


UzminiVardu="Saule"

while True:
  minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[2]+UzminiVardu[3]}: ")
  if UzminiVardu==minejums:
        print("Pareizi")
        break
   
meginamjumi=2
UzminiVardu="Skola"

for i in range(3):
    minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[2]+UzminiVardu[3]}: ")



    if UzminiVardu==minejums:
        print("Pareizi")
        break
    else:
        print("Neuzminēji, tev palikuši {meinajumi} meģinajumi")
        meginamjumi-=1