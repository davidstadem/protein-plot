# Intro
This is the Protein Plot, a tool to help you identify cheap protein. You can use cheap protein as the driver for cheap food.


# How I got here

So I'm putting together the grocery list  for the billionth time, or else wandering through the store for the billionth time,
or sticking my head in the fridge for the billionth time.
What to eat? What to buy?
I know there's a tradeoff between good food and cheap food, and I know there's some food that's both good *and* cheap.
But I don't know how to figure it out, so half the time I just grab something easy - in other words, neither good nor cheap.

With the Protein Plot I know what's good (or at least what's a viable protein source) *and* cheap.

I collected the prices and Nutrition Facts of a bunch of different foods. 
I calculated two numbers: the Protein Price and the Protein Percentage. 
Why those two numbers? Because *if you get enough cheap protein, you'll get the calories and fat and carbs for free*.

# How to Use It

The goal is to get the *highest Protein Percentage* (further to the right) for the *lowest Protein Price* (further down).
Use the plot to train your instincts and figure out which foods make the best building blocks of a frugal meal plan.

- The cheapest sources of protein are peanut butter and chickpeas (about $1.70/100g). However, they are also low in protein percentage (peanut butter: 17%, chickpeas: 35%).
- Brown Rice and Ramen have almost no protein, but they're still a reasonably priced source of protein because they're so cheap. Ramen protein is actually as cheap as black beans - it's just that you get a ton of carbs and fat along with it. That's why I say you get the fat and carbs for free.
- Greek yogurt (70% protein, $3/100g) is a much better protein source than a protein shake like Huel (40%, $6/100g). I mean it tastes like chalk, but that's not quantified on the plot.
- Pork chops are better than ground beef.
- As far as dry beans go, chickpeas are a little better than black beans, but they're close.

# How to Make It
I gathered prices and Nutrition Facts over the course of a couple years. I live in North Dakota and shop mostly at Sam's Club, and I gathered these prices mostly in 2022. Your mileage may vary.

Formulas are pretty straightforward:

$Protein\ Density = \frac{g\ Protein\ per\ serving \times 4}{Calories\ per\ serving}$

$\$\ per\ 100g\ Protein = \frac{Container\ Price}{Servings\ per\ container\ \times\ g\ Protein\ per\ serving}\times 100$


# Conclusion

See this site at https://github.com/davidstadem/protein-plot

------------------------

If you're still reading, maybe you have some burning questions or Important Stuff That You Need To Tell Me.
Perhaps you're interested in some rambly half-baked attempts to answer those questions! 

On New Year's Day, 2025, I posted this [on Reddit](https://www.reddit.com/r/Frugal/comments/1hr3r2t/the_protein_plot_cheap_food_is_basically_cheap/).
I got some great feedback.
Below is a bunch of rambly FAQ stuff that didn't make it into the post, as well as feedback from the post.

------------------------

# If you get enough cheap protein, you'll get the calories and fat and carbs for free

What's the definition of cheap food? Price per pound?
That's silly, you can just pump a bunch of water into a food for more or less free,
so the cheapest foods are just the ones with the most water. That's not right.

What about price per calorie?
I'm an energy engineer, which means I like to think about prices of different forms of energy,
from coal $1/GJ to electricity $30/GJ.
The problem there is that optimizing a diet based on energy doesn't work well.
A calorie (kcal) is 4.184 kJ, so there are about 240,000 calories in a GJ.
Turns out brown rice, the cheapest calorie source, is $150/GJ, and beef jerky is closer to $3,000/GJ.
So brown rice wins.
And as it turns out, all the carb-rich and fat-rich foods win at the cheap-energy game.
Carbs and fat are *way* cheaper than protein on an energy basis.

In fact, carbs and fat are so much cheaper that if you
What surprised me is that the more protein-rich a food is, the more you pay for that protein.
Carbs and fat are the opposite. Pure carbs, i.e. flour or sugar, is cheap per gram of carbs, and pure oil is cheap per gram of fat.
But protein doesn't work that way. There aren't really any pure protein sources, and the more you concentrate the protein, the more expensive it gets.
This means that when it comes to eating cheaply, the most important macronutrient is protein.
Specifically, you don't need to buy fat and carbs because *if you get enough cheap protein, you'll get the fat and carbs for free*.

