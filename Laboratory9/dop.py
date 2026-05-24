import os

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read().replace('\n', '').replace(' ', '').upper()
    except FileNotFoundError:
        return None

def analyze_plagiarism(reference_file, fragment_files):
    reference_data = read_file_content(reference_file)
    if not reference_data:
        return "Помилка: Еталонний файл не знайдено=(", 0

    total_fragments = len(fragment_files)
    found_count = 0
    search_results = {}

    for frag_file in fragment_files:
        fragment_data = read_file_content(frag_file)
        
        if not fragment_data:
            continue

        if fragment_data in reference_data:
            search_results[frag_file] = True
            found_count += 1
        else:
            search_results[frag_file] = False

    plagiarism_percentage = (found_count / total_fragments) * 100 if total_fragments > 0 else 0

    return search_results, plagiarism_percentage

if __name__ == "__main__":
    reference_path = 'reference.txt'
    
    fragments_paths = [
        'fragment_1.txt',
        'fragment_2.txt',
        'fragment_3.txt',
        'fragment_4.txt',
        'fragment_5.txt'
    ]

    results, percentage = analyze_plagiarism(reference_path, fragments_paths)

    if isinstance(results, dict):
        print("Плагіат знайдено у файлах:")
        for file, is_found in results.items():
            if is_found:
                print(f" {file}")
        
        print(f"Рівень плагіату: {percentage}%")
    else:
        print(results)