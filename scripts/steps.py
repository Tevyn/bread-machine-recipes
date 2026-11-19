"""Conversational steps (and typo notes) for the site. Keyed by recipe name in data.py."""

def first(x=None):
    return f"Add everything except the {x}, in order." if x else "Add everything in order."

DOUGH_FIRST = "Add the dough ingredients in order."

def go(prog, crust=True):
    return f"Run it on {prog}."

# When the add-in and paddle beeps sound, as h:mm after pressing start.
BEEPS = {
    'White': ('0:40', '1:15'), 'French': ('1:15', '1:55'), 'Whole Wheat': ('0:50', '1:35'),
    'Sweet': ('0:30', '1:10'), 'Gluten Free': ('0:20', '0:35'),
}

def _in(t):
    h, m = map(int, t.split(':'))
    parts = ([f"{h} hour" + ("s" if h > 1 else "")] if h else []) + ([f"{m} minutes"] if m else [])
    return " ".join(parts) + " in"

def add_at(prog): return _in(BEEPS[prog][0])
def paddle_at(prog): return _in(BEEPS[prog][1])

def addin(x, prog):
    return f"Toss in the {x} {add_at(prog)}."

def paddle(prog):
    return f"Pull the paddle {paddle_at(prog)}."
COOL = "Let it cool completely on a rack before slicing."
DOUGH = "Run it on Dough. It takes an hour and a half."
GF_GO = "Run it on Gluten Free."

JAM = [first(), "Run it on Jam.",
       "Scrape down the pan about 10 to 15 minutes in so everything mixes.",
       "Jar it, let it cool, and cover. It keeps about 3 weeks in the fridge."]
CAKE = ["Spray the pan, then add everything in order.",
        "Run it on Cake, and scrape down the sides with a spatula while it mixes.",
        "Let it cool on a rack before slicing. If the top's still a little wet, give it 10 to 15 minutes on Keep Warm first."]
ROLL_IT = ("Pull the dough and the paddle {at}. Roll the dough into a rectangle about ¼ inch thick "
           "and 16 inches long, {spread}, and roll it up tight from a short end. Tuck the ends under and set it back in "
           "the pan without the paddle.")

