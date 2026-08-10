from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста: УДАЛЕН, так как тестирует несуществующий метод
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
     #   collector = BooksCollector()

        # добавляем две книги
      #  collector.add_new_book('Гордость и предубеждение и зомби')
       # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
       # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
        def test_add_new_book_add_one_book_check_name_is_equal(self):
    
            collector = BooksCollector()
            collector.add_new_book('Задача трёх тел')
      
            assert 'Задача трёх тел' in collector.books_genre

        def test_add_new_book_add_two_books_two_books_added(self):
      
            collector = BooksCollector()
            collector.add_new_book('Задача трёх тел')
            collector.add_new_book('Темный лес')
            collector.add_new_book('Вечная жизнь смерти')

            assert len(collector.books_genre) == 3

        def test_set_book_genre_genre_from_list_genre_set(self):

            collector = BooksCollector()
            book_name = 'Задача трёх тел'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Фантастика')

            assert collector.books_genre[book_name] == 'Фантастика'


        def test_set_book_genre_genre_not_from_list_genre_is_empty(self):

            collector = BooksCollector()
            book_name = 'Задача трёх тел'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Научная фантастика')

            assert collector.books_genre[book_name] == ''

        def test_get_book_genre_existing_book_genre_is_equal(self):

            collector = BooksCollector()
            book_name = 'Задача трёх тел'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Фантастика')

            assert collector.get_book_genre(book_name) == 'Фантастика'