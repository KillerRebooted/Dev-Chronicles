from turtle import *

win = Screen()
win.tracer(0)

og_clicks = 0
clicks = 0
cost = 100

prestige_cost = 1000
prestige_clicks = 1

click_multiplier = 1

def update_score():

    og_click_count.clear()
    multiplier.clear()
    click_count.clear()

    og_click_count.write(f"Actual Clicks: {og_clicks}", align = "center", font = ("Courier", 24, "bold"))
    multiplier.write(f"Multiplier: {click_multiplier}x (Multiplier Cost: {cost}, Prestige Cost: {prestige_cost})", align = "center", font = ("Courier", 24, "bold"))
    click_count.write(f"Clicks: {clicks}", align = "center", font = ("Courier", 24, "bold"))

def prestige():

    global clicks, cost, prestige_cost, prestige_clicks, click_multiplier

    if clicks >= prestige_cost:
    
        click_multiplier = 1
        clicks = 0
        cost = 100

        prestige_clicks *= 2
        prestige_cost *= 4

    update_score()

def buy_multiplier():

    global click_multiplier, clicks, cost

    if clicks >= cost:

        click_multiplier += 1
        clicks -= cost

        cost += int(10/100 * cost)

    update_score()

def score(x, y):

    global og_clicks, clicks, prestige_clicks

    og_clicks += 1
    clicks += click_multiplier * prestige_clicks

    update_score()

og_click_count = Turtle()
og_click_count.hideturtle()
og_click_count.penup()
og_click_count.goto(0, 30)

multiplier = Turtle()
multiplier.hideturtle()
multiplier.penup()
multiplier.goto(0, 0)

click_count = Turtle()
click_count.hideturtle()
click_count.penup()
click_count.goto(0, -30)

update_score()

win.listen()

win.onclick(score)
win.onkeypress(buy_multiplier, "m")
win.onkeypress(prestige, "p")

done()
