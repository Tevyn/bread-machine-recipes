# Cuisinart CBK-110 recipe booklet, transcribed. Amount strings are as printed.
# item: (label, density_key, [amounts per size], tag, original_line_override)
# tag: "" normal | "addin" (hold back, add at add-in beep) | "warn:<col>[;<col>]|<msg>|<override>[;<override>]" (col: 1lb, 1.5lb, 2lb; msg may be empty on extra rows)

L3 = ["2 lb", "1½ lb", "1 lb"]
L2 = ["1½ lb", "1 lb"]

def I(label, key, amts, tag="", orig=None):
    if isinstance(amts, str):
        amts = [amts]
    return (label, key, amts, tag, orig)

def LOAD(program, crust=True):
    s = f"Press **PROG** → **{program}**. "
    s += "Set crust color and loaf size, then press **START/STOP**." if crust else "Set loaf size, then press **START/STOP**."
    return s

FIRST = "Put everything into the pan (paddle in) **in the order listed**, then lock the pan into the machine."
FIRST_EXCEPT = "Put everything except the {x} into the pan (paddle in) **in the order listed**, then lock the pan in."
RESHAPE = "*Optional:* at the paddle beep, pause, lift out the dough, remove the paddle, reshape, put it back and press START/STOP."
COOL = "When it finishes, turn the loaf out onto a wire rack and let it cool completely before slicing."

R = []

def recipe(**kw):
    R.append(kw)

