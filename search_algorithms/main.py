import timeit
from pathlib import Path
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def measure(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)

def main():
    pattern_1 = "Також, у теорії алгоритмів жадібні алгоритми відіграють важливу роль. Вони прості для розуміння та реалізації, працюють порівняно швидко, відомо багато різноманітних задач, які можна вирішити за допомогою таких алгоритмів"
    pattern_2 = "Постановка проблеми. Рекомендаційні системи є важливою складовою соціальних мереж та значним чином впливають на те, яким користувачі сприймають інформаційний простір"
    pattern_3 = "Постановка проблеми. Рекомендаційні системи є важливою складовою соціальних мереж та значним чином впливають на те, яким користувачі сприймають інформаційний простір"
    pattern_4 = "Також, у теорії алгоритмів жадібні алгоритми відіграють важливу роль. Вони прості для розуміння та реалізації, працюють порівняно швидко, відомо багато різноманітних задач, які можна вирішити за допомогою таких алгоритмів "

    file_path_article_1 = Path(__file__).parent / "texts" / "article_1.txt"
    file_path_article_2 = Path(__file__).parent / "texts" / "article_2.txt"
    
    
    with open(file_path_article_1, "r", encoding="cp1251") as file:
        file_content_1 = file.read()
    
    with open(file_path_article_2, "r", encoding="utf-8") as file:
        file_content_2 = file.read()
    
    print("\nTesting on Article 1 (Real pattern):")
    print("Boyer-Moore:", measure(boyer_moore_search, file_content_1, pattern_1))
    print("KMP:        ", measure(kmp_search, file_content_1, pattern_1))
    print("Rabin-Karp: ", measure(rabin_karp_search, file_content_1, pattern_1))
    print("\nTesting on Article 1 (Fake pattern):")
    print("Boyer-Moore:", measure(boyer_moore_search, file_content_1, pattern_3))
    print("KMP:        ", measure(kmp_search, file_content_1, pattern_1))
    print("Rabin-Karp: ", measure(rabin_karp_search, file_content_1, pattern_3))
    print("\nTesting on Article 2 (Real pattern):")
    print("Boyer-Moore:", measure(boyer_moore_search, file_content_2, pattern_2))
    print("KMP:        ", measure(kmp_search, file_content_2, pattern_2))
    print("Rabin-Karp: ", measure(rabin_karp_search, file_content_2, pattern_2))
    print("\nTesting on Article 2 (Fake pattern):")
    print("Boyer-Moore:", measure(boyer_moore_search, file_content_2, pattern_4))
    print("KMP:        ", measure(kmp_search, file_content_2, pattern_2))
    print("Rabin-Karp: ", measure(rabin_karp_search, file_content_2, pattern_4), "\n")


if __name__ == "__main__":
    main()
