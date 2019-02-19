print("Advertised GB are listed in thier base 10 form.")
print("All data however, is stored using base 2!")
print("I'm here to help you understand how many GB you're actually purchasing")
      
gb=int(input('Enter the advertised GB =>'))
base10=gb*(10**9)
oneGBinBase2= 2**30
base2=round(base10/oneGBinBase2)
lostGB=gb-base2
lostGB=round(lostGB)

print(gb,'GB in base 10 is actually',base2,
      'in base 2, which is', lostGB, ' less than advertised')
print("You will have appriximately",base2,"GB available")
