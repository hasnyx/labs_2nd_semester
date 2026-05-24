import os

def solve_wchain(words: list[str]) -> int:
    """Знаходить довжину максимального ланцюжка слів (використовуючи Bucket Sort)."""
    if not words:
        return 0
        
    unique_words = set(words)
    
    max_len = max(len(w) for w in unique_words)
    
    buckets = [[] for _ in range(max_len + 1)]
    for word in unique_words:
        buckets[len(word)].append(word)
        
    dp = {}
    max_chain_length = 0
    
    for length in range(1, max_len + 1):
        if not buckets[length]:  
            continue
            
        has_shorter_words = bool(buckets[length - 1]) if length > 1 else False
        
        for word in buckets[length]:
            current_max = 1
            
            if has_shorter_words:
                for i in range(length):
                    prev_word = word[:i] + word[i+1:]
                    if prev_word in dp:
                        current_max = max(current_max, dp[prev_word] + 1)
            
            dp[word] = current_max
            if current_max > max_chain_length:
                max_chain_length = current_max
                
    return max_chain_length

def main():
    input_filename = "wchain.in"
    output_filename = "wchain.out"

    try:
        if not os.path.exists(input_filename):
            print(f"Помилка: Файл {input_filename} не знайдено!")
            return

        with open(input_filename, "r") as f:
            lines = f.read().splitlines()
            if not lines:
                print("Файл wchain.in порожній.")
                return
            
            try:
                n = int(lines[0].strip())
                words = [line.strip() for line in lines[1:n+1]]
            except (ValueError, IndexError):
                print("Помилка: Неправильний формат даних у файлі.")
                return

        print("\n" + "-"*30)
        print("ВХІДНІ ДАНІ (з wchain.in):")
        print(f"Кількість слів: {n}")
        print("-" * 30)

        result = solve_wchain(words)
        
        with open(output_filename, "w") as f:
            f.write(str(result) + "\n")
            
        print("РЕЗУЛЬТАТ (записано в wchain.out):")
        print(f"Максимальний ланцюжок: {result}")
        print("-"*30 + "\n")
            
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

if __name__ == "__main__":
    main()