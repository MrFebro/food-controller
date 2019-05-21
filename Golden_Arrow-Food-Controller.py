#By: Luis Febro
#Goal: A programmatic approach to manage food goods better based on the type and quantity.
#Code written in Brazilian Portuguese Language for User Interface, but instructions in English.
#Date: 06/20/19

# IMPORTS
from datetime import *
import math

# FUNCTIONS
# Creating the title from the project
def title():
  print('')
  print('=' * 18)
  print('FOOD CONTROLLER')
  print('=' * 18)

# DATES:
def today():
  # ELEMENTS
  # today
  today = datetime.now()
  #weekday
  days = 'Segunda Terça Quarta Quinta Sexta Sábado Domingo'.split()
  days_numb = today.weekday() #here does not need -1 because function ALREADY STARTS WITH 0 (Segunda)
  #monthes
  monthes = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()
  monthes_numb = today.month - 1 #equalizes with index
  #BUILDING
  #formating day
  format_day = days[days_numb]
  #formating date
  format_date = today.strftime('%d de {} de %Y - %H:%M.').format(monthes[monthes_numb])
  #RESULT
  if days_numb < 5:
    result = '{}-Feira, {}'.format(format_day, format_date)
  else:
    result = '{}, {}'.format(format_day, format_date)
  return result

# Showing the weekday from Dates
def weekday_show(datehere):
  # MONTHES
  monthes = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()
  month_numb = datehere.month - 1 # it starts with 1 and list of monthes 0. Then they need to be equalized properly.
  # DAYS
  days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
  weekday_numb = datehere.weekday()
  real_date = datehere.strftime('%d de {} de %Y'.format(monthes[month_numb]))
  if weekday_numb < 5:
    result = '{}-Feira, {}.'.format(days[weekday_numb], real_date)
  else:
    result = '{}, {}.'.format(days[weekday_numb], real_date)
  return result

# Condition to check if it is a leftover until 2 units or big spoon if there more than 3
def leftover_biggest(ts, sd): # ts = total_spoon, sd = spoon_day
  left = 'Primeiro Dia: {} {} (Menor Qtde)'.format(int(ts % sd), type_food()) # only remainder(rest) here
  big = 'Primeiro Dia: {} {} (Maior ou Igual Qtde).'.format(int((ts % sd) + sd), type_food()) # here it is the remainder (rest) of division + spoon day
  if int(ts % sd) <= 2: #here I decided to put <= 2 as the rest of total_spoon \ spoon_day to calculate if bigger or lower quantity
    return big
  else:
    return left

# Type Food


def type_food():
  if type_food_selection == 1:
    return 'Unidades'
  elif type_food_selection == 2:
    return 'Colheres de Sopa'
  elif type_food_selection == 3:
    return 'Colheres de Chá'
  else:
    return 'Opção Inválida!'


# VARIABLES
# Food Infos
title()
print('Hoje: {}'.format(today()))
# Comida e Preço
print('')
#food panel algorithm
#addfood here:
food_list = sorted(['Tapioca - Goma',
  'Tapioca - Farinha',
  'Aveia em Flocos',
  'Ovos',
  'Castanha do Pará',
  'Chia',
  'Castanha de Cajú',
  'Canela',
  'Milho de Pipoca'])
food_len = len(food_list)
c_food = 1
while c_food <= food_len:
  print('[ {} ] {}'.format(c_food, food_list[c_food - 1]))
  c_food += 1
print('ESCOLHA')
food_opt = int(input('Escolha o Número da sua Comida: '))
food_selec = str(food_list[food_opt - 1]).strip().upper()
food_price = float(input('PREÇO pago R$'))
# Escolha do tipo
print('')
print('''===TIPO DE COMIDA POR:===
[ 1 ] Unidades;
[ 2 ] Colheres de Sopa;
[ 3 ] Colheres de Chá;''')
type_food_selection = int(input('SELECIONE A OPÇÃO: '))
print('OK...')
print('')
# Soup Spoons
total_spoon = float(input('TOTAL de {} contados: '.format(type_food().upper())))
spoon_day = float(input('META de {} por dia: '.format(type_food().upper())))
# Conditions to round up days
if total_spoon % spoon_day == 0:
  days_available = total_spoon / spoon_day
elif total_spoon % spoon_day >= 0.5:
  days_available = math.ceil(total_spoon / spoon_day)
else:
  days_available = math.floor(total_spoon / spoon_day)
# Money per day
money_perday = food_price / days_available
# Period of food Available witdatetimeh format Dates
start_period = datetime.now()
# -1 excludes ONE MORE DAY and generate the right period because the duration period already includes today insertion.
end_period = start_period + timedelta(days=days_available - 1)
# If equal days, not necessary - 1
if end_period == start_period:
  end_period = start_period + timedelta(days=days_available)
else:
  end_period
# Format_dates
form_start_period = start_period.strftime('%d/%m/%y')
form_end_period = end_period.strftime('%d/%m/%y')

title()
print('>>> ANÁLISE {} <<<'.format(food_selec))
print('> COMPRADO por R${:.2f}, R${:.2f} ao dia.'.format(food_price, money_perday))
print('> RENDE: {:.0f} dias;'.format(days_available))
print('Início: {}'.format(today()))
print('Término: {}'.format(weekday_show(end_period)))
print('''> META CONSUMO:
Total Contado: {:.0f} {};
{}
Outros {:.0f} dias: {:.0f} {}
HISTÓRICO:
Local: / Marca:Sem / Grama:Sem / Preços:R${:.2f}, por dia: R${:.2f} / {} Total: {:.0f} /Obs:Sem'''.format(total_spoon, type_food(), leftover_biggest(total_spoon, spoon_day), days_available - 1, spoon_day, type_food(), food_price, money_perday, type_food(), total_spoon)) # -1 Because we are already calculating the FIRST DAY
