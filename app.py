import os
import sys

# Storage dictionary structure for tracking student data
students_db = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def show_menu():
    print("=" * 45)
    print("    🎓 STUDENT GRADING & ANALYTICS CLI 🎓    ")
    print("=" * 45)
    print(" 1. Add New Student Profile")
    print(" 2. Enter/Record Assignment Score")
    print(" 3. View Classroom Statistical Summary")
    print(" 4. Search and Generate Individual Report Card")
    print(" 5. Shutdown Analytics Engine")
    print("=" * 45)

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select analytical protocol [1-5]: ").strip()
        
        if choice == '1':
            clear_screen()
            print("--- REGISTER NEW STUDENT ---")
            name = input("Enter unique student full name: ").strip()
            if not name:
                print("❌ Name parameter cannot remain null.")
                input("\nPress Enter to return...")
                continue
            if name in students_db:
                print("❌ Student file registry collision. Name exists.")
                input("\nPress Enter to return...")
                continue
                
            students_db[name] = []
            print(f"\n✅ Profile folder instantiated for '{name}' successfully.")
            input("\nPress Enter to return...")
            
        elif choice == '2':
            clear_screen()
            print("--- LOG PERFORMANCE DATA ---")
            if not students_db:
                print("\n[ Database empty. Register students first ]")
                input("\nPress Enter to return...")
                continue
                
            name = input("Enter student name to update: ").strip()
            if name not in students_db:
                print("❌ Name not found in system logs.")
                input("\nPress Enter to retry...")
                continue
                
            try:
                score = float(input(f"Enter evaluation numerical score (0-100) for {name}: "))
                if score < 0 or score > 100:
                    print("❌ Metrics bounds restriction: Must range between 0 and 100.")
                    input("\nPress Enter to return...")
                    continue
            except ValueError:
                print("❌ Invalid float numerical input format.")
                input("\nPress Enter to return...")
                continue
                
            students_db[name].append(score)
            print(f"\n✅ Registered performance rating of {score}% to student ledger.")
            input("\nPress Enter to return...")
            
        elif choice == '3':
            clear_screen()
            print("--- CLASSROOM STATISTICAL SUMMARY ---")
            if not students_db:
                print("\n[ Empty database matrix ]")
                input("\nPress Enter to return...")
                continue
                
            all_scores = []
            print(f"{'STUDENT NAME':<20} | {'GRADES RECORDED':<15} | {'CURRENT GPA':<12}")
            print("-" * 53)
            
            for student, scores in students_db.items():
                if not scores:
                    print(f"{student:<20} | {'No entries':<15} | {'N/A':<12}")
                else:
                    avg = sum(scores) / len(scores)
                    all_scores.append(avg)
                    print(f"{student:<20} | {len(scores):<15} | {avg:>5.1f}% ({get_letter_grade(avg)})")
                    
            print("-" * 53)
            if all_scores:
                class_avg = sum(all_scores) / len(all_scores)
                print(f"Aggregated Class GPA: {class_avg:.2f}% ({get_letter_grade(class_avg)})")
                print(f"Highest Individual Avg: {max(all_scores):.1f}%")
                print(f"Lowest Individual Avg:  {min(all_scores):.1f}%")
            else:
                print("Insufficient metric vectors compiled to compute analytics averages.")
            print("-" * 53)
            input("\nPress Enter to return to main menu...")
            
        elif choice == '4':
            clear_screen()
            print("--- GENERATE INDIVIDUAL INDICES REPORT ---")
            name = input("Enter student profile lookup string: ").strip()
            if name in students_db:
                scores = students_db[name]
                print(f"\nOfficial Report Card Ledger: {name}")
                print("=" * 40)
                if not scores:
                    print("No recorded raw evaluation profiles inside this semester container.")
                else:
                    for i, score in enumerate(scores, 1):
                        print(f" Assessment {i:02d}: {score:>5.1f}% -> Mark: {get_letter_grade(score)}")
                    avg = sum(scores) / len(scores)
                    print("-" * 40)
                    print(f" Final Compiled Metric Average: {avg:.1f}%")
                    print(f" Course Assignment Standing:   Grade [{get_letter_grade(avg)}]")
                print("=" * 40)
            else:
                print("❌ No matching analytical identifier matches profile name.")
            input("\nPress Enter to return...")
            
        elif choice == '5':
            clear_screen()
            print("Shutting down Analytics pipeline. Data successfully closed.")
            sys.exit()
        else:
            print("❌ Input parsing overflow. Select numbers [1-5].")
            input("\nPress Enter to restart runtime workflow...")

if __name__ == "__main__":
    main()
