def procent(sum,percent,month): 
    procent=percent/100 
    print(procent) 
    for i in range(month): 
        sum = (procent/12*(sum))+sum 
        print(f'Ваш вклад будет {sum} на {i+1} месяц') 
 
pr=int(input('Введите процент: ')) 
vk=int(input('Введите сумму вклада: ')) 
mon=int(input('Введите количество месяцев: ')) 
procent(vk,pr,mon)