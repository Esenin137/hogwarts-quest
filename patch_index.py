# -*- coding: utf-8 -*-
# Патч первой части: запоминаем последний финал и добавляем кнопку «Часть 2: Сова»
p='index.html'
t=open(p,encoding='utf-8').read()
def rep(old,new):
    global t
    assert t.count(old)==1,('не найдено или не единственно',old[:60])
    t=t.replace(old,new)
# 1) в финале (e===6) пишем S.end и сохраняем заново
rep('if(e===6){var g=[];','if(e===6){S.end=id;sv_();var g=[];')
# 2) кнопка продолжения на экране финала
rep('else btn("Начать заново",start,"go");return}',
    'else{btn("Часть 2: переписка «Сова»",function(){location.href="part2.html"},"go");btn("Начать заново",start,"go")}return}')
open(p,'w',encoding='utf-8').write(t)
print('ok')