# Stadem's Hierarchy of Food Needs

What a great segue into my shot-from-the-hip, wholly unsubstantiated philosophy on eating:

In the vein of [Maslow's Hierarchy of Needs](https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs),
I've made a list of my own personal food needs.
I need to meet the needs at the front of the list before I get to the needs at the back.
I do myself a disservice if I'm pounding kiwis to get all my micronutrients when I haven't gotten enough protein.

If carbs and fat are basically free, then I can skip ahead and check off level 3,
because if I get enough *cheap* protein then I will definitely get enough calories.

1. Water
2. Calories
3. Protein
4. Fiber
5. Vitamins/Micronutrients
6. Not Too Much!
7. Minimize "Bad Stuff" (trans fats, carcinogens, microplastics)

So yes, if you're optimizing for protein before you optimize for calories, that's bad.
But now that *you'll get the calories and fat and carbs for free*, the Protein Plot has killed two birds with one stone.
Then you're free to move onto the items further back in the hierarchy.

# But Not all Protein is Created Equal

This was the main complaint I got: Animal proteins should outrank plant proteins.

**Response**: well according to [u/Ajreil](https://www.reddit.com/r/Frugal/comments/1hr3r2t/comment/m4veksa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) and [Healthline](https://www.healthline.com/nutrition/incomplete-protein), all protein *is* created equal, so there!
OK, it's true that not all protein is exactly equal. But the differences are complex, and different proteins are going to be different for different people, and all that. Accounting for that complexity is going to add confusion to the plot.
Ultimately, I want to make something that works for a wide variety of people, and treating all protein as equal is a simple approach that I think works.

# But This Problem Is Irrelevant

Shoutout here to [u/ProtozoaPatriot](https://www.reddit.com/r/Frugal/comments/1hr3r2t/comment/m4x09g3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), who wrote:
> ... you're missing the point of nutrition. Americans don't suffer insufficient Protein intake unless they have problems such as eating disorder or severe intestinal issues. What we are lacking are the micronutrients (vitamins, minerals) as well as antioxidants and fiber.

Yeah, granted; cheap protein is not the point of nutrition. However, you'll notice that the statement "we are lacking the micronutrients... antioxidants, and fiber" is not the point of nutrition either - it's three different points. And that's not counting the other, probably more important points of nutrition - Americans eat too much over-processed food, too much poisonous/toxic food, and too much food in general. And this I think is a very important point of nutrition: **it's too overwhelming to have to fix all those problems at once.** Even a robot gets lost in the noise when you start piling on objectives in a multi-objective optimization problem; why would we expect people to do better? It's no wonder we struggle to eat right when there's 10 different dimensions of what right even is.

The solution isn't perfect, but it's easy. Adopt Stadem's Hierarchy of Needs, and skip right ahead to the protein plot. Water is level 1, and that's very cheap. Level 2 is calories, and remember that if you get enough cheap protein, *you'll get the calories and fat and carbs for free*, so you can skip ahead to protein. Use the protein plot to build a diet that clears Level 3 without breaking the bank - Greek yogurt, tuna, eggs, beans, rice, rotisserie chicken. Now you've made some progress. Yes there's more that you *should* do, and more that you *could* do, but you've done what you *had* to do. 

Not only that, optimizing for cheap protein does start moving you in the right direction when it comes to those higher-level goals.
Beans have tons of fiber.

There's even evidence to suggest that higher-protein diets increase satiation which helps you avoid over-eating, although I don't think the protein plot will actually move the needle much.

The protein plot has definitely failed on one aspect: encouraging you to eat vegetables.
So eat a bunch of vegetables.

# Conclusion

Does anybody want a conclusion?
Look, you can rapidly compare protein sources by putting them on the protein plot.
The goal is to get the *highest Protein Percentage* (further to the right) for the *lowest Protein Price* (further down).
You'll never starve if you buy cheap protein because if you get enough cheap protein, you'll get the fat and carbs for free.
This doesn't solve all your problems, but it answers your first question of "how do I eat enough to live?" and frees you up to ask your second question "How do I eat to live well?"
