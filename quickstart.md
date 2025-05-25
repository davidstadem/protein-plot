# Quick Start

1. Go to the [website](https://stadem.pythonanywhere.com), or just download [the default plot image file](https://stadem.pythonanywhere.com/static/protein-plot.png). 

**To make your own plot**:

2. **Download the Nutrition Facts** used in this plot as a CSV file.
3. **Add your own foods** to the CSV file using Nutrition Facts for each food.
    - Here are all the columns in my CSV: `Name,From,Date,Price,Number,Unit,Servings per container,Calories per serving,Fat g,Carb g,Protein g`
    - You need at a minimum the following columns: `Name,Price,Servings per container,Calories per serving,Protein g`
4. **Upload the CSV** file back to the website. The protein plot automatically updates.Click the Upload button, or drag-n-drop your own file onto the button.
5. **Download your custom Protein Plot**: hover over the new protein plot. A camera image shows up with the hover data 'Download plot as a png'. Click to save the plot. 

I'd like to make the process much easier, but I'll need some more time to get that going. Then it'll be a 3 step process. Go to the website, click around to change prices, and export your results. 

# Notes

- in the CSV, you can delete rows for foods that you don't want. 
- You can just go in and update the price in the CSV. I've already entered in the nutrition facts. 
- Certain columns (From, Date, Number, Unit) won't impact the calculation at all. They're just for information. 
- The key is Servings Per Container. You need the right number for how many servings you're getting when you spend *x* amount of money. 

