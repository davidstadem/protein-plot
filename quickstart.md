# Quick Start Guide: The Protein Plot

This guide helps you use the Protein Plot website and create your own customized plots.

## Option 1: View the Default Plot

1.  Go to the [Protein Plot website](https://stadem.pythonanywhere.com).
2.  You can also directly download [the default plot image](https://stadem.pythonanywhere.com/static/protein-plot.png).

## Option 2: Create Your Own Custom Plot

1.  **Download the Nutrition Facts:**
    * Click the 'Download' button to download my CSV file containing nutrition facts. This file includes columns like: `Name,From,Date,Price,Number,Unit,Servings per container,Calories per serving,Fat g,Carb g,Protein g`. 
2.  **Add Your Own Foods:**
    * **Open the CSV file** in a spreadsheet editor.
    * **Add nutritional information** for your new foods. At minimum, fill in these columns: `Name,Price,Servings per container,Calories per serving,Protein g`. The `Servings per container` value is important - make sure it's right! This value is the number of servings you're getting for the price you enter.
    * **Update or remove existing foods:** You can change prices or remove rows for foods already listed.
    * ***Note:*** Columns like `From, Date, Number, Unit` are for your reference and don't affect the plot calculations. 
3.  **Re-generate Your Custom Plot:**
    * Return to the [Protein Plot website](https://stadem.pythonanywhere.com).
    * Upload your modified CSV file. You can click the "Upload" button or drag and drop the file onto the button.
    * The website will automatically generate your custom Protein Plot.
4.  **Download Your Plot:**
    * Hover your mouse over the newly generated plot on the website.
    * A camera icon will appear with the tooltip "Download plot as a png". Click this icon to save your custom plot.

**Future Goal:** I hope to add functionality to the website itself. Then you could just visit the website, click around to add or change prices, and export your results.