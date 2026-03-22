import pandas as pd

df = pd.read_csv('/Users/makbuk/VSCode/Python/students.csv', delimiter=',')
kfcLovers = df[df['Fastfood']=='KFC']['Weight']
bkLovers = df[df['Fastfood']=='Бургер кинг']['Weight']
mcdLovers = df[df['Fastfood']=='Макдональдс (или как он там сейчас называется?)']['Weight']
meanKfcWeigth = kfcLovers.mean()
meanBkWeigth = bkLovers.mean()
meanMcdWeigth = mcdLovers.mean()
print(meanKfcWeigth-meanMcdWeigth)