
def dict_collector(file_path):
    with open(file_path, 'r',encoding ='utf 8' ) as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_point = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) 
                ingridient = file_work.readline().strip().split(' | ') 
                for point in ingridient:
                    dish_point['ingredient_name'] = ingridient[0]
                    dish_point['quantity'] = ingridient[1]
                    dish_point['measure'] = ingridient[2]
                list_of_ingridient.append(dish_point)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline() 

    return(menu)

dict_collector('cook_book.txt')

def get_shop_list_by_dishes(dishes, persons=int):

    menu = dict_collector('cook_book.txt')
    print('Узнай больше в нашем меню :')
    print(menu)
    print()
    shopping_list = {}

    try:
        for dish in dishes:
            for point in (menu[dish]):
                
                point_list = dict([(point['ingredient_name'], {'measure': point['measure'], 'quantity': int(point['quantity'])*persons})])
                if shopping_list.get(point['ingredient_name']):
                    
                    other_point = (int(shopping_list[point['ingredient_name']]['quantity']) +
                                  int(point_list[point['ingredient_name']]['quantity']))
                    
                    shopping_list[point['ingredient_name']]['quantity'] = other_point

                else:
                  
                    shopping_list.update(point_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        
   get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
