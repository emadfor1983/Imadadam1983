import random
import time

class RobinHoodGame:
    def __init__(self):
        self.gold = 0
        self.reputation = 0
        self.arrows = 10
        self.poor_helped = 0

    def display_status(self):
        print(f"\n{'='*50}")
        print(f"Gold: {self.gold} | Reputation: {self.reputation} | Arrows: {self.arrows} | Poor Helped: {self.poor_helped}")
        print(f"{'='*50}\n")

    def archery_challenge(self):
        print("\n🏹 ARCHERY CHALLENGE 🏹")
        print("Aim at the target! Enter a number between 1-10")
        print("The closer to the bullseye (random target), the better!")

        if self.arrows <= 0:
            print("You're out of arrows! Skip this challenge.")
            return False

        target = random.randint(1, 10)

        try:
            aim = int(input("Your aim (1-10): "))
            if aim < 1 or aim > 10:
                print("Invalid aim! Must be between 1-10.")
                return False
        except ValueError:
            print("Invalid input!")
            return False

        self.arrows -= 1
        distance = abs(target - aim)

        print(f"Target was at: {target}")

        if distance == 0:
            print("🎯 BULLSEYE! Perfect shot!")
            reward = random.randint(30, 50)
            self.gold += reward
            self.reputation += 10
            print(f"You found {reward} gold on the target!")
            return True
        elif distance <= 2:
            print("✓ Great shot! Very close!")
            reward = random.randint(15, 25)
            self.gold += reward
            self.reputation += 5
            print(f"You found {reward} gold!")
            return True
        elif distance <= 4:
            print("○ Decent shot!")
            reward = random.randint(5, 15)
            self.gold += reward
            self.reputation += 2
            print(f"You found {reward} gold.")
            return True
        else:
            print("✗ Missed! Better luck next time.")
            return False

    def rob_the_rich(self):
        print("\n💰 ROB THE RICH 💰")
        print("You spot a wealthy noble's carriage!")
        print("1. Ambush directly (risky but more gold)")
        print("2. Sneak attack (safer but less gold)")
        print("3. Let them pass (no risk, no reward)")

        choice = input("Your choice (1-3): ").strip()

        if choice == "1":
            success_chance = random.randint(1, 100)
            if success_chance > 40:
                loot = random.randint(40, 80)
                self.gold += loot
                self.reputation += 8
                print(f"Success! You ambushed the carriage and took {loot} gold!")
                return True
            else:
                lost_gold = min(20, self.gold)
                self.gold -= lost_gold
                self.reputation -= 5
                print(f"Failed! The guards fought back. Lost {lost_gold} gold and some reputation.")
                return False
        elif choice == "2":
            success_chance = random.randint(1, 100)
            if success_chance > 20:
                loot = random.randint(20, 40)
                self.gold += loot
                self.reputation += 5
                print(f"Success! You sneaked away with {loot} gold!")
                return True
            else:
                self.reputation -= 2
                print("Failed! You were spotted but managed to escape.")
                return False
        elif choice == "3":
            print("You let the carriage pass. Sometimes wisdom is better than risk.")
            self.reputation += 1
            return True
        else:
            print("Invalid choice!")
            return False

    def help_the_poor(self):
        print("\n❤️  HELP THE POOR ❤️")
        print(f"You encounter a poor family in need.")
        print(f"Your current gold: {self.gold}")

        if self.gold < 10:
            print("You don't have enough gold to help them. (Need at least 10 gold)")
            return False

        print("How much gold will you give? (minimum 10)")

        try:
            donation = int(input("Gold to donate: "))
            if donation < 10:
                print("Minimum donation is 10 gold!")
                return False
            if donation > self.gold:
                print("You don't have that much gold!")
                return False
        except ValueError:
            print("Invalid amount!")
            return False

        self.gold -= donation
        self.poor_helped += 1
        reputation_gain = donation // 5
        self.reputation += reputation_gain

        print(f"The family is grateful! Your reputation increased by {reputation_gain}!")
        print("'Bless you, Robin Hood!' they say.")
        return True

    def find_arrows(self):
        print("\n🏹 ARROW SEARCH 🏹")
        print("You search the forest for arrows...")
        time.sleep(1)

        found = random.randint(2, 5)
        self.arrows += found
        print(f"You found {found} arrows!")
        return True

    def play_round(self):
        print("\n" + "="*50)
        print("What will Robin Hood do?")
        print("="*50)
        print("1. Archery Challenge")
        print("2. Rob the Rich")
        print("3. Help the Poor")
        print("4. Search for Arrows")
        print("5. View Status")
        print("6. End Adventure")

        choice = input("\nYour choice: ").strip()

        if choice == "1":
            self.archery_challenge()
        elif choice == "2":
            self.rob_the_rich()
        elif choice == "3":
            self.help_the_poor()
        elif choice == "4":
            self.find_arrows()
        elif choice == "5":
            self.display_status()
        elif choice == "6":
            return False
        else:
            print("Invalid choice!")

        return True

    def final_score(self):
        print("\n" + "="*50)
        print("ADVENTURE COMPLETE!")
        print("="*50)
        print(f"Final Gold: {self.gold}")
        print(f"Final Reputation: {self.reputation}")
        print(f"Poor Families Helped: {self.poor_helped}")
        print(f"Arrows Remaining: {self.arrows}")

        total_score = self.gold + (self.reputation * 2) + (self.poor_helped * 20)
        print(f"\nTotal Score: {total_score}")

        if total_score >= 200:
            print("🏆 LEGENDARY HERO! You're a true Robin Hood!")
        elif total_score >= 150:
            print("⭐ GREAT HERO! The people sing songs about you!")
        elif total_score >= 100:
            print("✓ GOOD OUTLAW! You've helped many people!")
        elif total_score >= 50:
            print("○ DECENT EFFORT! Keep helping the poor!")
        else:
            print("✗ NEEDS IMPROVEMENT! Robin Hood would do better!")

def main():
    print("="*50)
    print("🏹  WELCOME TO ROBIN HOOD ADVENTURE  🏹")
    print("="*50)
    print("\nSteal from the rich, give to the poor!")
    print("Build your reputation as a legendary outlaw!\n")

    game = RobinHoodGame()
    game.display_status()

    while True:
        if not game.play_round():
            break
        game.display_status()

    game.final_score()
    print("\nThanks for playing! 🏹")

if __name__ == "__main__":
    main()