STEPS = {
    "Basic White Bread": [first(), go("White"), paddle("White"), COOL],
    "Oatmeal Bread": [first(), go("White"), paddle("White"), COOL],
    "Cinnamon Swirl Bread": [DOUGH_FIRST, go("White"),
        "While it kneads, mix the swirl sugar and cinnamon (and the raisins, if you're using them) in a small bowl.",
        ROLL_IT.format(at=paddle_at("White"), spread="sprinkle the swirl all over it"), COOL],
    "Rye Bread": [first(), go("White"), paddle("White"), COOL],
    "Jalapeño Cheddar Bread": [first("jalapeño and cheddar"), go("White"), addin("jalapeño and cheddar", "White"), paddle("White"), COOL],
    "French Bread Loaf": [first(), go("French", False), paddle("French"), COOL],
    "King Arthur-Style French Bread": [first(), go("French", False), paddle("French"), COOL],
    "Rustic Italian Loaf": [first("sesame seeds"), go("French", False),
        paddle("French") + " Sprinkle the sesame seeds on top if you like.", COOL],
    "Country French Bread with Olives & Rosemary": [first("olives"), go("French", False), addin("olives", "French"), paddle("French"), COOL],
    "Parmesan Peppercorn French Bread": [first(), go("French", False), paddle("French"), COOL],
    "Semolina Bread with Fennel & Golden Raisins": [first("raisins"), go("French", False), addin("raisins", "French"), paddle("French"), COOL],
    "Basic Whole Wheat Bread": [first(), go("Whole Wheat"), paddle("Whole Wheat"), COOL],
    "Multigrain Cereal Wheat Bread": [first(), go("Whole Wheat"), paddle("Whole Wheat"), COOL],
    "Nutty Whole Wheat Bread": [first("nuts and seeds"), go("Whole Wheat"), addin("nuts and seeds", "Whole Wheat"), paddle("Whole Wheat"), COOL],
    "Wheat Bran Bread": [first(), go("Whole Wheat"), paddle("Whole Wheat"), COOL],
    "Challah Loaf": [first(), go("Sweet"), paddle("Sweet"), COOL],
    "Brioche Loaf": [first(), go("Sweet"), paddle("Sweet"), COOL],
    "Panettone Loaf": [first("dried fruit"), go("Sweet"), addin("dried fruit", "Sweet"), paddle("Sweet"), COOL],
    "Chocolate Cherry Loaf": [DOUGH_FIRST, go("Sweet"),
        ROLL_IT.format(at=paddle_at("Sweet"), spread="scatter the chocolate and cherries over it"), COOL],
    "Babka": [DOUGH_FIRST, go("Sweet"),
        "While it kneads, whisk the filling together in a small bowl.",
        ROLL_IT.format(at=paddle_at("Sweet"), spread="sprinkle the filling over it"),
        "While it bakes, make the glaze: warm the sugar and water in a small pot until the sugar dissolves.",
        "As soon as it's done, turn it out and brush the glaze over it while it's warm. Extra syrup keeps in the fridge for a couple of weeks.",
        "Let it cool completely before slicing."],
    "Gluten-Free Sandwich Bread": [first(), GF_GO, paddle("Gluten Free"), COOL],
    "Gluten-Free Multigrain Bread": [first(), GF_GO, paddle("Gluten Free"), COOL],
    "Gluten-Free Cinnamon Swirl Bread": [DOUGH_FIRST, GF_GO,
        "While it kneads, mix the sugar and cinnamon in a small bowl.",
        f"Pull the dough and the paddle {paddle_at('Gluten Free')}. Dust the counter heavily with GF flour (the blend or white rice flour), "
        "roll the dough into a rectangle about ¼ inch thick and 16 inches long, sprinkle the swirl over it, and roll it up tight "
        "from a short end. Tuck the ends under and set it back in the pan without the paddle.", COOL],
    "Gluten-Free Pizza Dough": ["Heat the oven to 400°F with racks in the lower and upper thirds.",
        first("brushing oil and toppings"), GF_GO,
        f"End the program {paddle_at('Gluten Free')}. The dough's done.",
        "Shape it into two 12-inch or four 6-inch rounds. Extra dough keeps overnight in the fridge or a month in the freezer.",
        "Brush the edges with oil and par-bake on the lower rack for 15 minutes, until the edges just firm up.",
        "Top it and finish on the upper rack, about 10 more minutes, until the edges brown."],
    "Sourdough Loaf and Boule": [first("cornmeal"),
        "Run it on Artisan Dough. It takes about 5 hours.",
        "For a loaf, pull the paddle when it finishes and run Bake for 60 minutes.",
        "For a boule, shape the dough into a 10-inch round on a floured counter, cover it loosely, and let it rest 20 to 30 minutes while the oven heats to 425°F.",
        "Move it to a parchment-lined sheet dusted with cornmeal, dust the top with flour, and slash an X about ¼ inch deep. Bake 25 to 30 minutes, until it's browned and sounds hollow, then let it cool completely."],
    "Ciabatta": [
        "The night before, mix the sponge in a big bowl, cover it loosely, and leave it out overnight (up to a day). It should be bubbly and smell a little sour.",
        "Add the sponge first, then the rest of the dough ingredients in order.",
        "Run it on Artisan Dough. It takes about 5 hours.",
        "When it's done, move the dough onto a parchment-lined pan, shape it into a 12-inch oblong, cover it loosely, and let it rest about 20 minutes.",
        "Heat the oven to 425°F, dust the top with flour, and bake about 30 minutes, until it's lightly browned and sounds hollow. Let it cool completely."],
    "French Baguettes": [first("cornmeal"), DOUGH,
        "When it's done, punch the dough down on a floured counter, cover it, and let it rest 10 minutes.",
        "Split it in half and roll each piece into a skinny 12-inch baguette. Set them on a sheet dusted with cornmeal, cover loosely, and let them rise 30 to 40 minutes. Meanwhile, put a pan of hot water on the bottom rack and heat the oven to 425°F.",
        "Dust them with flour, cut four diagonal slashes about ¼ inch deep in each, and bake 25 to 30 minutes, until they're browned and sound hollow."],
    "Cheddar Breadsticks": [first("brushing oil"), DOUGH,
        "When it's done, punch it down on a floured counter and line two sheets with parchment.",
        "Roll it into a rectangle about ¼ inch thick, 10 by 22 inches. Cut ½-inch strips, twist each one into a tight spiral, and lay them out with a little space between. Cover and let them rest about 30 minutes.",
        "Heat the oven to 375°F with racks in the upper and lower spots.",
        "Brush them with oil and bake 15 to 20 minutes until golden, swapping the pans halfway."],
    "Pizza Dough": [first(), DOUGH, "Then use it for whatever pizza you're making."],
    "Herb Focaccia": ["Add the crust ingredients in order.", DOUGH,
        "Punch it down on a floured counter and let it rest 10 minutes.",
        "Oil a shallow rimmed pan and dust it with cornmeal. Roll the dough out to fit, cover it loosely, and let it rise somewhere warm until it's about doubled, 40 to 50 minutes.",
        "Heat the oven to 450°F. Press dimples all over with oiled fingertips, about ½ inch deep and an inch apart, then drizzle the oil and scatter the salt, Parmesan, and herbs.",
        "Bake 20 to 25 minutes, until it's deep golden and crisp."],
    "Pretzels": [DOUGH_FIRST, DOUGH + " Line two sheets with parchment while you wait.",
        "Cut the dough into 12 pieces, about 57 g each, and keep them covered. Roll each into a thin rope, twist it into a pretzel, and set it on a sheet. Cover and let them rest 20 to 30 minutes.",
        "Stir the baking soda into the 2 cups of water.",
        "Bring a big pot of water to a boil and heat the oven to 425°F.",
        "Boil the pretzels one at a time for 3 minutes, flipping halfway. Drain them on a rack, dip each in the soda water, and put it back on the sheet.",
        "Sprinkle with coarse salt and bake 15 to 20 minutes, until they're deep golden."],
    "Whole Wheat Kalamata Rolls": [first(), DOUGH,
        "Turn it out onto a floured counter and line a sheet with parchment.",
        "Cut it into 12 pieces, shape each into an oval, and set them on the sheet. Cover and let them rise about 30 minutes, until roughly doubled. Heat the oven to 350°F.",
        "Cut two small slashes across each roll, dust with whole wheat flour, and bake 15 to 20 minutes, until they're dark golden."],
    "Garlic, Herb and Cheese Knots": [DOUGH_FIRST, DOUGH,
        "Turn it out onto a floured counter, sprinkle the garlic powder all over it, and line a sheet with parchment.",
        "Cut it into 12 pieces, roll each into a 10-inch rope, and tie it in a knot. Cover and let them rest about 30 minutes while the oven heats to 350°F.",
        "Melt the butter, then stir in the garlic, herbs, and salt off the heat.",
        "Bake the knots 15 to 18 minutes until lightly browned, brush them with the garlic butter right away, and give them 5 to 10 minutes before eating."],
    "Cinnamon Swirl Rolls": [DOUGH_FIRST, DOUGH,
        "While it runs, stir the sugars and cinnamon together for the filling, and beat the frosting ingredients until totally smooth.",
        "Punch the dough down, cut it in half, and let it rest covered for 10 minutes. Grease a 13 by 9 pan.",
        "Roll each half into a rectangle 12 inches wide and ½ inch thick. Brush with the melted butter, leaving a 1-inch strip bare on one long side, sprinkle the filling, and roll it up toward the bare edge. Pinch the seam, cut each log into 8, and set them in the pan. Cover and let them rise 30 minutes while the oven heats to 350°F.",
        "Bake 30 to 35 minutes, until they're puffed and lightly golden.",
        "Let them cool 20 to 25 minutes, then frost."],
    "Basic Sweet Dough": [first(), DOUGH,
        "Punch it down on a floured counter and let it rest 10 minutes before you use it, like for the Danish."],
    "Raspberry Cheese Danish": [
        "Make the Basic Sweet Dough and line two sheets with parchment.",
        "While it runs, blend the cream cheese, sugar, salt, egg, and vanilla in the food processor until smooth, and chill it.",
        "Cut the dough in half, roll each piece to roughly 14 by 10 inches, and set them on the sheets. Spread the filling down the middle and spoon the preserves over it.",
        "Cut ½-inch strips along both sides, from the edge in to the filling, and fold them over the top in an alternating crisscross all the way down. Heat the oven to 350°F.",
        "Cover them loosely and let them rise until almost doubled. Brush with egg wash and bake 30 to 40 minutes, until golden and set.",
        "If you want the glaze, whisk milk into the sugar and vanilla a few drops at a time until it drizzles.",
        "Slide them onto a rack and pull the parchment out so the bottoms stay crisp. Let them cool, then dust or drizzle."],
    "Strawberry Rhubarb Jam": JAM,
    "Pear & Ginger Preserves": JAM,
    "Blueberry Lime Jam": JAM,
    "Mixed Berry Jam": JAM,
    "Banana Walnut Bread": CAKE,
    "Sour Cream Chocolate Bread": CAKE,
    "Zucchini Bread": CAKE,
}

ULTRA = ("Swap in rapid-rise yeast: 5.4 g for the 1 lb loaf or 7.8 g for the 1½ lb. Run it on Ultra-Fast (1:53 or 2:03) "
         "and pick up from step III. The timing's different on this program: add-ins go in at 13 minutes, and the paddle comes out at 18.")
