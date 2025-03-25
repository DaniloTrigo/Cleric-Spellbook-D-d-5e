import requests

def display_spell(spell_data):
    print(f"Name: {spell_data['name']}")
    print(f"Level: {spell_data['level']}")
    print(f"Index: {spell_data['index']}")
    print(f"URL: {spell_data['url']}")
    print("Description:")
    print(" ".join(spell_data.get('desc', ['No description available.'])))
    print()
    print(f"Range: {spell_data.get('range', 'N/A')}")
    print(f"Casting Time: {spell_data.get('casting_time', 'N/A')}")
    print(f"Duration: {spell_data.get('duration', 'N/A')}")
    print(f"Concentration: {'Yes' if spell_data.get('concentration', False) else 'No'}")
    print(f"Components: {', '.join(spell_data.get('components', []))}")
    if 'material' in spell_data:
        print(f"Material: {spell_data['material']}")
    
    # Adding spell scaling details
    if 'higher_level' in spell_data and spell_data['higher_level']:
        print("Higher Levels:")
        print(" ".join(spell_data['higher_level']))
    print()

def get_cleric_spells():
    url = "https://www.dnd5eapi.co/api/classes/cleric/spells"
    headers = {'Accept': 'application/json'}
    
    print("Fetching Cleric spell list...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        spells_data = response.json()
        all_spells = spells_data.get('results', [])
        
        if not all_spells:
            print("No Cleric spells found in API response.")
            return []
        
        detailed_spells = []
        for spell in all_spells:
            spell_details_url = f"https://www.dnd5eapi.co{spell['url']}"
            print(f"Fetching details for {spell['name']}...")
            spell_details_response = requests.get(spell_details_url, headers=headers)
            
            if spell_details_response.status_code == 200:
                spell_data = spell_details_response.json()
                detailed_spells.append(spell_data)
            else:
                print(f"Failed to fetch details for {spell['name']} - Status Code: {spell_details_response.status_code}")
        
        print(f"Total Cleric Spells Found: {len(detailed_spells)}")
        return detailed_spells
    else:
        print(f"Failed to retrieve Cleric spell list - Status Code: {response.status_code}")
        return []

def main():
    cleric_spells = get_cleric_spells()
    
    if not cleric_spells:
        print("No spells found or failed to retrieve data.")
        return
    
    print("Welcome to the D&D 5e Cleric Spellbook!")
    print(f"Total Cleric Spells: {len(cleric_spells)}\n")
    
    while True:
        print("Commands:")
        print("1 - List all Cleric spells")
        print("2 - Search for a spell by name")
        print("3 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nList of Cleric Spells:")
            for spell in cleric_spells:
                display_spell(spell)
        elif choice == '2':
            spell_name = input("Enter the spell name: ").lower()
            matching_spells = [spell for spell in cleric_spells if spell_name in spell['name'].lower()]
            if matching_spells:
                print("\nMatching Cleric Spells:")
                for spell in matching_spells:
                    display_spell(spell)
            else:
                print("No matching Cleric spells found.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
