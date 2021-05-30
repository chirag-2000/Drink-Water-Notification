import time
from plyer import notification
import random

def ran(r):
    if r==1:
        return ("“A man of wisdom delights in water.” ― Confucius")
    if r==2:
        return("“By means of water, we give life to everything.”- Koran ")
    if r==3:
        return("“If there is magic on this planet, it is contained in water.” ― Loren Eiseley")
    if r==4:
        return("“I believe that water is the only drink for a wise man.” ― Henry David Thoreau")
    if r==5:
        return("“Did you know that dehydration has been linked to poor mood and fatigue? Drink Up!”")
    if r==6:
        return("“Bless the water you drink and it will light up the cells of your body.” ― Diana Cooper")
    if r==7:
        return("“To me, working out is literally like eating a meal or drinking water or breathing.” ― Hilary Swank")
    if r==8:
        return("“Water is life’s matter and matrix, mother and medium. There is no life without water.” ― Albert Szent-Gyorgyi")
    if r==9:
        return("“Water is a cure-all. Water is everything. You can’t get better without drinking lots of water, and you can’t drink water unless it’s clean.” ― Josh Fox")
    if r==10:
        return("“Drink water, stay hydrated, eat clean, exercise your brain and body, get rid of toxicity, and get shit done. That’s how you’ll win.”")
    
    

print("drink water")
if __name__=="__main__":
    while True:
        r=random.randint(1,10)
        notification.notify(
            title="Drink Water Right Now!!",
            
            message=ran(r),

            app_icon="M:\Python\drink_water_notification\drink_119593.ico",
        
            timeout=4
        )
        time.sleep(60*60)
