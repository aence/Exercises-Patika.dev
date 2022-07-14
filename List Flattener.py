
flatten_list = []

def flattener(thelist,container):
    # ENG
    # Flattener is a function to flatten the lists inside the lists. 
    # "thelist" argument specifies the list to be flattened.
    # "container" argument specifies the list to carry the flattened list
    # TUR
    # Flattener fonksiyonu içinde listeler bulunan listeleri tek katmanlı bir listeye çevirir ( düzleştirir ).
    # "thelist" argümanı düzleştirilecek listeyi belirtir.
    # "container" argümanı düzleştirilen listeyi taşıyacak olan listeyi belirtir.
    
    for i in range(len(thelist)):
        if type(thelist[i]) != list:
            container.append(thelist[i])
        else:
            flattener(thelist[i],container)
    return container

test_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flattener(test_list,flatten_list))

print(test_list)
print(flatten_list)
