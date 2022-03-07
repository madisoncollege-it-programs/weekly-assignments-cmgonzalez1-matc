#Christian Gonzalez
#Purpose: Create an output that looks exactly like each of the Questions.

varRed="Red"
varGreen="Green"
varBlue="Blue"
varName="Timmy"
varLoot= 10.4516295
#Example Question and answer:
#Output 'Your Green Output"
print(f"Your {varGreen:<0s} Output")

#Output: 'Hello Timmy'
print(f"Hello {varName}")

#Output: 'Red-Green-Blue'
print(f"{varRed}-{varGreen}-{varBlue}")

#Output: 'Is this green or blue?'
vargreen = varGreen.lower()
varblue = varBlue.lower()
print(f"Is this {vargreen} or {varblue}")

#Output: 'My name is TIMMY'
varNAME = varName.upper()
print(f"My name is {varNAME}")

#Output: '[++Red++]'
print(f"[++{varRed}++]")

#Output: '[green==]'
print(f"[{vargreen}==]")

#Output: '[*****blue]'
print(f"[*****{varblue}]")

#Output: 'BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue'
spamBlue = varBlue * 10 #I googled this command
print(spamBlue)

#Output: '10.4516295'
print(varLoot)

#Output: '10.5'
varLootStr = str(varLoot) #googled
print(varLootStr[0:3]+varLootStr[4])

#Output: 'I have $10.45'
print(f"I have ${varLootStr[0:5]}")

#Output: '[$$$Red$$$] [$$$Green$$$] [$$$Blue$$$]
print(f"[$$${varRed}$$$] [$$${varGreen}$$$] [$$${varBlue}$$$]")

#Output: '[  der  ] [  Green  ] [  eulB  ]'
print(f"[  {varRed[::-1]}  ] [  {varGreen}  ] [  {varBlue[::-1]}  ]")

#Output: 'First Color:[Red] Second Color:[Green] Third Color:[Blue]'
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
