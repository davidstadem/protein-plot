
# About the Protein Plot

So I'm putting together the grocery list for the billionth time, or else wandering through the store for the billionth time,
or sticking my head in the fridge for the billionth time.
What to eat? What to buy?
I know there's a tradeoff between good food and cheap food, and I know there's some food that's both good *and* cheap.
But I don't know how to figure it out, so half the time I just grab something easy - in other words, neither good nor cheap.

With the Protein Plot I know what's good (or at least what's a viable protein source) *and* cheap.

I collected the prices and Nutrition Facts of a bunch of different foods. 
I calculated two numbers: the Protein Price and the Protein Percentage. 
Why those two numbers? Because *if you get enough cheap protein, you'll get the calories and fat and carbs for free*.

## How to Use It

The goal is to find foods that are:
* **High in Protein Percentage** (further to the right on the plot)
* **Low in Protein Price** (further down on the plot)

**Key Insights from the Plot:**

* **Black beans** are among the cheapest protein sources (around $1.70/100g of protein), but they have lower protein percentages (about 35% respectively). **Chickpeas and Pinto Beans** are not shown on the plot because they overlap black beans, but they're also about the same.
* **Brown rice and ramen** have a low protein price simply because the food itself is so cheap. For instance, the protein from ramen is almost as cheap as protein from chicken thighs, but it comes with a lot of carbohydrates and fats. This illustrates the principle: "get enough cheap protein, and you'll get the fat and carbs for free." (read on for details on that)
* **Greek yogurt** (70% protein, $3/100g protein) is a significantly better protein source than a protein shake like **Huel** (40% protein, $6/100g protein). Greek yogurt tastes like chalk, of course, but that's not quantified on the plot.
* **Pork chops** are both cheaper than sliced turkey, and denser in protein.

## How to Make It
I gathered prices and Nutrition Facts over the course of a couple years. I live in North Dakota and shop mostly at Sam's Club, and I gathered these prices mostly in 2022. Your mileage may vary.

The formulas used are:

* **Protein Density (or Protein Percentage)**:
    $$Protein\ Density = \frac{g\ Protein\ per\ serving \times 4\ (kcal/g)}{Calories\ per\ serving}$$
    *(This calculates the percentage of calories from protein, as protein provides approximately 4 kcal per gram).*

* **Protein Price (Price per 100g of Protein)**:
    $$\$\ per\ 100g\ Protein = \frac{Container\ Price}{Servings\ per\ container\ \times\ g\ Protein\ per\ serving}\times 100$$
    *(This calculates the price of protein, expressed as the cost of getting 100g of protein from the specified food).*


## Conclusion

The Protein Plot helps you quickly compare protein sources. By aiming for foods with a high Protein Percentage and a low Protein Price, you can ensure you're getting enough protein without overspending. Remember, if you get enough cheap protein, you'll get the carbs and fat for free. This tool doesn't solve every nutritional challenge, but it addresses the frugal question of "How do I eat enough to live?" so you can then focus on "How do I eat to live well?".

