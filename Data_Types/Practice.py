# # Lists
# # 1.
# # Create a list of 5 numbers. Print the largest and smallest number.
#
# # list_1 = [1,2,3,4,5]
# # print(max(list_1))
# # print(min(list_1))
#
# # OUTPUT
# # 1 is the largest element in the list
# # 5 is the smallest element in the lits
# # ONE DOWN
#
# # Add an element to the end of a list and remove one from the beginning.
# #  2.
# # list_2 = ['rohail','romail','raheel','wasim']
#
# # list_2.append('hasnain')
# # list_2.append('tasir')
# # list_2.append('sheryar')
# # list_2.pop(1) pop hamisha indexing layta hai
# #
# # print(list_2)
#
# #3. Reverse a list without using reverse() or slicing.
# # through sclicing
# # list_3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# # reverse_list = list_3[::-1]
# # print(reverse_list)
# # through reverse() method
# # list_3.reverse()
# # print(list_3)
#
# # Count how many times a particular value appears in a list.
# # # 4.
# # list_4 = [1,1,2,3,4,5,]
# # # how to find a value in a list which is repeated how many times
# # count_item = list_4.count(1) #ya help karta hai k brakets mai jo number hai wo kitni bar aya hai
# # print(count_item)
#
# # Replace all negative numbers in a list with 0.
# # 5.
# #
# # list_5 = [-1,-3,4,3,5,7,9,2,-2]
# # for item in range(len(list_5)):
# #     if list_5[item] < 0:
# #         list_5[item] = 0
# # print(list_5)
# #
#
# # ----------------------------------------------------------------------------------------------------------------
#
# # NOW LETS PLAY A BACKPACK GAME
# pack = []
# print('starting a journey with empty backpack')
#
# print("🎒", pack)
# print('--'*40)
#
# # now lets pick some things for our backpack
#
# print('📦1.picking up the nessesary things like (water, food , sleepingbag, tent...etc')
#
# pack  .append('Water 💧')
# pack  .append('Food 🍉')
# pack  .append('Food 🍉')
# pack  .append('Food 🍉')
# pack  .append('sleeping Bag 💤')
# pack  .append('tent ⛺')
# pack  .append('fire 🔥')
#
# print("🎒", pack)
# print('--'*40)
#
# # now we will add some things using a different way to collect items
#
# first_aid_items = ['bandage 🩹','medicine 💊','injection💉']
#
# pack += first_aid_items
#
# print('2.⛑️ adding some medical kit for safety purposes')
# print(f'first aid items: {first_aid_items}')
# print("🎒", pack)
# print('--'*40)
#
#
# # now we will exchanges some things with a marchant to upgrade items in the backpack
# print('3.⬆️ Upgrading the items in backpack')
# print('selling bandage 🩹')
# print('Upgrading with magic medicine 💊')
#
# pack.remove('bandage 🩹')
# new_item = pack.index('medicine 💊')
# pack[new_item] = 'magic medicine 💊'
#
# print("🎒", pack)
# print('--'*40)
#
#
# # NOW WE WILL CHECK FOR TOTAL ITEMS AND CHECK FOR UNIQUE ITEMS AN AS WELL AS COUNT
#
# print("🔍 checking for items in the Backpack")
# print("🎒", pack)
# total_items = len(pack)
# unique_items = set(pack) #yaha pa hum nay list ko set ma convert kya takay wo unique items ko ak bar hi print karay
# unique_count = len(unique_items)
# food_count = pack.count('Food 🍉')
#
# print(f'total items in the backpack are: {total_items}')
# print(f'unique items in the backpack are: {unique_count}')
# print(f'food count in the backpack is: {food_count}')
#
# print('--'*40)
#
#
# # Dropped The Backpack
#
# print('5. 🙃Dropped The Backpack up side down ')
#
# pack.reverse()
# print("🎒", pack)
# print('--'*40)
#
#
# # 6 Sort Your Backpack
# print('6.➡️ sorting the the backpack')
# pack.sort()
# print("🎒", pack)
# print('--'*40)
#
#
# # Stolen Items during Sleep
#
# print("Stolen Items during Sleep 💤")
# a   = pack.pop(0)
# b   = pack.pop(2)
# c   = pack.pop(1)
# stolen = [a, b, c]
#
# print(f"stolen items {stolen}")
#
# print("🎒", pack)
# print('--'*40)
#
# # 🪄 Found Magic Ring and Coin Pouch
#
# print("8. found a magic ring and a money pouch")
#
# ring = 'magic ring💍'
# pounch = ['coins 🪙','paper money💵']
#
# pack.insert(0, ring)
# pack.append(pounch)
#
# print("🎒", pack)
# print('--'*40)
#
# # Half Backpack Disappears
#
# print('9. 💥Half Items Magically Disappeared. Damn You Magic Ring...')
#
# count = len(pack)
# half = count // 2
# pack = pack[:half]
#
# print("🎒", pack)
# print('--'*40)
#
# print('10. 🧌Bandits Attacked.')
# print('Backpack Stolen...')
#
# pack = None                       # None is not the same as empty list!
#
# print('🎒', pack)
# print('-'*50)
#
#
#
# print('Game Over 🎮')
# print('Learn More Python To Fight Back! 💣')


#############################################################
# DICTIONARIES                                              #
#############################################################


# Dicitonaries

phonebook = {
    "rohail": "+92 35566 7788",
    "raheel": "+92 76555 0998",
    "romail": "+92 55443 7768",
}
# adding more items in the dictionary

phonebook['wasim']      =  '+92 34567 0987'
phonebook['sarim']      =  '+92 37566 7488'
phonebook['alian']      =  '+92 87657 4568'
phonebook['hasnain']    =  '+92 87650 2347'


print(phonebook)

number = phonebook['hasnain']
print(f'📞 Calling hasnain... ({number})')

number = phonebook['wasim']
print(f'📞 Calling wasim... ({number})')

number = phonebook['rohail']
print(f'📞 Calling rohail... ({number})')