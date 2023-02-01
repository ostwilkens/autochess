#%%
from data import all_units, all_combos
from math import floor, ceil


def score_lineup(units):
    bonus_score = 0

    # sum traits
    traits = [x["races"] for x in units] + [x["classes"] for x in units]
    # flatten traits
    traits = [item for sublist in traits for item in sublist]
    # count traits
    traits = {x: traits.count(x) for x in traits}

    # if we have 2 wizards, reduce all 4+ traits reqs by 1
    if "Wizard" in traits:
        has_2_wizards = traits["Wizard"] >= 2

        if has_2_wizards:
            for trait in traits:
                if traits[trait] >= 3:
                    traits[trait] += 1
                    # print(f"WIZARD: trait {trait} increased to {traits[trait]}")

    # if we have 2 demon hunters, demons are good
    if "Demon Hunter" in traits and "Demon" in traits:
        has_2_dhs = traits["Demon Hunter"] >= 2

        if has_2_dhs:
            bonus_score += traits["Demon"]

    # if we have 3 undead, -score for every non-undead
    if "Undead" in traits and traits["Undead"] >= 3:
        undeads = traits["Undead"]
        non_undeads = len(units) - undeads
        bonus_score -= non_undeads

    # find matching combos
    all_matched_combos = []
    for trait in traits:
        count = traits[trait]
        matches = [x for x in all_combos if x["requirement"][1] == trait and count >= x["requirement"][0]]
        all_matched_combos.extend(matches)

    # count tier
    combo_score = sum([x["tier"] for x in all_matched_combos])
    unit_score = sum([x["tier"] for x in units])

    total_score = combo_score + unit_score + bonus_score
    return total_score



def solve(unavailable_units, owned_units, max_units, max_cost):
    # flesh out current_units
    current_units = []
    for name in owned_units:
        for unit in all_units:
            if unit["name"] == name:
                current_units.append(unit)
                break

    missing_unit_count = max_units - len(current_units)
    # available_units = [x for x in all_units if x["cost"] <= max_cost and x["name"] not in current_units and x["name"] not in unavailable_units]

    unit_combinations = []
    unit_combination_hashes = []

    def recurse(current_units, available_units, max_units, max_cost):
        if len(current_units) == max_units:

            combo_hash = str([x["name"] for x in current_units])

            if combo_hash not in unit_combination_hashes:
                unit_combination_hashes.append(combo_hash)
                unit_combinations.append(current_units)
            
            return
        
        available_units = [x for x in all_units if x["cost"] <= max_cost and x["name"] not in current_units and x["name"] not in unavailable_units]

        for new_unit in available_units:
            if new_unit["name"] not in [x["name"] for x in current_units]:
                new_unit_combination = current_units + [new_unit]

                # sort new_unit_combination by name
                new_unit_combination = sorted(new_unit_combination, key=lambda x: x["name"])

                recurse(new_unit_combination, available_units, max_units, max_cost)


    recurse(current_units, None, max_units, max_cost)
    # recurse(current_units, available_units, max_units, max_cost)

    # score combinations
    scores = []
    for combination in unit_combinations:
        score = score_lineup(combination)
        scores.append(score)

    # zip scores and unit_combinations
    scores_and_combos = zip(scores, unit_combinations)
    # sort by score
    scores_and_combos = sorted(scores_and_combos, key=lambda x: x[0], reverse=True)
    

    unit_attractiveness = {}

    top_score = max(scores)
    for scored_combo in scores_and_combos:
        score, units = scored_combo
        
        unit_names = [x["name"] for x in units if x["name"] not in owned_units]

        if score == top_score:
            print(f"{score}: {', '.join(unit_names)}")

        for unit_name in unit_names:
            unit_score = 0
            if score == top_score:
                unit_score += 3
            elif score == top_score - 1:
                unit_score += 1

            if unit_name not in unit_attractiveness:
                unit_attractiveness[unit_name] = 0
            
            unit_attractiveness[unit_name] += unit_score

    # as tuples
    unit_attractiveness = [(x, unit_attractiveness[x]) for x in unit_attractiveness]

    # sort by score
    unit_attractiveness = sorted(unit_attractiveness, key=lambda x: x[1], reverse=True)

    return unit_attractiveness



# user input
unavailable_units = ["Disruptor", "Invoker", "Templar Assassin", "Troll Warlord", "Techies", "Tidehunter", "Queen of Pain", "Arc Warden"]
owned_units = ["Dragon Knight", "Huskar", "Juggernaut", "Rubick", "Slardar", "Naga Siren", "Chaos Knight", "Axe", "Mars", "Warlock"]

# max_units = min(10, len(owned_units) + 3)
max_units = min(10, len(owned_units) + 2)
max_cost = min(4, 1+floor(len(owned_units)/2))

if max_cost == 1:
    max_units += 1

if len(unavailable_units) > 0 and max_units == 10 and max_cost == 4:
    max_cost = 5

print(f"Max cost: {max_cost}")
print(f"Max units: {max_units}\n")

print("Best additions:")
recs = solve(unavailable_units, owned_units, max_units, max_cost)
print("\nPotential:")
for rec in [x for x in recs if x[1] > 0][:5]:
    print(f"{rec[0]}: {rec[1]}")


#%%
# which could be removed?
for i in range(0, len(owned_units)):
    new_owned_units = owned_units.copy()

    
    max_units = min(10, len(new_owned_units) + 2)
    max_cost = min(4, 1+floor(len(new_owned_units)/2))

    if max_cost == 1:
        max_units += 1

    if len(unavailable_units) > 0 and max_units == 10 and max_cost == 4:
        max_cost = 5


    print(f"-{new_owned_units[i]}")
    del new_owned_units[i]
    recs = solve(unavailable_units, new_owned_units, max_units, max_cost)
    # print(new_owned_units)