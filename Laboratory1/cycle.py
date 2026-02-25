from longest_peak import longest_peak

def analyze_training():
    print("=== Аналіз потужності велосипедиста ===")
    print("Мета: знайти найдовший цикл (підйом, пік, спад).")
    
    try:
        user_input = input("\nВведіть показники потужності (хв): ")
        power_data = [int(x) for x in user_input.split()]
        
        if len(power_data) < 3:
            print("Помилка: Недостатньо даних для аналізу (мінімум 3 значення).")
            return

        length, summit_min = longest_peak(power_data)

        if length > 0:
            print(f"\nРезультати аналізу тренування:")
            print(f"- Тривалість найдовшого циклу: {length} хв.")
            print(f"- Пік навантаження зафіксовано на: {summit_min + 1}-й хвилині.")
        else:
            print("\nУ цьому тренуванні не знайдено правильних пікових циклів.")
            
    except ValueError:
        print("Помилка: Вводьте лише цілі числа через пробіл.")

if __name__ == "__main__":
    analyze_training()