For more information and to recreate or extend the protein plot, visit the [Protein Plot GitHub page](https://github.com/davidstadem/protein-plot).

---

# Frequently Asked Questions (FAQ)


Perhaps you have many burning questions, and perhaps you're interested in some rambly half-baked attempts to answer said burning questions! 

On New Year's Day, 2025, I posted the protein plot [on Reddit](https://www.reddit.com/r/Frugal/comments/1hr3r2t/the_protein_plot_cheap_food_is_basically_cheap/).
I got some great feedback.
Below is a bunch of rambly FAQ stuff that didn't make it into the post, as well as feedback from the post.

## **Q1: Why cheap protein?**
A1: tl;dr because *if you get enough cheap protein, you'll get the calories and fat and carbs for free*.

Defining "cheap food" can be tricky.

- *Price per pound?* Often, grocery stores help you compare the same food in different containers by giving you the price per ounce or gram. This is nice if it's the same food, but doesn't work across all foods because, among other things, water content skews it. Dry beans don't get cheaper just because you cook them in water, but the price per pound will go down. The cheapest food on this metric is straight tap water.
- *Price per calorie?* This is a little closer - after all, food is fuel right? Problem is that optimizing a diet solely on calories isn't effective. For a given food, think of what it would cost to feed yourself on just that food for a day (a standard 2,000 calories). 2,000 calories of beef jerky costs $25, while 2,000 calories of white rice is as low as $0.70. Carb-rich and fat-rich foods generally win the "cheap energy" game. Even plain sugar is cheap ($0.85), and vegetable oil at $0.47 is the cheapest food on this metric. But I'm not about to chug a 16-oz bottle of oil a day, and I can't base my diet on it either.

What surprised me is that the more protein-rich a food is, *the more you pay for that protein*.
There aren't really any pure protein sources, and the more you concentrate the protein, the more expensive it gets.
Carbs and fat are *way* cheaper than protein on an energy basis.
So much so that if you want to get the cheapest protein, you're going to buy foods like black beans and peanut butter that have some protein but are also packed with carbs and fat.
Ultimately, this is why you don't need to buy fat and carbs because *if you get enough cheap protein, you'll get the fat and carbs for free*.

## **Q2: How can I eat frugally without starving?**

A2: What a great segue into my shot-from-the-hip, wholly unsubstantiated philosophy on eating:

***Stadem's Hierarchy of Food Needs***

In the vein of [Maslow's Hierarchy of Needs](https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs),
I've made a list of my own personal food needs.
I need to meet the needs at the top of the list before I get to the needs at the back.
If I don't get enough water, I'll die in days. Water's at the top of the list.
Trans fats will kill me, but it'll take decades, so down to the bottom they go.
I do myself a disservice if I'm pounding kiwis to get all my micronutrients when I haven't gotten enough protein.


The hierarchy is prioritized by what is most urgent for you to survive. 

1.  **Water**
2.  **Calories**
3.  **Protein**
4.  **Fiber**
5.  **Vitamins/Micronutrients**
6.  **Not Too Much** (Portion Control)
7.  **Minimize "Bad Stuff"** (e.g., trans fats, carcinogens, microplastics)


The idea is to address lower-level needs first. As in the example above, focusing on micronutrients (level 5) before ensuring adequate protein (level 3) would be counterproductive. 
The shortcut is protein: now that *you'll get the calories and fat and carbs for free*, the Protein Plot checks boxes 2 and 3 simultaneously.
This allows you to then concentrate on higher-level needs like fiber and micronutrients.

## Q3: Aren't Plant Proteins and Animal Proteins Different?

This was the main complaint I got: Animal proteins should outrank plant proteins.

A3: well according to [u/Ajreil](https://www.reddit.com/r/Frugal/comments/1hr3r2t/comment/m4veksa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) and [Healthline](https://www.healthline.com/nutrition/incomplete-protein), all protein *is* more or less equal in the way the body utilizes it.
The differences can be complex and vary based on individual needs and overall diet.
But ultimately, I want to make something that works for a wide variety of people, and treating all protein as equal is a simple approach that I think works and isn't too confusing.

## Q4: Isn't Cheap Protein a Red Herring?

[u/ProtozoaPatriot](https://www.reddit.com/r/Frugal/comments/1hr3r2t/comment/m4x09g3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) wrote:
> ... you're missing the point of nutrition. Americans don't suffer insufficient Protein intake unless they have problems such as eating disorder or severe intestinal issues. What we are lacking are the micronutrients (vitamins, minerals) as well as antioxidants and fiber.


A4: Exactly! "We are lacking the micronutrients (vitamins, minerals) antioxidants, and fiber" - yes, *and* we eat too much over-processed food, too much poisonous/toxic food, and too much food in general. And this I think is a very important point of nutrition: **it's too overwhelming to have to fix all those problems at once.** Even a robot gets lost in the noise when you start piling on objectives in a multi-objective optimization problem; why would we expect people to do better? It's no wonder we struggle to eat right when there's 10 different dimensions of what right even is.

So yes, cheap protein isn't the *only* aspect of nutrition. However, the Protein Plot offers a simple, actionable first step to eating cheaply.
Because cheap protein, *gives you the calories and fat and carbs for free*, it's a great shortcut to eating frugally.
You can meet your protein needs affordably with foods like Greek yogurt, tuna, eggs, beans, rice, and rotisserie chicken.
Yes, there's more that you *should* do to get fiber and vitamins, and more that you *could* do for the environment and your long-term health, but you've done what you *had* to do. 
Once these foundational needs are met, you're better positioned to tackle higher-level goals.

## In Summary

You can rapidly compare protein sources by putting them on the protein plot.
The goal is to get the *highest Protein Percentage* (further to the right) for the *lowest Protein Price* (further down).
You'll never starve if you buy cheap protein because if you get enough cheap protein, you'll get the fat and carbs for free.
This doesn't solve all your problems, but it answers your first question of "how do I eat enough to live?" and frees you up to ask your second question "How do I eat to live well?"
