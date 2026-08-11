from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
       
        @pytest.mark.parametrize("book_name, is_valid", 
                                 [('Задача трёх тел', True), 
                                  ('Похождения бравого солдата Швейка во время мировой войны', False)])
        def test_add_new_book_add_two_books_check_if_name_valid(self, book_name, is_valid):
            collector = BooksCollector()
            collector.add_new_book(book_name)     
            result = book_name in collector.books_genre
            assert result == is_valid

        def test_add_new_book_add_book_twice_book_not_added(self):
      
            collector = BooksCollector()
            collector.add_new_book('Задача трёх тел')
            collector.add_new_book('Темный лес')
            collector.add_new_book('Вечная жизнь смерти')
            collector.add_new_book('Задача трёх тел')

            assert len(collector.books_genre) == 3

        @pytest.mark.parametrize("input_genre, expected_result", [('Фантастика', 'Фантастика'), ('Научная фантастика', '')])
        def test_set_book_genre_validate_genre (self, input_genre, expected_result):
            collector = BooksCollector()
            book_name = 'Задача трёх тел'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, input_genre)

            assert collector.get_book_genre(book_name) == expected_result

        def test_get_books_with_specific_genre_filtered_names_returned (self):
            collector = BooksCollector()
            book1 = 'Задача трёх тел'
            book2 = 'Десять негритят'
            book3 = 'Тёмный лес'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_new_book(book2)
            collector.set_book_genre(book2, 'Детективы')
            collector.add_new_book(book3)
            collector.set_book_genre(book3, 'Фантастика')
            assert collector.get_books_with_specific_genre('Фантастика') == [book1,book3]

        def test_get_books_genre_full_dictionary_returned(self):
            collector = BooksCollector()
            book1 = 'Задача трёх тел'
            book2 = 'Десять негритят'
            book3 = 'Тёмный лес'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_new_book(book2)
            collector.set_book_genre(book2, 'Детективы')
            collector.add_new_book(book3)
            collector.set_book_genre(book3, 'Фантастика')
            expected_result = {'Задача трёх тел': 'Фантастика', 'Десять негритят': 'Детективы', 'Тёмный лес': 'Фантастика'}
            assert collector.get_books_genre() == expected_result

        def test_get_books_for_children_filtered_out_rated_and_unknown(self):
            collector = BooksCollector()
            book1 = 'Задача трёх тел'
            book2 = 'Десять негритят'
            book3 = 'Куджо'
            book4 = 'Король-Лев'
            book5 = 'Просто книга'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_new_book(book2)
            collector.set_book_genre(book2, 'Детективы')
            collector.add_new_book(book3)
            collector.set_book_genre(book3, 'Ужасы')
            collector.add_new_book(book4)
            collector.set_book_genre(book4, 'Мультфильмы')
            collector.add_new_book(book5)            
            collector.set_book_genre(book5, 'Несуществующий жанр')
            expected_result = ['Задача трёх тел','Король-Лев']
            assert collector.get_books_for_children() == expected_result

        def test_add_book_in_favorites_only_allowed_book_added(self):
            collector = BooksCollector()
            book1 = 'Задача трёх тел'
            book2 = 'Книга не для коллекции'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_book_in_favorites(book1)
            collector.add_book_in_favorites(book1)
            collector.add_book_in_favorites(book2)
            assert collector.get_list_of_favorites_books() == [book1] 

        def test_delete_book_from_favorites_book_deleted(self):
            collector = BooksCollector()    
            book1 = 'Задача трёх тел'
            book2 = 'Десять негритят'
            book3 = 'Бульварное чтиво'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_book_in_favorites(book1)
            collector.add_new_book(book2)
            collector.set_book_genre(book2, 'Детективы')
            collector.add_book_in_favorites(book2)
            collector.delete_book_from_favorites (book1)
            collector.delete_book_from_favorites (book3)
            assert collector.get_list_of_favorites_books() == [book2]


        def test_get_book_genre_genre_returned(self):
            collector = BooksCollector()
            book_name = 'Трое в лодке...'
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Комедии')
            assert collector.get_book_genre(book_name) == 'Комедии'

        def test_get_list_of_favorites_books_favorites_returned(self):
            collector = BooksCollector()    
            book1 = 'Задача трёх тел'
            book2 = 'Десять негритят'
            book3 = 'Трое в лодке...'
            book4 = 'Король-Лев'
            collector.add_new_book(book1)
            collector.set_book_genre(book1, 'Фантастика')
            collector.add_book_in_favorites(book1)
            collector.add_new_book(book2)
            collector.set_book_genre(book2, 'Детективы')
            collector.add_new_book(book3)
            collector.set_book_genre(book3, 'Комедии')
            collector.add_book_in_favorites(book3)
            collector.add_new_book(book4)
            collector.set_book_genre(book4, 'Мультфильмы')
            assert collector.get_list_of_favorites_books() == [book1,book3]