# ---------------- WHITE ----------------
recipe(name="Basic White Bread", program="White", page=21, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=[], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1½ cups", "1 cup + 2 tablespoons", "¾ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter",
             ["3 tablespoons", "2 tablespoons + 1 teaspoon", "1½ teaspoons"],
             tag="warn:1lb|Booklet prints 1½ *tea*spoons for the 1 lb loaf. Every comparable recipe (e.g. Jalapeño Cheddar, same 3 tbsp → 2 tbsp + 1 tsp progression) scales to 1½ *table*spoons, so the gram figure uses that. As printed it would be 7.1 g.|1½ tablespoons"),
           I("Granulated sugar", "sugar", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"]),
           I("Kosher salt", "salt", ["1½ teaspoons", "1¼ teaspoons", "¾ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["4 cups", "3 cups", "2 cups"]),
           I("Nonfat dry milk", "dry_milk", ["¼ cup", "3 tablespoons", "2 tablespoons"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1 teaspoon", "¾ teaspoon"]),
       ])],
       steps=[FIRST, LOAD("White"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 96 cal (15% from fat) · carb 18 g · protein 3 g · fat 2 g · sat fat 1 g · chol 5 mg · sodium 189 mg · calcium 10 mg · fiber 0 g")

recipe(name="Oatmeal Bread", program="White", page=22, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=["Whole grain"], attention=[],
       sections=[(None, [
           I("Whole milk, room temperature", "milk", ["1¼ cups", "1 cup", "¾ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["2½ tablespoons", "2 tablespoons", "1½ tablespoons"]),
           I("Maple syrup (or honey)*", "maple", ["2 tablespoons", "1½ tablespoons", "1 tablespoon"]),
           I("Kosher salt", "salt", ["1¼ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["3¾ cups", "3 cups", "2¼ cups"]),
           I("Old-fashioned oats* (not quick-cooking)", "oats", ["1 cup", "¾ cup", "½ cup"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2¼ teaspoons", "2 teaspoons", "1¾ teaspoons"]),
       ])],
       steps=[FIRST, LOAD("White"), RESHAPE, COOL],
       notes=["*Sweeter version: add ½ tbsp more maple syrup (+9.8 g), swap the oats for granola, and add ½ tsp ground cinnamon (1.3 g)."],
       nutrition="Per 2-oz slice: 117 cal (17% from fat) · carb 21 g · protein 3 g · fat 2 g · sat fat 1 g · chol 6 mg · sodium 134 mg · calcium 21 mg · fiber 1 g")

recipe(name="Cinnamon Swirl Bread", program="White", page=23, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=["Spice", "Fruit"], attention=["Fill & roll at paddle beep"],
       sections=[("Dough (goes in the pan)", [
           I("Whole milk, room temperature", "milk", ["1¼ cups", "1 cup", "¾ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["2½ tablespoons", "2 tablespoons", "1½ tablespoons"]),
           I("Egg, large, room temperature", "egg", ["1", "1", "1"]),
           I("Kosher salt", "salt", ["1 teaspoon", "1 teaspoon", "½ teaspoon"]),
           I("Granulated sugar", "sugar", ["1½ tablespoons", "1 tablespoon", "1 tablespoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["4 cups", "3½ cups", "2½ cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2 teaspoons", "2 teaspoons", "1¾ teaspoons"]),
       ]), ("Cinnamon swirl (mix in a bowl; used at the paddle beep)", [
           I("Granulated sugar", "sugar", ["⅓ cup", "¼ cup", "3 tablespoons"]),
           I("Ground cinnamon", "cinnamon", ["2½ teaspoons", "2 teaspoons", "1½ teaspoons"]),
           I("Raisins (optional)", "raisins", ["1¼ cups", "1 cup", "¾ cup"]),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.",
              LOAD("White"),
              "While it mixes, stir the swirl ingredients (and raisins, if using) together in a small bowl.",
              "At the **paddle beep**, pause. Pull out the dough and remove the paddle. On a floured surface, roll the dough into a ¼-inch-thick rectangle about 16 in long, short side facing away from you. Sprinkle the swirl evenly over it, roll it up tightly from one short end, tuck the ends under, and put it back in the pan **without the paddle**. Press START/STOP.",
              COOL],
       nutrition="Per 2-oz slice: 141 cal (13% from fat) · carb 28 g · protein 4 g · fat 2 g · sat fat 1 g · chol 16 mg · sodium 139 mg · calcium 24 mg · fiber 1 g")

recipe(name="Rye Bread", program="White", page=25, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Whole grain", "Seeds"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1⅔ cups", "1¼ cups", "1 cup"], tag="warn:1lb||¾ cup + 1 tablespoon"),
           I("Kosher salt", "salt", ["1¼ teaspoons", "1 teaspoon", "¾ teaspoon"], tag="warn:2lb;1.5lb||1¾ teaspoons;1¼ teaspoons"),
           I("Unbleached all-purpose flour", "ap_flour", ["3 cups", "1¾ cups", "1¼ cups"], tag="warn:1.5lb;1lb||2¼ cups;1½ cups"),
           I("Rye flour", "rye_flour", ["2 cups", "1¼ cups", "¾ cup"], tag="warn:1.5lb;1lb||1½ cups;1 cup"),
           I("Caraway seeds (optional)", "caraway", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"]),
       ])],
       steps=[FIRST, LOAD("White"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 66 cal (5% from fat) · carb 15 g · protein 2 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 127 mg · calcium 1 mg · fiber 2 g")

recipe(name="Jalapeño Cheddar Bread", program="White", page=26, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Cheese"], attention=["Add-ins at beep"],
       sections=[(None, [
           I("Buttermilk, room temperature", "buttermilk", ["1½ cups", "1 cup", "¾ cup"],
             tag="warn:1.5lb||1 cup + 2 tablespoons"),
           I("Hot pepper sauce", "hot_sauce", ["¾ teaspoon", "½ teaspoon", "¼ teaspoon"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["3 tablespoons", "2 tablespoons + 1 teaspoon", "1½ tablespoons"]),
           I("Granulated sugar", "sugar", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"]),
           I("Kosher salt", "salt", ["1 teaspoon", "¾ teaspoon", "½ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["4 cups", "3 cups", "2 cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Jalapeño, seeded and finely chopped", "jalapeno", ["2 chiles", "1½ chiles", "1 chile"], tag="addin"),
           I("Sharp cheddar, shredded", "cheddar", ["1 cup", "¾ cup", "½ cup"], tag="addin"),
       ])],
       steps=[FIRST_EXCEPT.format(x="jalapeño and cheddar"), LOAD("White"),
              "At the **add-in beep**, add the jalapeño and cheddar.", RESHAPE, COOL],
       nutrition="Per 2-oz slice: 108 cal (26% from fat) · carb 16 g · protein 4 g · fat 3 g · sat fat 2 g · chol 9 mg · sodium 132 mg · calcium 45 mg · fiber 0 g")

# ---------------- FRENCH ----------------
recipe(name="French Bread Loaf", program="French", page=28, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=[], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1½ cups", "1¼ cups", "1 cup + 1 tablespoon"], tag="warn:1lb||¾ cup + 2 tablespoons"),
           I("Kosher salt", "salt", ["1½ teaspoons", "1½ teaspoons", "¾ teaspoon"], tag="warn:1.5lb||1¼ teaspoons"),
           I("Unbleached all-purpose flour", "ap_flour", ["4 cups", "3¼ cups", "2¼ cups + 2 tablespoons"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons", "1 teaspoon"]),
       ])],
       steps=[FIRST, LOAD("French", crust=False), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 73 cal (0% from fat) · carb 13 g · protein 2 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 159 mg · calcium 1 mg · fiber 0 g")

# Not from the booklet: King Arthur's pro French bread ratios (67% water, 2% salt, 1.1% yeast),
# poolish folded into one straight dough. page=28.5 just sorts it next to French Bread Loaf.
recipe(name="King Arthur-Style French Bread", program="French", page=28.5, sizes=L3, delay="Yes", ultrafast=False,
       typ="Bread loaf", flavor="Plain", keyings=[], attention=[],
       source="Adapted from King Arthur Baking's French Bread with Poolish pro formula (kingarthurbaking.com/pro/formulas/french-bread-with-poolish), mixed as a straight dough.",
       sections=[(None, [
           I("Water, room temperature", "water", ["1⅓ cups + 1½ tablespoons", "1 cup + 2½ tablespoons", "¾ cup + 1½ tablespoons"]),
           I("Kosher salt", "salt", ["1¾ teaspoons", "1½ teaspoons", "1 teaspoon"]),
           I("Bread flour", "bread_flour", ["4 cups", "3¼ cups", "2¼ cups + 2 tablespoons"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1¾ teaspoons", "1¼ teaspoons + ⅛ teaspoon", "1 teaspoon"]),
       ])],
       steps=[FIRST, LOAD("French", crust=False), RESHAPE, COOL],
       notes=["Adapted from King Arthur's professional French bread formula: 67% water, 2% salt and 1.1% yeast by flour weight. Their version builds an overnight poolish; here that flour and water simply go into one dough."],
       nutrition="Estimated per 2-oz slice: 137 cal (4% from fat) · carb 27 g · protein 5 g · fat 1 g · sat fat 0 g · chol 0 mg · sodium 300 mg · calcium 6 mg · fiber 1 g")

recipe(name="Rustic Italian Loaf", program="French", page=29, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Whole grain", "Seeds"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1½ cups", "1 cup", "¾ cup"],
             tag="warn:1.5lb||1 cup + 2 tablespoons"),
           I("Olive oil", "olive_oil", ["2 tablespoons", "1½ tablespoons", "1 tablespoon"]),
           I("Kosher salt", "salt", ["2 teaspoons", "1½ teaspoons", "1 teaspoon"]),
           I("Granulated sugar", "sugar", ["1 teaspoon", "¾ teaspoon", "½ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["4 cups", "3 cups", "2 cups"]),
           I("Wheat bran (unprocessed, coarse)", "wheat_bran", ["½ cup", "⅓ cup", "¼ cup"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons", "1 teaspoon"]),
           I("Sesame seeds (optional, for the top)", "sesame", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"], tag="top"),
       ])],
       steps=[FIRST_EXCEPT.format(x="sesame seeds"), LOAD("French", crust=False),
              "*Optional:* at the paddle beep, pause, remove the paddle and reshape the dough. Sprinkle with sesame seeds if you like, then press START/STOP.",
              COOL],
       nutrition="Per 2-oz slice: 112 cal (9% from fat) · carb 24 g · protein 2 g · fat 1 g · sat fat 0 g · chol 0 mg · sodium 191 mg · calcium 1 mg · fiber 1 g")

recipe(name="Country French Bread with Olives & Rosemary", program="French", page=30, sizes=L3,
       delay="Yes (be there for add-ins)", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Olives", "Herbs", "Whole grain"], attention=["Add-ins at beep"],
       sections=[(None, [
           I("Water, room temperature", "water", ["1½ cups", "1 cup + 2 tablespoons", "¾ cup"]),
           I("Olive oil", "olive_oil", ["1 tablespoon", "2 teaspoons", "1½ teaspoons"]),
           I("Kosher salt", "salt", ["1½ teaspoons", "1¼ teaspoons", "¾ teaspoon"]),
           I("Honey", "honey", ["1 teaspoon", "1 teaspoon", "½ teaspoon"]),
           I("Fresh rosemary, chopped", "rosemary", ["1 tablespoon", "2 teaspoons", "1 teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["2½ cups", "2 cups", "1½ cups"]),
           I("Whole wheat flour", "ww_flour", ["1½ cups", "1 cup", "½ cup"]),
           I("Rye flour", "rye_flour", ["⅓ cup", "¼ cup", "3 tablespoons"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons", "1 teaspoon"]),
           I("Kalamata olives, pitted, drained, patted dry, halved", "olives", ["1 cup", "¾ cup", "½ cup"], tag="addin"),
       ])],
       steps=[FIRST_EXCEPT.format(x="olives"), LOAD("French", crust=False),
              "At the **add-in beep**, add the olives.", RESHAPE, COOL],
       nutrition="Per 2-oz slice: 81 cal (14% from fat) · carb 15 g · protein 2 g · fat 1 g · sat fat 0 g · chol 0 mg · sodium 184 mg · calcium 4 mg · fiber 1 g")

recipe(name="Parmesan Peppercorn French Bread", program="French", page=32, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Cheese", "Spice"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1¼ cups", "1 cup", "¾ cup"]),
           I("Olive oil", "olive_oil", ["¼ cup", "3 tablespoons", "2 tablespoons"]),
           I("Kosher salt", "salt", ["1¼ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["3¾ cups", "3 cups", "2¼ cups"]),
           I("Parmesan, grated", "parmesan", ["⅔ cup", "½ cup", "⅓ cup"]),
           I("Black pepper, freshly ground", "pepper", ["¾ teaspoon", "½ teaspoon", "¼ teaspoon"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons", "1 teaspoon"]),
       ])],
       steps=[FIRST, LOAD("French", crust=False), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 101 cal (29% from fat) · carb 15 g · protein 4 g · fat 3 g · sat fat 1 g · chol 3 mg · sodium 184 mg · calcium 41 mg · fiber 0 g")

recipe(name="Semolina Bread with Fennel & Golden Raisins", program="French", page=33, sizes=L3,
       delay="Yes (be there for add-ins)", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=["Fruit", "Seeds", "Spice"], attention=["Add-ins at beep"],
       sections=[(None, [
           I("Water, room temperature", "water", ["1⅔ cups", "1¼ cups + 1 tablespoon", "¾ cup + 2 tablespoons"]),
           I("Kosher salt", "salt", ["2 teaspoons", "1½ teaspoons", "1 teaspoon"]),
           I("Fennel seeds", "fennel", ["2 teaspoons", "1½ teaspoons", "1 teaspoon"]),
           I("Granulated sugar", "sugar", ["1 teaspoon", "¾ teaspoon", "½ teaspoon"]),
           I("Semolina flour", "semolina", ["3 cups", "2¼ cups", "1½ cups"]),
           I("Unbleached all-purpose flour", "ap_flour", ["1 cup", "¾ cup", "½ cup"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons", "1 teaspoon"]),
           I("Golden raisins", "raisins", ["¾ cup", "⅔ cup", "½ cup"], tag="addin"),
       ])],
       steps=[FIRST_EXCEPT.format(x="raisins"), LOAD("French", crust=False),
              "At the **add-in beep**, add the raisins.", RESHAPE, COOL],
       nutrition="Per 2-oz slice: 106 cal (3% from fat) · carb 23 g · protein 3 g · fat 1 g · sat fat 0 g · chol 0 mg · sodium 192 mg · calcium 7 mg · fiber 1 g")

# ---------------- WHOLE WHEAT ----------------
recipe(name="Basic Whole Wheat Bread", program="Whole Wheat", page=34, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=["Whole grain"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1¼ cups", "1 cup", "¾ cup"]),
           I("Kosher salt", "salt", ["1¼ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["2½ tablespoons", "2 tablespoons", "1½ tablespoons"]),
           I("Granulated sugar", "sugar", ["2 tablespoons", "1½ tablespoons", "1 tablespoon"]),
           I("Whole wheat flour", "ww_flour", ["2¼ cups", "2 cups", "1½ cups"]),
           I("Unbleached all-purpose flour", "ap_flour", ["1½ cups", "1 cup + 2 tablespoons", "¾ cup + 2 tablespoons"]),
           I("Rye flour", "rye_flour", ["2 tablespoons", "1½ tablespoons", "1 tablespoon"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1 tablespoon", "2¼ teaspoons", "2 teaspoons"]),
       ])],
       steps=[FIRST, LOAD("Whole Wheat"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 77 cal (20% from fat) · carb 13 g · protein 2 g · fat 1 g · sat fat 1 g · chol 3 mg · sodium 127 mg · calcium 10 mg · fiber 2 g")

recipe(name="Multigrain Cereal Wheat Bread", program="Whole Wheat", page=35, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=["Whole grain"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1¼ cups", "¾ cup + 3 tablespoons", "½ cup + 2 tablespoons"]),
           I("Plain fat-free yogurt", "yogurt", ["⅓ cup", "¼ cup", "3 tablespoons"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["3 tablespoons", "2 tablespoons", "1½ tablespoons"]),
           I("Light brown sugar, packed", "brown_sugar", ["2 tablespoons", "4 teaspoons", "1 tablespoon"]),
           I("Kosher salt", "salt", ["1½ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Whole wheat flour", "ww_flour", ["2 cups", "1½ cups", "1 cup"]),
           I("Unbleached all-purpose flour", "ap_flour", ["2 cups", "1½ cups", "1 cup"]),
           I("Multigrain cereal flakes", "cereal_flakes", ["2⅔ cups", "2 cups", "1⅓ cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2½ teaspoons", "2 teaspoons", "1¼ teaspoons"]),
       ])],
       steps=[FIRST, LOAD("Whole Wheat"), RESHAPE, COOL],
       notes=["Cereal flakes vary a lot by brand. The grams assume about 40 g per cup. For a better number, use your box's label: serving grams ÷ serving cups × cups needed."],
       nutrition="Per 2-oz slice: 84 cal (15% from fat) · carb 16 g · protein 3 g · fat 1 g · sat fat 1 g · chol 3 mg · sodium 130 mg · calcium 12 mg · fiber 2 g")

recipe(name="Nutty Whole Wheat Bread", program="Whole Wheat", page=36, sizes=L3, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Savory", keyings=["Nuts", "Seeds", "Whole grain"], attention=["Add-ins at beep"],
       sections=[(None, [
           I("Low-fat buttermilk, room temperature", "buttermilk", ["1½ cups", "1¼ cups", "1 cup"]),
           I("Kosher salt", "salt", ["1 teaspoon", "¾ teaspoon", "½ teaspoon"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["1½ tablespoons", "1 tablespoon", "1 tablespoon"]),
           I("Maple syrup", "maple", ["1½ tablespoons", "1 tablespoon", "1 tablespoon"]),
           I("Whole wheat flour", "ww_flour", ["2¼ cups", "2 cups", "1½ cups"]),
           I("Unbleached all-purpose flour", "ap_flour", ["1¼ cups", "1 cup", "¾ cup"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1 tablespoon", "2¼ teaspoons", "2 teaspoons"]),
           I("Mixed nuts & seeds (walnuts, pecans, pumpkin, sunflower…)", "mixed_nuts", ["¾ cup", "¾ cup", "½ cup"], tag="addin"),
       ])],
       steps=[FIRST_EXCEPT.format(x="nuts and seeds"), LOAD("Whole Wheat"),
              "At the **add-in beep**, add the nuts and seeds.", RESHAPE, COOL],
       nutrition="Per 2-oz slice: 129 cal (30% from fat) · carb 19 g · protein 4 g · fat 5 g · sat fat 1 g · chol 3 mg · sodium 103 mg · calcium 32 mg · fiber 2 g")

recipe(name="Wheat Bran Bread", program="Whole Wheat", page=37, sizes=L3, delay="Yes", ultrafast=True,
       typ="Bread loaf", flavor="Plain", keyings=["Whole grain"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["1½ cups", "1 cup + 2 tablespoons", "1 cup"], tag="warn:1lb||¾ cup + 2 tablespoons"),
           I("Kosher salt", "salt", ["1¼ teaspoons", "1 teaspoon", "¾ teaspoon"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["1½ tablespoons", "1 tablespoon", "1 tablespoon"]),
           I("Molasses", "molasses", ["2 tablespoons", "1½ tablespoons", "1 tablespoon"]),
           I("Whole wheat flour", "ww_flour", ["2¼ cups", "2 cups", "1½ cups"]),
           I("Unbleached all-purpose flour", "ap_flour", ["1½ cups", "1 cup", "¾ cup"]),
           I("Oats (not quick-cooking)", "oats", ["⅓ cup + 2 tablespoons", "⅓ cup", "¼ cup"]),
           I("Wheat bran", "wheat_bran", ["⅓ cup + 2 tablespoons", "⅓ cup", "¼ cup"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1 tablespoon", "2¼ teaspoons", "2 teaspoons"]),
       ])],
       steps=[FIRST, LOAD("Whole Wheat"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 99 cal (11% from fat) · carb 19 g · protein 3 g · fat 1 g · sat fat 1 g · chol 2 mg · sodium 128 mg · calcium 13 mg · fiber 3 g")

# ---------------- SWEET ----------------
recipe(name="Challah Loaf", program="Sweet", page=38, sizes=L2, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=[], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", ["¾ cup", "½ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["5 tablespoons", "4 tablespoons"]),
           I("Large egg, room temperature", "egg", ["1 egg", "1 egg"]),
           I("Kosher salt", "salt", ["1 teaspoon", "¾ teaspoon"]),
           I("Granulated sugar", "sugar", ["3 tablespoons", "2½ tablespoons"]),
           I("Unbleached all-purpose flour", "ap_flour", ["3 cups", "2¼ cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1½ teaspoons", "1¼ teaspoons"]),
       ])],
       steps=[FIRST, LOAD("Sweet"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 108 cal (28% from fat) · carb 17 g · protein 2 g · fat 3 g · sat fat 2 g · chol 19 mg · sodium 131 mg · calcium 2 mg · fiber 0 g")

recipe(name="Brioche Loaf", program="Sweet", page=39, sizes=L2, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=[], attention=[],
       sections=[(None, [
           I("Whole milk, room temperature", "milk", ["⅓ cup", "¼ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["6 tablespoons", "4 tablespoons"]),
           I("Large eggs, room temperature", "egg", ["3 eggs", "2 eggs"]),
           I("Kosher salt", "salt", ["1 teaspoon", "¾ teaspoon"]),
           I("Granulated sugar", "sugar", ["1½ tablespoons", "1 tablespoon"]),
           I("Nonfat powdered milk", "dry_milk", ["1½ tablespoons", "1 tablespoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["2¾ cups + 1 tablespoon", "2 cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2¼ teaspoons", "1¾ teaspoons"]),
       ])],
       steps=[FIRST, LOAD("Sweet"), RESHAPE, COOL],
       nutrition="Per 2-oz slice: 120 cal (36% from fat) · carb 16 g · protein 4 g · fat 5 g · sat fat 3 g · chol 42 mg · sodium 145 mg · calcium 20 mg · fiber 0 g")

recipe(name="Panettone Loaf", program="Sweet", page=40, sizes=L2, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=["Fruit", "Spice"], attention=["Add-ins at beep"],
       sections=[(None, [
           I("Whole milk, room temperature", "milk", ["½ cup", "⅓ cup"], tag="warn:1lb||⅓ cup + 2 tablespoons"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["4 tablespoons", "2 tablespoons"], tag="warn:1lb||3 tablespoons"),
           I("Large eggs, room temperature", "egg", ["2 eggs", "1 egg"]),
           I("Kosher salt", "salt", ["¾ teaspoon", "½ teaspoon"]),
           I("Granulated sugar", "sugar", ["¼ cup", "3 tablespoons"]),
           I("Unbleached all-purpose flour", "ap_flour", ["2¾ cups", "2 cups"]),
           I("Grated orange zest", "orange_zest", ["1 tablespoon", "2 teaspoons"]),
           I("Anise seed", "anise", ["1 teaspoon", "¾ teaspoon"]),
           I("Ground nutmeg", "nutmeg", ["½ teaspoon", "1¾ teaspoons"],
             tag="warn:1lb|Booklet prints 1¾ tsp nutmeg for the **1 lb** loaf, which is 3½× the 1½ lb amount. That's almost certainly a typo for ¼ tsp; the gram figure uses ¼ tsp. As printed it would be 3.9 g.|¼ teaspoon"),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2 teaspoons", "1¼ teaspoons"]),
           I("Mixed dried fruit (currants and/or candied citrus)", "dried_fruit", ["¾ cup", "½ cup"], tag="addin"),
       ])],
       steps=[FIRST_EXCEPT.format(x="dried fruit"), LOAD("Sweet"),
              "At the **add-in beep**, add the dried fruit.", RESHAPE, COOL],
       nutrition="Per 2-oz slice: 126 cal (23% from fat) · carb 21 g · protein 3 g · fat 3 g · sat fat 2 g · chol 28 mg · sodium 107 mg · calcium 17 mg · fiber 1 g")

recipe(name="Chocolate Cherry Loaf", program="Sweet", page=42, sizes=L2, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=["Chocolate", "Fruit"], attention=["Fill & roll at paddle beep"],
       sections=[("Dough (goes in the pan)", [
           I("Whole milk, room temperature", "milk", ["½ cup", "⅓ cup"], tag="warn:1lb||½ cup"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["¼ cup", "2 tablespoons"]),
           I("Large eggs, room temperature", "egg", ["2 eggs", "1 egg"]),
           I("Kosher salt", "salt", ["¾ teaspoon", "½ teaspoon"], tag="warn:1.5lb;1lb||1 teaspoon;¾ teaspoon"),
           I("Granulated sugar", "sugar", ["3 tablespoons", "2 tablespoons"]),
           I("Unbleached all-purpose flour", "ap_flour", ["3 cups", "2¼ cups"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["1¾ teaspoons", "1½ teaspoons"]),
       ]), ("Rolled in at the paddle beep", [
           I("Bittersweet chocolate, roughly chopped", "choc_chopped", ["⅔ cup", "½ cup"]),
           I("Dried cherries", "dried_cherries", ["½ cup", "⅓ cup"]),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.",
              LOAD("Sweet"),
              "At the **paddle beep**, pause. Pull out the dough and remove the paddle. On a floured surface, roll it into a ¼-inch-thick rectangle about 16 in long. Scatter the chocolate and cherries evenly over it, roll it up tightly from a short end, seal and tuck the ends, and put it back in the pan **without the paddle**. Press START/STOP.",
              COOL],
       nutrition="Per 2-oz slice: 155 cal (33% from fat) · carb 23 g · protein 4 g · fat 6 g · sat fat 3 g · chol 28 mg · sodium 107 mg · calcium 13 mg · fiber 1 g")

recipe(name="Babka", program="Sweet", page=44, sizes=L2, delay="No", ultrafast=True,
       typ="Bread loaf", flavor="Sweet", keyings=["Chocolate", "Spice"], attention=["Fill & roll at paddle beep"],
       sections=[("Dough (goes in the pan)", [
           I("Whole milk, room temperature", "milk", ["⅔ cup", "½ cup"]),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", ["4 tablespoons", "3 tablespoons"]),
           I("Large eggs, room temperature", "egg", ["2 eggs", "1 egg"]),
           I("Pure vanilla extract", "vanilla", ["1 teaspoon", "¾ teaspoon"]),
           I("Granulated sugar", "sugar", ["3 tablespoons", "2 tablespoons"]),
           I("Kosher salt", "salt", ["1 teaspoon", "¾ teaspoon"]),
           I("Unbleached all-purpose flour", "ap_flour", ["3 cups", "2 cups"]),
           I("Ground nutmeg", "nutmeg", ["¼ teaspoon", "1 to 2 pinches"]),
           I("Yeast (active dry, instant or bread machine)", "yeast", ["2 teaspoons", "1½ teaspoons"]),
       ]), ("Filling (whisk in a bowl; used at the paddle beep)", [
           I("Granulated sugar", "sugar", ["¼ cup", "3 tablespoons"]),
           I("Ground cinnamon", "cinnamon", ["2 teaspoons", "1½ teaspoons"]),
           I("Cocoa powder", "cocoa", ["1 tablespoon", "2 teaspoons"]),
           I("Kosher salt", "salt", ["Pinch", "Pinch"]),
       ]), ("Glaze (simmer while it bakes)", [
           I("Granulated sugar", "sugar", ["½ cup", "½ cup"]),
           I("Water", "water", ["⅓ cup", "⅓ cup"]),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.",
              LOAD("Sweet"),
              "While it mixes, whisk the filling ingredients together in a small bowl.",
              "At the **paddle beep**, pause. Pull out the dough and remove the paddle. On a floured surface, roll it into a ¼-inch-thick rectangle about 16 in long. Sprinkle the filling evenly over it, roll it up tightly from a short end, seal and tuck the ends, and put it back in the pan **without the paddle**. Press START/STOP.",
              "While it bakes, make the glaze: heat the sugar and water in a small saucepan over medium-high until the sugar fully dissolves.",
              "When it finishes, turn the babka onto a rack and **brush the glaze on right away** while it's warm. Leftover syrup keeps 2 weeks in the fridge.",
              "Let it cool completely before slicing."],
       nutrition="Per 2-oz slice: 147 cal (17% from fat) · carb 26 g · protein 3 g · fat 3 g · sat fat 2 g · chol 28 mg · sodium 147 mg · calcium 16 mg · fiber 1 g")

# ---------------- GLUTEN FREE ----------------
GF_PSYL = "Use psyllium husk **powder**, not whole husk, or the texture changes a lot. Look in the baking aisle or near the fiber supplements."
GF_STEPS = [FIRST, "Press **PROG** → **Gluten Free**, then press **START/STOP**.", RESHAPE.replace("lift out the dough, remove the paddle, reshape", "remove the paddle, reshape the dough"), COOL]

recipe(name="Gluten-Free Sandwich Bread", program="Gluten Free", page=46, sizes=["1½ lb"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf",
       typ="Bread loaf", flavor="Plain", keyings=[], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", "1 cup"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", "4 tablespoons", orig="4 tablespoons (½ stick)"),
           I("Large eggs, room temperature", "egg", "3"),
           I("Kosher salt", "salt", "1¼ teaspoons"),
           I("Granulated sugar", "sugar", "3 tablespoons"),
           I("Gluten-free all-purpose flour blend*", "gf_blend", "3¼ cups"),
           I("Psyllium husk powder**", "psyllium", "3 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
       ])],
       steps=GF_STEPS,
       notes=["*Store-bought GF blends weigh 120–155 g per cup. The grams here use about 131 g/cup, which is what the booklet's own DIY blend weighs. If your bag lists a cup weight, use that instead.",
              "*DIY blend (booklet), in grams: **192 g** brown rice flour (1½ c) + **142 g** white rice flour (1 c) + **64 g** arrowroot (½ c) + **28 g** tapioca starch (¼ c) = 426 g, exactly the 3¼ cups this loaf needs.",
              "**" + GF_PSYL],
       nutrition="Per 2-oz slice: 139 cal (24% from fat) · carb 24 g · protein 3 g · fat 4 g · sat fat 2 g · chol 38 mg · sodium 172 mg · calcium 8 mg · fiber 1 g")

recipe(name="Gluten-Free Multigrain Bread", program="Gluten Free", page=47, sizes=["1½ lb"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf",
       typ="Bread loaf", flavor="Plain", keyings=["Whole grain", "Seeds"], attention=[],
       sections=[(None, [
           I("Water, room temperature", "water", "1 cup"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", "4 tablespoons", orig="4 tablespoons (½ stick)"),
           I("Large eggs, room temperature", "egg", "3"),
           I("Kosher salt", "salt", "1¼ teaspoons"),
           I("Granulated sugar", "sugar", "3 tablespoons"),
           I("Gluten-free all-purpose flour blend*", "gf_blend", "2 cups"),
           I("Oat flour", "oat_flour", "1 cup"),
           I("Ground flax seed", "flax", "¼ cup"),
           I("Psyllium husk powder**", "psyllium", "2 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
       ])],
       steps=GF_STEPS,
       notes=["*GF blend grams use about 131 g/cup (the booklet DIY blend's weight). If your bag lists a cup weight, use that instead.",
              "*DIY blend (booklet), in grams: **128 g** brown rice flour (1 c) + **71 g** white rice flour (½ c) + **43 g** arrowroot (⅓ c) + **21 g** tapioca starch (3 tbsp) = 263 g.",
              "If you're strictly gluten-free, buy oat flour labeled certified GF.",
              "**" + GF_PSYL],
       nutrition="Per 2-oz slice: 105 cal (31% from fat) · carb 16 g · protein 2 g · fat 4 g · sat fat 2 g · chol 38 mg · sodium 172 mg · calcium 7 mg · fiber 1 g")

recipe(name="Gluten-Free Cinnamon Swirl Bread", program="Gluten Free", page=48, sizes=["1½ lb"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf",
       typ="Bread loaf", flavor="Sweet", keyings=["Spice"], attention=["Fill & roll at paddle beep"],
       sections=[("Dough (goes in the pan)", [
           I("Water, room temperature", "water", "1 cup"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", "4 tablespoons", orig="4 tablespoons (½ stick)"),
           I("Large eggs, room temperature", "egg", "3"),
           I("Kosher salt", "salt", "1¼ teaspoons"),
           I("Granulated sugar", "sugar", "3 tablespoons"),
           I("Gluten-free all-purpose flour blend*", "gf_blend", "3¼ cups"),
           I("Psyllium husk powder**", "psyllium", "3 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
       ]), ("Cinnamon swirl (used at the paddle beep)", [
           I("Granulated sugar", "sugar", "¼ cup"),
           I("Ground cinnamon", "cinnamon", "2 teaspoons"),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.",
              "Press **PROG** → **Gluten Free**, then press **START/STOP**.",
              "While it kneads, whisk the swirl ingredients together in a small bowl.",
              "At the **paddle beep**, pause. Remove the dough and paddle and turn the dough out onto a counter **heavily** dusted with GF flour (the blend or white rice flour). Roll it into a ¼-inch-thick rectangle about 16 in long, short side facing away from you. Sprinkle the swirl over it, roll it up tightly from a short end, tuck the ends under, and put it back in the pan **without the paddle**. Press START/STOP.",
              COOL],
       notes=["*GF blend grams use about 131 g/cup. If your bag lists a cup weight, use that instead.",
              "*DIY blend (booklet), in grams: **128 g** brown rice flour (1 c) + **142 g** white rice flour (1 c) + **64 g** arrowroot (½ c) + **28 g** tapioca starch (¼ c) = 362 g. The booklet's blend comes out short of 3¼ cups, so make extra.",
              "**" + GF_PSYL],
       nutrition="Per 2-oz slice: 135 cal (24% from fat) · carb 23 g · protein 2 g · fat 4 g · sat fat 2 g · chol 38 mg · sodium 172 mg · calcium 8 mg · fiber 1 g")

recipe(name="Gluten-Free Pizza Dough", program="Gluten Free", page=50, sizes=["2 lb dough"], delay="No", ultrafast=False,
       yield_="2 lb dough: two 12-in pizzas or four 6-in personal pizzas", machine_note="≈35 min (you stop it at the paddle beep)", machine_min=35,
       typ="Dough → oven", flavor="Savory", keyings=["Seeds"], attention=["Oven finish"],
       sections=[(None, [
           I("Water, room temperature", "water", "1¼ cups"),
           I("Olive oil", "olive_oil", "¼ cup"),
           I("Granulated sugar", "sugar", "2 teaspoons"),
           I("Kosher salt", "salt", "2 teaspoons"),
           I("Brown rice flour", "brown_rice_flour", "1 cup"),
           I("White rice flour", "white_rice_flour", "1 cup"),
           I("Arrowroot flour", "arrowroot", "½ cup"),
           I("Ground flax seeds", "flax", "⅓ cup"),
           I("Quinoa flour", "quinoa_flour", "⅓ cup"),
           I("Tapioca flour", "tapioca", "¼ cup"),
           I("Psyllium husk powder*", "psyllium", "3 tablespoons"),
           I("Baking powder", "baking_powder", "2½ teaspoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "1 teaspoon"),
           I("Olive oil, for brushing", "none", "", tag="top"),
           I("Pizza toppings of your choice", "none", "", tag="top"),
       ])],
       steps=["Heat the oven to **400°F** with racks in the lower and upper thirds.",
              FIRST.replace("Put everything", "Put everything except the brushing oil and toppings"),
              "Press **PROG** → **Gluten Free**, then press **START/STOP**.",
              "At the **paddle beep**, hold START/STOP until it beeps to **end the program**. The dough is done.",
              "Shape into two 12-in or four 6-in rounds. Extra dough keeps overnight in the fridge or 1 month frozen.",
              "Brush the edges with olive oil. Par-bake on the **lower** rack for 15 min, until just firm at the edges with little color.",
              "Add toppings and bake on the **upper** rack about 10 more min, until the edges are browned and the toppings hot."],
       notes=["*" + GF_PSYL],
       nutrition="Per serving (12 servings): 194 cal (30% from fat) · carb 31 g · protein 3 g · fat 7 g · sat fat 1 g · chol 0 mg · sodium 484 mg · calcium 21 mg · fiber 3 g")

# ---------------- ARTISAN DOUGH ----------------
recipe(name="Sourdough Starter", program="No machine", page=53, sizes=["Starter"], delay="n/a", ultrafast=False,
       yield_="About 1 lb of active starter after 5 days",
       typ="Starter", flavor="Plain", keyings=["Whole grain"], attention=["Overnight prep"],
       sections=[("Day 1 (stir in a glass or ceramic bowl)", [
           I("Water, room temperature", "water", "4 ounces", orig="4 ounces*"),
           I("Unbleached all-purpose flour", "ap_flour", "2 ounces", orig="2 ounces*"),
           I("Whole wheat flour", "ww_flour", "2 ounces", orig="2 ounces*"),
       ]), ("Daily feed, days 2–5 (add to the bowl)", [
           I("Water", "water", "4 ounces"),
           I("Flour (booklet just says flour; keeping the 50/50 all-purpose/whole wheat mix works well)", "ap_flour", "4 ounces"),
       ]), ("Day-5 refresh & weekly fridge feed (after discarding half)", [
           I("Water", "water", "2 ounces"),
           I("Flour", "ap_flour", "2 ounces"),
       ])],
       steps=["**Day 1:** stir the water and both flours until smooth in a glass or ceramic bowl. Cover loosely with plastic wrap or a damp towel and leave it in one spot at room temperature for 24 hours.",
              "**Days 2–5:** once a day, stir in another 113 g water + 113 g flour until smooth, then cover again.",
              "**After day 5:** it should have doubled, be full of bubbles, and smell sweet and yeasty. Stir, discard half (or give it away), then stir in 57 g water + 57 g flour. It's ready to use.",
              "**To store:** keep it in the fridge and feed it weekly with 57 g water + 57 g flour. Leave it at room temperature for 12–24 hours before baking with it."],
       notes=["The booklet already gives this recipe by weight. The original drawer also has its cup version for anyone without a scale."],
       nutrition="(none listed)",
       orig_extra="Cup version if you have no scale: ½ cup water, ½ cup less 1 tablespoon all-purpose flour, ½ cup less 1½ tablespoons whole-wheat flour (spooned and leveled).")

recipe(name="Sourdough Loaf and Boule", program="Artisan Dough", page=52, sizes=["1½ lb"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf or boule", machine_note="5:05 dough cycle, then 60 min on Bake for the loaf (or bake the boule in the oven)",
       typ="Bread loaf", flavor="Plain", keyings=[], attention=["Oven finish"],
       sections=[(None, [
           I("Water, cool", "water", "3 tablespoons"),
           I("Sourdough starter*, room temperature", "starter", "2 cups"),
           I("Bread flour", "bread_flour", "2½ cups"),
           I("Granulated sugar", "sugar", "1 teaspoon"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
           I("Cornmeal, for dusting (boule only)", "none", "", tag="top"),
       ])],
       steps=[FIRST_EXCEPT.format(x="cornmeal"),
              "Press **PROG** → **Artisan Dough**, then press **START/STOP** (5:05).",
              "**Loaf (bakes in the machine):** when the cycle ends, remove the paddle, switch to **Bake** and set it for **60 min**.",
              "**Boule (oven):** when the cycle ends, shape the dough into a 10-in round on a lightly floured surface. Cover loosely and rest 20–30 min. Heat the oven to **425°F**, rack in the middle.",
              "Move it to a parchment-lined sheet dusted with cornmeal, dust the top with flour, and slash an **X** about ¼ in deep. Bake 25–30 min, until browned and hollow-sounding. Cool completely on a rack before slicing."],
       notes=["*Starter weight assumes a 100%-hydration starter (equal weights flour and water), about 227 g per cup. Stir it down before measuring.",
              "Make your own: see Sourdough Starter."],
       nutrition="Per 2-oz slice: 81 cal (1% from fat) · carb 18 g · protein 3 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 195 mg · calcium 1 mg · fiber 1 g",
       links=["Sourdough Starter"])

recipe(name="Ciabatta", program="Artisan Dough", page=54, sizes=["1½ lb"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf",
       typ="Dough → oven", flavor="Plain", keyings=[], attention=["Overnight prep", "Oven finish"],
       sections=[("Overnight sponge (the night before)", [
           I("Bread flour", "bread_flour", "¾ cup"),
           I("Water", "water", "½ cup"),
           I("Yeast, active dry or instant", "yeast", "Pinch"),
       ]), ("Dough", [
           I("Overnight sponge, proofed", "none", "all"),
           I("Water, cool", "water", "¾ cup"),
           I("Olive oil", "olive_oil", "3 tablespoons"),
           I("Bread flour", "bread_flour", "2½ cups"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
       ])],
       steps=["**Night before:** mix the sponge ingredients in a large bowl until smooth. Cover loosely and leave at room temperature overnight, up to 24 h. It should be bubbly and smell pleasantly sour.",
              "Put the sponge in the pan first, then the remaining dough ingredients in order (paddle in). Lock the pan in.",
              "Press **PROG** → **Artisan Dough**, then press **START/STOP** (5:05).",
              "When the cycle ends, move the dough to a parchment-lined pan and shape it into an oblong about 12 in long. Cover loosely and rest about 20 min.",
              "Heat the oven to **425°F**, rack in the middle. Uncover, dust lightly with flour, and bake about 30 min, until lightly browned and hollow-sounding. Cool completely on a rack."],
       nutrition="Per 2-oz slice: 63 cal (21% from fat) · carb 16 g · protein 3 g · fat 2 g · sat fat 0 g · chol 0 mg · sodium 194 mg · calcium 1 mg · fiber 1 g")

# ---------------- DOUGH ----------------
DOUGH_GO = "Press **PROG** → **Dough**, then press **START/STOP** (1:30)."

recipe(name="French Baguettes", program="Dough", page=55, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="1½ lb dough → 2 baguettes",
       typ="Dough → oven", flavor="Plain", keyings=[], attention=["Oven finish"],
       sections=[(None, [
           I("Water, room temperature", "water", "1 cup + 2 tablespoons"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Granulated sugar", "sugar", "¾ teaspoon"),
           I("Bread flour", "bread_flour", "3 cups"),
           I("Wheat germ", "wheat_germ", "2 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "1¾ teaspoons"),
           I("Cornmeal, for dusting", "none", "", tag="top"),
       ])],
       steps=[FIRST_EXCEPT.format(x="cornmeal"), DOUGH_GO,
              "When the cycle ends, punch the dough down on a lightly floured surface. Cover and rest 10 min.",
              "Cut it in half and shape each piece into a narrow baguette about 12 in long. Put them on a cornmeal-dusted sheet, cover loosely, and let rise 30–40 min. Meanwhile put a pan of hot water on the oven's bottom rack and heat the oven to **425°F**.",
              "Dust with flour and make 4 diagonal slashes about ¼ in deep on each. Bake 25–30 min, until browned and hollow-sounding. Cool on a rack."],
       nutrition="Per 2-oz slice: 70 cal (1% from fat) · carb 15 g · protein 2 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 191 mg · calcium 1 mg · fiber 1 g")

recipe(name="Cheddar Breadsticks", program="Dough", page=56, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="About 30 breadsticks",
       typ="Dough → oven", flavor="Savory", keyings=["Cheese"], attention=["Oven finish"],
       sections=[(None, [
           I("Water, room temperature", "water", "¾ cup"),
           I("Olive oil", "olive_oil", "⅓ cup", orig="⅓ cup (plus 1 tablespoon more for brushing)"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Granulated sugar", "sugar", "½ teaspoon"),
           I("Bread flour", "bread_flour", "3 cups"),
           I("Sharp cheddar, shredded", "cheddar", "1 cup"),
           I("Paprika", "paprika", "1 teaspoon"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2¼ teaspoons"),
           I("Olive oil, for brushing", "olive_oil", "1 tablespoon", tag="top", orig="(the extra 1 tablespoon above)"),
       ])],
       steps=[FIRST_EXCEPT.format(x="brushing oil"), DOUGH_GO,
              "When the cycle ends, punch the dough down on a lightly floured surface. Line 2 baking sheets with parchment.",
              "Roll it into a ¼-inch-thick rectangle about 10 × 22 in, long side left to right. Cut ½-in strips, twist each into a tight spiral, and lay them on the sheets ½–1 in apart. Cover and rest about 30 min.",
              "Heat the oven to **375°F** with racks in the lower and upper positions.",
              "Brush with olive oil and bake 15–20 min until golden, swapping the pans halfway. Cool slightly and serve."],
       nutrition="Per breadstick: 61 cal (26% from fat) · carb 9 g · protein 3 g · fat 2 g · sat fat 1 g · chol 4 mg · sodium 142 mg · calcium 27 mg · fiber 1 g")

recipe(name="Pizza Dough", program="Dough", page=57, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="1½ lb dough",
       typ="Dough → oven", flavor="Savory", keyings=["Whole grain"], attention=["Oven finish"],
       sections=[(None, [
           I("Water, room temperature", "water", "1 cup"),
           I("Honey", "honey", "1 teaspoon"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Extra-virgin olive oil", "olive_oil", "1½ tablespoons"),
           I("Bread flour*", "bread_flour", "2⅔ cups"),
           I("Whole wheat flour*", "ww_flour", "½ cup + 1 tablespoon"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "1¾ teaspoons"),
       ])],
       steps=[FIRST, DOUGH_GO,
              "When the cycle ends, take out the dough and use it in any pizza recipe, or see Pizza Margherita."],
       notes=["*All bread flour is fine. Swap the whole wheat for 68 g more bread flour (≈ the same volume)."],
       nutrition="Per serving (16 servings): 95 cal (13% from fat) · carb 13 g · protein 2 g · fat 1 g · sat fat 0 g · chol 0 mg · sodium 218 mg · calcium 2 mg · fiber 1 g")

recipe(name="Herb Focaccia", program="Dough", page=58, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="One 12 × 8-in focaccia (12 servings)",
       typ="Dough → oven", flavor="Savory", keyings=["Herbs", "Cheese"], attention=["Oven finish"],
       sections=[("Crust (goes in the pan)", [
           I("Water, room temperature", "water", "1 cup + 2 tablespoons"),
           I("Extra-virgin olive oil", "olive_oil", "2 tablespoons + 1 teaspoon"),
           I("Dry Italian herb blend*", "italian_herbs", "2¼ teaspoons"),
           I("Kosher salt", "salt", "1½ teaspoons"),
           I("Bread flour", "bread_flour", "3 cups + 3 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "1½ teaspoons"),
           I("Olive oil, for the pan", "none", "", tag="top"),
           I("Cornmeal, for dusting the pan", "none", "", tag="top"),
       ]), ("Topping", [
           I("Extra-virgin olive oil", "olive_oil", "3 tablespoons"),
           I("Kosher salt", "salt", "¾ teaspoon"),
           I("Parmesan, grated", "parmesan", "⅓ cup"),
           I("Fresh herbs, chopped, loosely packed (parsley, basil, oregano, thyme, marjoram)", "fresh_herbs", "¼ cup"),
       ])],
       steps=["Put the **crust** ingredients into the pan (paddle in) in the order listed; lock the pan in.", DOUGH_GO,
              "When the cycle ends, punch the dough down on a lightly floured surface and rest 10 min.",
              "Oil a shallow rimmed pan and dust it with cornmeal. Roll the dough to fit, put it in the pan, cover loosely, and let it rise somewhere warm until about doubled, 40–50 min.",
              "Heat the oven to **450°F**, rack in the middle. With oiled fingertips, press dimples ½ in deep and 1 in apart all over. Drizzle with the oil, then sprinkle the salt, Parmesan and herbs evenly.",
              "Bake 20–25 min, until deep golden and puffed with a crisp crust."],
       notes=["*DIY blend: equal parts dried basil, oregano, marjoram and thyme, plus a pinch of garlic powder."],
       nutrition="Per serving (12 servings): 169 cal (32% from fat) · carb 24 g · protein 6 g · fat 1 g · sat fat 1 g · chol 3 mg · sodium 487 mg · calcium 47 mg · fiber 1 g")

recipe(name="Pretzels", program="Dough", page=59, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="12 pretzels",
       typ="Dough → oven", flavor="Savory", keyings=[], attention=["Oven finish"],
       sections=[("Dough (goes in the pan)", [
           I("Water, room temperature", "water", "1 cup"),
           I("Kosher salt", "salt", "2 teaspoons"),
           I("Light brown sugar, packed", "brown_sugar", "1 tablespoon"),
           I("Bread flour", "bread_flour", "3¼ cups"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2¼ teaspoons"),
       ]), ("Baking-soda dip", [
           I("Water", "water", "2 cups"),
           I("Baking soda", "baking_soda", "2 tablespoons"),
           I("Coarse salt, for sprinkling", "none", "", tag="top"),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.",
              DOUGH_GO + " Line two baking sheets with parchment.",
              "When the cycle ends, cut the dough into 12 pieces (**about 57 g each**) and keep them covered. Roll each into a thin rope, twist into a pretzel, and set on the sheets. Cover and rest 20–30 min.",
              "Stir the 2 cups of water and the baking soda together in a small bowl.",
              "Bring a 6-qt pot of water to a boil. Heat the oven to **425°F**.",
              "Boil the pretzels one at a time for 3 min total, flipping at 1½ min. Drain on a rack, dip each in the soda solution, and return it to the sheet.",
              "Sprinkle with coarse salt and bake 15–20 min, until dark golden. Cool slightly on a rack."],
       nutrition="Per pretzel: 115 cal (0% from fat) · carb 25 g · protein 4 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 428 mg · calcium 1 mg · fiber 1 g")

recipe(name="Whole Wheat Kalamata Rolls", program="Dough", page=60, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="12 rolls (or 1 large oval loaf)",
       typ="Dough → oven", flavor="Savory", keyings=["Olives", "Herbs", "Whole grain"], attention=["Oven finish"],
       sections=[(None, [
           I("Whole milk, room temperature", "milk", "½ cup"),
           I("Water, room temperature", "water", "¼ cup + 2 tablespoons"),
           I("Olive oil", "olive_oil", "1 tablespoon"),
           I("Kosher salt", "salt", "½ teaspoon"),
           I("Granulated sugar", "sugar", "1 tablespoon"),
           I("Whole wheat flour", "ww_flour", "1½ cups"),
           I("Bread flour", "bread_flour", "1½ cups"),
           I("Kalamata olives, pitted, roughly chopped", "olives", "½ cup"),
           I("Herbes de Provence", "herbes_provence", "1 teaspoon"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2¼ teaspoons"),
       ])],
       steps=[FIRST, DOUGH_GO,
              "When the cycle ends, turn the dough out onto a lightly floured surface. Line a baking sheet with parchment.",
              "Cut into 12 pieces, roll each into an oval, and set them on the sheet. Cover and let rise about 30 min, until roughly doubled. Heat the oven to **350°F**.",
              "Cut 2 small slashes across each roll and dust with whole wheat flour. Bake 15–20 min, until dark golden. Cool on a rack."],
       notes=["For one large oval loaf, shape it the same way and bake about 10 min longer."],
       nutrition="Per roll: 147 cal (17% from fat) · carb 26 g · protein 5 g · fat 3 g · sat fat 0 g · chol 1 mg · sodium 141 mg · calcium 22 mg · fiber 3 g")

recipe(name="Garlic, Herb and Cheese Knots", program="Dough", page=61, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="12 knots",
       typ="Dough → oven", flavor="Savory", keyings=["Herbs"], attention=["Oven finish"],
       sections=[("Dough (goes in the pan)", [
           I("Water, room temperature", "water", "1 cup"),
           I("Olive oil", "olive_oil", "1½ tablespoons"),
           I("Kosher salt", "salt", "1 teaspoon"),
           I("Bread flour", "bread_flour", "3 cups"),
           I("Nonfat dry milk powder", "dry_milk", "¼ cup"),
           I("Potato flakes", "potato_flakes", "2 tablespoons"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2 teaspoons"),
       ]), ("For shaping", [
           I("Garlic powder (sprinkled on the dough)", "garlic_powder", "2 teaspoons", orig="2 teaspoons (listed with the dough; used at shaping)"),
       ]), ("Seasoning (brushed on after baking)", [
           I("Unsalted butter", "butter", "2 tablespoons"),
           I("Large garlic cloves, finely chopped", "garlic_clove", "3"),
           I("Fresh mixed herbs (oregano, thyme, parsley), finely chopped", "fresh_herbs", "1 tablespoon"),
           I("Kosher salt", "salt", "¼ teaspoon"),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.", DOUGH_GO,
              "When the cycle ends, turn the dough out onto a lightly floured surface and sprinkle garlic powder on all sides. Line a baking sheet with parchment.",
              "Cut into 12 pieces and keep them covered. Roll each into a 10-in rope and tie it in a knot. Set on the sheet, cover loosely, and rest about 30 min. Heat the oven to **350°F**.",
              "Meanwhile, melt the butter in a small saucepan over medium heat. Off the heat, stir in the garlic, herbs and salt.",
              "Bake the knots 15–18 min until lightly browned, brush with the garlic butter right away, and cool 5–10 min before serving."],
       notes=["The booklet's title says cheese, but there's no cheese in its ingredient list. A little grated Parmesan on the warm knots works well if you want it."],
       nutrition="Per knot: 148 cal (22% from fat) · carb 25 g · protein 5 g · fat 4 g · sat fat 1 g · chol 6 mg · sodium 258 mg · calcium 38 mg · fiber 1 g")

recipe(name="Cinnamon Swirl Rolls", program="Dough", page=62, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="16 rolls (13 × 9-in pan)",
       typ="Dough → oven", flavor="Sweet", keyings=["Spice"], attention=["Oven finish"],
       sections=[("Dough (goes in the pan)", [
           I("Low-fat milk, room temperature", "milk", "½ cup"),
           I("Large eggs, room temperature", "egg", "2"),
           I("Unsalted butter, room temperature, cubed", "butter", "4 tablespoons"),
           I("Granulated sugar", "sugar", "⅓ cup"),
           I("Kosher salt", "salt", "¾ teaspoon"),
           I("Pure vanilla extract", "vanilla", "1 teaspoon"),
           I("Bread flour", "bread_flour", "3 cups"),
           I("Cornstarch", "cornstarch", "⅓ cup"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "1¾ teaspoons"),
       ]), ("Filling", [
           I("Light brown sugar, packed", "brown_sugar", "⅓ cup"),
           I("Granulated sugar", "sugar", "3 tablespoons"),
           I("Ground cinnamon", "cinnamon", "2 teaspoons"),
           I("Unsalted butter, melted (for brushing)", "butter", "3 tablespoons"),
       ]), ("Frosting", [
           I("Cream cheese, room temperature", "cream_cheese", "3 ounces"),
           I("Unsalted butter, room temperature", "butter", "3 tablespoons"),
           I("Pure vanilla extract", "vanilla", "¾ teaspoon"),
           I("Confectioners' sugar, sifted", "powdered_sugar", "1 cup + 2 tablespoons"),
           I("Low-fat milk", "milk", "2 teaspoons"),
       ]), ("Pan", [
           I("Nonstick cooking spray", "none", "", tag="top"),
       ])],
       steps=["Put the **dough** ingredients into the pan (paddle in) in the order listed; lock the pan in.", DOUGH_GO,
              "While it runs, stir the sugars and cinnamon together for the filling. Beat all the frosting ingredients until completely smooth (food processor or mixer).",
              "When the cycle ends, punch the dough down on a lightly floured surface, cut it in half, and rest it covered for 10 min. Spray a 13 × 9-in pan.",
              "Roll each half into a rectangle 12 in wide and ½ in thick. Brush with melted butter, leaving a 1-in strip bare along one long side. Sprinkle with the filling, roll up tightly toward the bare edge, and pinch to seal. Cut 8 slices from each log, arrange them in the pan, cover, and let rise 30 min. Heat the oven to **350°F**, rack in the middle.",
              "Bake 30–35 min, until puffed with lightly golden tops.",
              "Cool 20–25 min, then frost."],
       nutrition="Per roll: 243 cal (28% from fat) · carb 34 g · protein 5 g · fat 8 g · sat fat 5 g · chol 43 mg · sodium 161 mg · calcium 44 mg · fiber 1 g")

recipe(name="Basic Sweet Dough", program="Dough", page=64, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="1½ lb dough",
       typ="Dough → oven", flavor="Sweet", keyings=[], attention=["Oven finish"],
       sections=[(None, [
           I("Water, room temperature", "water", "¼ cup + 2 tablespoons"),
           I("Large eggs, room temperature", "egg", "2"),
           I("Kosher salt", "salt", "½ teaspoon"),
           I("Sour cream, room temperature", "sour_cream", "¼ cup"),
           I("Unsalted butter, room temperature, cubed", "butter", "¼ cup"),
           I("Granulated sugar", "sugar", "¼ cup"),
           I("Bread flour", "bread_flour", "3 cups"),
           I("Yeast (active dry, instant or bread machine)", "yeast", "2¼ teaspoons"),
       ])],
       steps=[FIRST, DOUGH_GO,
              "When the cycle ends, punch the dough down on a lightly floured surface and rest 10 min before using. It's made for sweet breakfast pastries like the Raspberry Cheese Danish."],
       nutrition="Per serving (24 servings): 87 cal (27% from fat) · carb 13 g · protein 3 g · fat 2 g · sat fat 2 g · chol 22 mg · sodium 57 mg · calcium 4 mg · fiber 1 g")

recipe(name="Raspberry Cheese Danish", program="Dough", page=65, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="2 large Danish (24 servings)",
       typ="Dough → oven", flavor="Sweet", keyings=["Fruit"], attention=["Oven finish"],
       sections=[("Dough", [
           I("Basic Sweet Dough", "ref_sweet_dough", "1 recipe", orig="1 recipe"),
       ]), ("Cream cheese filling", [
           I("Cream cheese, room temperature, cubed", "cream_cheese", "6 ounces"),
           I("Confectioners' sugar, sifted", "powdered_sugar", "3 tablespoons"),
           I("Kosher salt", "salt", "Pinch"),
           I("Large egg, room temperature", "egg", "1"),
           I("Pure vanilla extract", "vanilla", "¾ teaspoon"),
       ]), ("Assembly", [
           I("Seedless raspberry preserves", "jam", "½ cup"),
           I("Egg wash: 1 large egg + ½ teaspoon water", "egg", "1", orig="1 large egg beaten with ½ teaspoon water"),
       ]), ("Vanilla glaze (optional)", [
           I("Confectioners' sugar, sifted", "powdered_sugar", "¾ cup"),
           I("Pure vanilla extract", "vanilla", "½ teaspoon"),
           I("Low-fat milk, a few drops at a time (about ¼ cup max)", "milk", "¼ cup", orig="approximately ¼ cup"),
       ])],
       steps=["Make the **Basic Sweet Dough**. Line two baking sheets with parchment.",
              "While the dough runs, process the cream cheese, sugar, salt, egg and vanilla in a food processor until completely smooth. Keep it in the fridge.",
              "Cut the dough in half. Roll each piece into a rectangle about 14 × 10 in and put it on a sheet. Spread the filling down the center of each, then spoon the preserves on top.",
              "On both sides, cut ½-in strips from the dough's edge in to the filling. Fold the strips over the filling, alternating sides and crisscrossing into an X, until you reach the bottom. Heat the oven to **350°F**.",
              "Cover loosely and let rise until nearly doubled. Brush with egg wash and bake 30–40 min, until golden brown and the filling is set.",
              "While they bake, make the glaze if using: whisk milk a few drops at a time into the sugar and vanilla until it's thin enough to drizzle.",
              "Slide the parchment and Danish onto a rack, then pull the parchment out so the bottoms don't go soggy. Cool, then serve plain, dusted with sugar, or drizzled with glaze."],
       nutrition="Per serving (24 servings, with glaze): 152 cal (31% from fat) · carb 23 g · protein 5 g · fat 5 g · sat fat 3 g · chol 38 mg · sodium 93 mg · calcium 9 mg · fiber 1 g",
       links=["Basic Sweet Dough"])

# ---------------- JAM ----------------
JAM_STEPS = [FIRST, "Press **PROG** → **Jam**, then press **START/STOP** (1:20).",
             "**10–15 min in**, scrape down the pan with a spatula so everything mixes well.",
             "When it finishes, spoon into clean, dry jars, let cool, then cover. Keeps up to 3 weeks in the fridge."]

recipe(name="Strawberry Rhubarb Jam", program="Jam", page=67, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="About 4 cups", typ="Jam", flavor="Sweet", keyings=["Fruit"], attention=["Scrape pan"],
       sections=[(None, [
           I("Fresh strawberries, stemmed, quartered (halved if small)", "strawberries", "4 cups", orig="4 cups (1 pound)"),
           I("Fresh rhubarb, cut in ½-inch slices", "rhubarb", "12 ounces"),
           I("Granulated sugar", "sugar", "1 cup"),
           I("Powdered pectin", "pectin", "1 tablespoon"),
           I("Fresh lemon juice", "lemon_juice", "1 teaspoon"),
           I("Kosher salt", "salt", "Pinch"),
           I("Fresh basil, thinly sliced (optional)", "basil_fresh", "⅓ cup"),
       ])],
       steps=JAM_STEPS,
       nutrition="Per 2 tbsp: 32 cal (2% from fat) · carb 8 g · protein 0 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 6 mg · calcium 12 mg · fiber 1 g")

recipe(name="Pear & Ginger Preserves", program="Jam", page=68, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="3 cups", typ="Jam", flavor="Sweet", keyings=["Fruit", "Spice"], attention=["Scrape pan"],
       sections=[(None, [
           I("Pears (4 medium-large), peeled, cored, diced", "pears", "1¾ pounds", orig="4 medium to large pears, about 1¾ pounds"),
           I("Fresh ginger, grated", "ginger_fresh", "1 teaspoon"),
           I("Granulated sugar", "sugar", "1 cup"),
           I("Powdered pectin (one packet, ¼ cup)", "pectin", "¼ cup", orig="1 (¼ cup) packet"),
           I("Fresh lemon juice", "lemon_juice", "1 tablespoon"),
           I("Candied ginger, chopped", "candied_ginger", "2 tablespoons"),
           I("Kosher salt", "salt", "Pinch"),
       ])],
       steps=JAM_STEPS,
       notes=["The pears are weighed whole, before peeling and coring, so start with about 794 g of whole pears.",
              "One standard 1.75 oz (49 g) box of Sure-Jell is this recipe's \"¼ cup packet\"."],
       nutrition="Per 2 tbsp: 57 cal (1% from fat) · carb 15 g · protein 0 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 111 mg · calcium 3 mg · fiber 1 g")

recipe(name="Blueberry Lime Jam", program="Jam", page=69, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="About 4⅓ cups", typ="Jam", flavor="Sweet", keyings=["Fruit"], attention=["Scrape pan"],
       sections=[(None, [
           I("Fresh blueberries", "blueberries", "6 cups"),
           I("Granulated sugar", "sugar", "1¼ cups"),
           I("Powdered pectin", "pectin", "1 tablespoon"),
           I("Fresh lime juice", "lime_juice", "¼ cup"),
           I("Lime zest, grated", "lime_zest", "1 teaspoon"),
           I("Kosher salt", "salt", "Pinch"),
       ])],
       steps=JAM_STEPS,
       nutrition="Per 2 tbsp: 43 cal (2% from fat) · carb 11 g · protein 0 g · fat 0 g · sat fat 0 g · chol 0 mg · sodium 5 mg · calcium 2 mg · fiber 1 g")

recipe(name="Mixed Berry Jam", program="Jam", page=70, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="About 5 cups", typ="Jam", flavor="Sweet", keyings=["Fruit"], attention=["Scrape pan"],
       sections=[(None, [
           I("Fresh strawberries, stemmed, quartered (halved if small)", "strawberries", "4 cups"),
           I("Raspberries", "raspberries", "2 cups"),
           I("Blueberries", "blueberries", "2 cups"),
           I("Granulated sugar", "sugar", "1 cup"),
           I("Powdered pectin", "pectin", "1 tablespoon"),
           I("Fresh lemon juice", "lemon_juice", "1 teaspoon"),
       ])],
       steps=JAM_STEPS,
       notes=["The booklet's nutrition line for this jam (protein 2 g, sodium 116 mg) looks copied from another recipe, so treat it loosely."],
       nutrition="Per 2 tbsp (as printed): 77 cal (17% from fat) · carb 13 g · protein 2 g · fat 1 g · sat fat 1 g · chol 3 mg · sodium 116 mg · calcium 16 mg · fiber 0 g")

# ---------------- CAKE ----------------
CAKE_STEPS = ["Spray the inside of the pan (paddle in) with nonstick spray.",
              "Put everything into the pan **in the order listed** and lock the pan in.",
              "Press **PROG** → **Cake**, then press **START/STOP** (1:52).",
              "While it mixes, scrape down the sides with a rubber spatula so everything gets incorporated.",
              "When it finishes, turn the loaf onto a rack and cool completely before slicing. If the top is still a bit moist, leave it on Keep Warm for another 10–15 min first."]

recipe(name="Banana Walnut Bread", program="Cake", page=71, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="One 2⅓ lb loaf (12 servings)", typ="Quick bread", flavor="Sweet", keyings=["Nuts", "Fruit"], attention=["Scrape pan"],
       sections=[(None, [
           I("Nonstick cooking spray", "none", "", tag="top"),
           I("Low-fat buttermilk, room temperature", "buttermilk", "½ cup"),
           I("Unsalted butter, room temperature, cut into ½-inch pieces", "butter", "½ cup"),
           I("Large eggs, room temperature", "egg", "2"),
           I("Pure vanilla extract", "vanilla", "1 teaspoon"),
           I("Mashed ripe bananas (about 3 medium)", "banana", "1¼ cups"),
           I("Kosher salt", "salt", "¾ teaspoon"),
           I("Granulated sugar", "sugar", "1 cup"),
           I("Unbleached all-purpose flour", "ap_flour", "2 cups"),
           I("Baking soda", "baking_soda", "1 teaspoon"),
           I("Baking powder", "baking_powder", "¾ teaspoon"),
           I("Walnuts, chopped", "walnuts", "⅔ cup"),
       ])],
       steps=CAKE_STEPS,
       nutrition="Per serving (12): 285 cal (38% from fat) · carb 39 g · protein 5 g · fat 12 g · sat fat 5 g · chol 52 mg · sodium 296 mg · calcium 30 mg · fiber 2 g")

recipe(name="Sour Cream Chocolate Bread", program="Cake", page=72, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf (12 servings)", typ="Quick bread", flavor="Sweet", keyings=["Chocolate", "Nuts"], attention=["Scrape pan"],
       sections=[(None, [
           I("Nonstick cooking spray", "none", "", tag="top"),
           I("Low-fat milk, room temperature", "milk", "½ cup + 1 tablespoon"),
           I("Sour cream, room temperature", "sour_cream", "½ cup"),
           I("Large eggs, room temperature", "egg", "2"),
           I("Pure vanilla extract", "vanilla", "¾ teaspoon"),
           I("Granulated sugar", "sugar", "½ cup"),
           I("Light brown sugar, packed", "brown_sugar", "⅓ cup"),
           I("Unbleached all-purpose flour", "ap_flour", "1⅓ cups"),
           I("Baking powder", "baking_powder", "¾ teaspoon"),
           I("Baking soda", "baking_soda", "½ teaspoon"),
           I("Kosher salt", "salt", "½ teaspoon"),
           I("Chocolate chips", "choc_chips", "¾ cup"),
           I("Walnuts, chopped", "walnuts", "⅓ cup"),
       ])],
       steps=CAKE_STEPS,
       notes=["Despite the name, there's no cocoa in the batter. The chocolate comes from the chips."],
       nutrition="Per serving (12): 226 cal (34% from fat) · carb 34 g · protein 4 g · fat 9 g · sat fat 41 g (sic — as printed) · chol 38 mg · sodium 199 mg · calcium 33 mg · fiber 1 g")

recipe(name="Zucchini Bread", program="Cake", page=73, sizes=["Batch"], delay="No", ultrafast=False,
       yield_="One 1½ lb loaf (12 servings)", typ="Quick bread", flavor="Sweet", keyings=["Nuts", "Fruit", "Spice"], attention=["Scrape pan"],
       sections=[(None, [
           I("Nonstick cooking spray", "none", "", tag="top"),
           I("Vegetable oil", "veg_oil", "⅓ cup"),
           I("Zucchini, shredded", "zucchini", "¾ cup"),
           I("Large eggs, room temperature", "egg", "2"),
           I("Light brown sugar, packed", "brown_sugar", "⅓ cup"),
           I("Granulated sugar", "sugar", "3 tablespoons"),
           I("Unbleached all-purpose flour", "ap_flour", "1½ cups"),
           I("Kosher salt", "salt", "¾ teaspoon"),
           I("Ground cinnamon", "cinnamon", "¾ teaspoon"),
           I("Ground allspice", "allspice", "¼ teaspoon"),
           I("Baking soda", "baking_soda", "½ teaspoon"),
           I("Baking powder", "baking_powder", "½ teaspoon"),
           I("Walnuts", "walnuts", "⅓ cup"),
           I("Raisins", "raisins", "⅓ cup"),
       ])],
       steps=CAKE_STEPS,
       notes=["Shredded zucchini packs differently every time; the grams use about 135 g/cup. Don't squeeze it dry, the batter counts on that moisture."],
       nutrition="Per serving (12): 183 cal (43% from fat) · carb 23 g · protein 4 g · fat 9 g · sat fat 1 g · chol 31 mg · sodium 228 mg · calcium 15 mg · fiber 1 g")

# ---------------- BONUS (no machine) ----------------
recipe(name="Breadcrumbs", program="No machine", page=74, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="4 cups from a 1 lb loaf", typ="Uses leftover bread", flavor="Savory", keyings=[], attention=["Overnight prep"],
       sections=[(None, [
           I("Basic White Bread (1 lb loaf)", "ref_white", "1 loaf"),
       ]), ("Seasoned version (optional)", [
           I("Dried oregano", "oregano_dried", "¼ teaspoon"),
           I("Dried basil", "basil_dried", "¼ teaspoon"),
           I("Garlic powder", "garlic_powder", "¼ teaspoon"),
           I("Dried onion flakes, ground", "onion_flakes", "¼ teaspoon"),
       ])],
       steps=["Break the loaf into large pieces and leave them out uncovered overnight.",
              "Pulse in a food processor to break them up, then run it 40–60 s until finely ground. For seasoned crumbs, add the herbs and spices to the bread first."],
       nutrition="Per 2 tbsp: 48 cal (15% from fat) · carb 9 g · protein 1 g · fat 1 g · sat fat 1 g · chol 2 mg · sodium 95 mg · calcium 5 mg · fiber 0 g",
       links=["Basic White Bread"])

recipe(name="Croutons", program="No machine", page=74, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="6 cups from a 1 lb loaf", typ="Uses leftover bread", flavor="Savory", keyings=[], attention=["Oven finish"],
       sections=[(None, [
           I("Basic White Bread (1 lb loaf)", "ref_white", "1 loaf"),
           I("Olive oil", "olive_oil", "1 to 2 tablespoons"),
           I("Kosher salt", "salt", "Pinch"),
       ])],
       steps=["Heat the oven to **325°F**.",
              "Cut the bread into ½-in cubes and toss with the oil in a large bowl. Spread on a rimmed sheet in a single layer (use 2 pans if needed) and sprinkle evenly with salt.",
              "Bake about 20 min, until golden brown."],
       nutrition="Per ¼ cup: 69 cal (22% from fat) · carb 12 g · protein 2 g · fat 2 g · sat fat 1 g · chol 3 mg · sodium 132 mg · calcium 7 mg · fiber 0 g",
       links=["Basic White Bread"])

recipe(name="Challah French Toast", program="No machine", page=75, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="8–10 slices", typ="Uses leftover bread", flavor="Sweet", keyings=["Spice"], attention=[],
       sections=[(None, [
           I("Large eggs", "egg", "8"),
           I("Milk (any kind)", "milk", "2 cups"),
           I("Pure vanilla extract", "vanilla", "1 tablespoon"),
           I("Pure maple syrup", "maple", "2 tablespoons"),
           I("Ground cinnamon", "cinnamon", "1 teaspoon"),
           I("Ground nutmeg", "nutmeg", "Pinch"),
           I("Kosher salt", "salt", "1 to 2 pinches"),
           I("Challah, sliced ¾ inch thick", "ref_challah", "8 to 10 slices"),
           I("Butter or coconut oil, for the griddle", "none", "", tag="top"),
           I("Confectioners' sugar, fresh fruit and maple syrup, to serve", "none", "", tag="top"),
       ])],
       steps=["Whisk the eggs, milk, vanilla, maple syrup, cinnamon, nutmeg and salt in a bowl, then pour into a 13 × 9-in dish.",
              "Soak half the bread, turning so both sides are saturated.",
              "Heat a griddle over medium to medium-high and add about 1 tbsp butter or oil.",
              "Cook the soaked slices 3½–4 min per side. Soak the second batch while the first cooks.",
              "Keep cooked slices warm in a low oven while you finish the rest.",
              "Serve dusted with confectioners' sugar, with fruit and maple syrup."],
       nutrition="Per slice (10 slices): 189 cal (37% from fat) · carb 23 g · protein 6 g · fat 8 g · sat fat 4 g · chol 170 mg · sodium 174 mg · calcium 81 mg · fiber 1 g",
       links=["Challah Loaf"])

recipe(name="Berry Brioche Bread Pudding", program="No machine", page=76, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="6–8 servings (9-in round pan)", typ="Uses leftover bread", flavor="Sweet", keyings=["Fruit"], attention=["Overnight prep", "Oven finish"],
       sections=[(None, [
           I("Brioche, cut into 1-inch cubes (about 10 cups)", "ref_brioche", "1 pound", orig="1 loaf (1 pound), about 10 cups cubed"),
           I("Large eggs, lightly beaten", "egg", "4"),
           I("Granulated sugar", "sugar", "¼ cup"),
           I("Kosher salt", "salt", "½ teaspoon"),
           I("Whole milk", "milk", "1½ cups"),
           I("Heavy cream", "cream", "1½ cups"),
           I("Pure vanilla extract", "vanilla", "2 teaspoons"),
           I("Mixed berry jam (homemade or store-bought)", "jam", "1 cup"),
           I("Nonstick spray or softened butter, for the pan", "none", "", tag="top"),
           I("Whipped cream, to serve", "none", "", tag="top"),
       ])],
       steps=["Put the bread cubes in a large bowl.",
              "Whisk the eggs, sugar and salt until light and frothy, then whisk in the milk, cream and vanilla. Pour over the bread and stir gently to coat. Cover and refrigerate **at least 3 hours**, or overnight.",
              "Let it come to room temperature, then gently fold in the jam.",
              "Heat the oven to **350°F**, rack in the lower third. Grease a 9-in round pan and add the bread mixture.",
              "Bake loosely covered with foil for 1 hour, then uncovered about 15 min more, until puffed. It's done at an internal **160°F**. Serve right away with whipped cream."],
       nutrition="Per serving (8): 507 cal (46% from fat) · carb 56 g · protein 10 g · fat 25 g · sat fat 16 g · chol 215 mg · sodium 418 mg · calcium 94 mg · fiber 1 g",
       links=["Brioche Loaf", "Mixed Berry Jam"])

recipe(name="Pizza Margherita", program="No machine", page=77, sizes=["Batch"], delay="n/a", ultrafast=False,
       yield_="9 servings (rimmed baking tray)", typ="Uses leftover bread", flavor="Savory", keyings=["Cheese", "Herbs"], attention=["Oven finish"],
       sections=[(None, [
           I("Olive oil, divided (1 tsp pan · 2 tbsp sauce · rest for edges)", "olive_oil", "3 tablespoons", orig="3 tablespoons, divided"),
           I("Cornmeal, for dusting the pan", "none", "", tag="top"),
           I("Pizza Dough, room temperature", "ref_pizza", "1 recipe", orig="1 recipe (booklet p. 57)"),
           I("Dried basil", "basil_dried", "½ teaspoon"),
           I("Dried oregano", "oregano_dried", "¼ teaspoon"),
           I("Crushed red pepper", "red_pepper", "¼ teaspoon"),
           I("Whole peeled tomatoes, drained (1 large can)", "tomatoes", "28 ounces", orig="1 large can (28 ounces)"),
           I("Kosher salt", "salt", "½ teaspoon"),
           I("Fresh mozzarella, cut into 9 slices", "mozzarella", "8 ounces"),
           I("Fresh basil leaves, to garnish", "none", "", tag="top"),
       ])],
       steps=["Heat the oven to **450°F**, rack in the lower third.",
              "Brush a rimmed tray with 1 tsp of the oil (4 g) and dust with cornmeal. Stretch the dough evenly into the tray, cover, and let rise 30 min.",
              "Meanwhile, make the sauce: heat 2 tbsp of the oil (25 g) with the basil, oregano and red pepper in a small saucepan over medium-high. Add the drained tomatoes carefully and crush them with a wooden spoon as they heat. Once simmering, lower to medium and simmer 20–30 min to reduce slightly. Off the heat, stir in the salt.",
              "Spread the sauce over the dough, leaving a 1-in border. Lay the mozzarella in 3 rows of 3 and brush the edges with the remaining oil.",
              "Bake about 25 min, until the cheese has melted, the crust is golden and the bottom crisp. Garnish with basil."],
       notes=["The 28 oz is the can's labeled weight. Drained, you'll have roughly 500 g of tomatoes."],
       nutrition="(none listed)",
       links=["Pizza Dough"])
