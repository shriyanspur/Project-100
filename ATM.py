class Atm:
  def __init__(self, CardNumber, Pin):
    self.cardnumber = CardNumber
    self.pin = Pin

  def check_balance(self, balance):
    print()
    print('Your balance is', balance)
    print()

  def withdrawl(self, amount, balance):
    if (amount <= balance):
      new_amount = balance - amount
      print()
      print('You have withdrawn amount: ' + str(amount))
      print('Your remaining balance is '+ str(new_amount))
      print()
    else:
      print()
      print('Amount entered exceeds account balance')
      print('Your account balance is', balance)
      print()

def main():
  print()
  Card_Number = input('Enter your card number: ')
  Pin_Number  = input('Enter your pin number: ')
  Balance = 10000
  print()

  new_user = Atm(Card_Number, Pin_Number)

  print('Choose your activity: ')
  print('1. Check Balance')
  print('2. Withdrawl Cash')
  print()
  activity = int(input('Enter activity number: '))

  if (activity == 1):
    new_user.check_balance(Balance)
  elif (activity == 2):
    print()
    amount = int(input('Enter the amount to be withdrawed: '))
    new_user.withdrawl(amount, Balance)
  else:
    print('Enter a valid number')


main()