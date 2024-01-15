#!/usr/bin/python3
''' Module for Base model Unittests

Unittest classes:
    TestBase_init
    TestBase_to_json_string
    TestBase_to_json_string_rectangle
    TestBase_to_json_string_square
    TestBase_save_to_file
    TestBase_from_json_string
    TestBase_from_json_string_rectangle
    TestBase_from_json_string_square
    TestBase_create_rectangle
    TestBase_create_square
    TestBase_load_from_file
    TestBase_save_to_csv
    TestBase_load_from_csv
'''
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    ''' Defines test cases for the base class '''

#  no id's given
    def test_id_not_given(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_not_given_multiple(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)

    def test_id_is_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

#  id's given
    def test_id_given(self):
        b1 = Base(20)
        self.assertEqual(b1.id, 20)

    def test_id_multiple(self):
        with self.assertRaises(TypeError):
            Base(6, 4)

    def test_id_infinity(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_id_neg_infinity(self):
        self.assertEqual(float('-inf'), Base(float('-inf')).id)

# mix of no id and id given
    def test_nb_instances_after_id_given(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        b4 = Base(76)
        b5 = Base()
        b6 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 76)
        self.assertEqual(b5.id, b2.id + 1)
        self.assertEqual(b6.id, b5.id + 1)

#  test whether id is public
    def test_id_is_public(self):
        b1 = Base(8)
        b1.id = 90
        self.assertEqual(90, b1.id)

# test whether nb_instances is private
    def test_nb_instances_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(23).__nb_instances)

# cases that should raise errors, unlikely cases where id is not an int
    def test_id_Nan(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

# test id is not type int
    def test_id_float(self):
        self.assertEqual(2.5, Base(2.5).id)

    def test_id_str(self):
        self.assertEqual('string', Base('string').id)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_set(self):
        self.assertEqual({"apple", "banana", "cherry"},
                         Base({"apple", "banana", "cherry"}).id)

    def test_id_frozenset(self):
        self.assertEqual(frozenset({"apple", "banana", "cherry"}),
                         Base(frozenset({"apple", "banana", "cherry"})).id)

    def test_id_list(self):
        self.assertEqual(["list", "list", "list"],
                         Base(["list", "list", "list"]).id)

    def test_id_tuple(self):
        self.assertEqual(("list", "list", "list"),
                         Base(("list", "list", "list")).id)

    def test_id_dict(self):
        self.assertEqual({"name": "John", "age": 36},
                         Base({"name": "John", "age": 36}).id)

    def test_id_range(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_id_complex(self):
        self.assertEqual(1j, Base(1j).id)

    def test_id_bytes(self):
        self.assertEqual(b"Hello", Base(b"Hello").id)

    def test_id_bytearray(self):
        self.assertEqual(bytearray(5), Base(bytearray(5)).id)

    def test_id_memoryview(self):
        self.assertEqual(memoryview(bytes(10)), Base(memoryview(bytes(10))).id)


class TestBase_to_json_string(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_none(self):
        self.assertEqual("null", Base.to_json_string(None))

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_to_json_string_rectangle(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_type_rectangle(self):
        rec1 = Rectangle(3, 5, 7, 9, 11)
        self.assertEqual(str,
                         type(Base.to_json_string([rec1.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)


class TestBase_to_json_string_square(unittest.TestCase):
    ''' Test for to_json_string '''
    def test_to_json_string_type_square(self):
        s = Square(5, 20, 15, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)


class TestBase_save_to_file(unittest.TestCase):
    ''' Testing save_to_file method of Base class '''

    @classmethod
    def tearDown(self):
        ''' Delete  files '''
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_rectangle_one(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_rectangles_two(self):
        rec1 = Rectangle(9, 4, 8, 8, 3)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) != 105)

    def test_save_to_file_square_one(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_squares_two(self):
        sq1 = Square(16, 12, 8, 4)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) != 77)

    def test_save_to_file_overwrite(self):
        sq = Square(11, 9, 7, 5)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    ''' Tests for from_json_string  '''
    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_type(self):
        list_of_inputs = [{"id": 54, "width": 24, "height": 5}]
        json_list_input = Rectangle.to_json_string(list_of_inputs)
        list_of_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_of_output))


class TestBase_from_json_string_rectangle(unittest.TestCase):
    ''' Tests for from_json_string  '''
    def test_from_json_string_one_rectangle(self):
        list_of_input = [{"id": 76, "width": 17, "height": 8, "x": 6}]
        json_list_input = Rectangle.to_json_string(list_of_input)
        list_of_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_of_input, list_of_output)

    def test_from_json_string_two_rectangles(self):
        list_of_input = [
            {"id": 32, "width": 4, "height": 7, "x": 4, "y": 2},
            {"id": 28, "width": 8, "height": 6, "x": 7, "y": 6},
        ]
        json_list_input = Rectangle.to_json_string(list_of_input)
        list_of_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_of_input, list_of_output)


class TestBase_from_json_string_square(unittest.TestCase):
    ''' Tests for from_json_string  '''
    def test_from_json_string_one_square(self):
        list_of_input = [{"id": 76, "size": 30, "height": 2}]
        json_list_input = Square.to_json_string(list_of_input)
        list_of_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_of_input, list_of_output)

    def test_from_json_string_two_squares(self):
        list_of_input = [
            {"id": 74, "size": 12, "height": 5},
            {"id": 9, "size": 4, "height": 5}
        ]
        json_list_input = Square.to_json_string(list_of_input)
        list_of_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_of_input, list_of_output)


class TestBase_create_rectangle(unittest.TestCase):
    '''Test for create method '''
    def test_create_rectangle_original(self):
        rec1 = Rectangle(3, 5, 1, 7, 8)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (8) 1/7 - 3/5", str(rec1))

    def test_create_rectangle_new(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec2))

    def test_create_rectangle_equals(self):
        rec1 = Rectangle(8, 3, 6, 5, 7)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)


class TestBase_create_square(unittest.TestCase):
    '''Test for create method '''
    def test_create_square_original(self):
        sq1 = Square(8, 2, 2, 4)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (4) 2/2 - 8", str(sq1))

    def test_create_square_new(self):
        sq1 = Square(8, 2, 2, 4)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (4) 2/2 - 8", str(sq2))

    def test_create_square_is(self):
        sq1 = Square(3, 4, 10, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_create_square_equals(self):
        sq1 = Square(3, 5, 2, 3)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    ''' test load_from_file_method '''

    @classmethod
    def tearDown(self):
        ''' Delete files '''
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rec1 = Rectangle(8, 4, 2, 7, 6)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rec1, rec2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_csv(unittest.TestCase):
    ''' Test save_to_file_csv method '''

    @classmethod
    def tearDown(self):
        ''' Delete files'''
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_csv_one_rectangle(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_csv_two_rectangles(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_csv_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_csv_two_squares(self):
        sq1 = Square(10, 7, 4, 9)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as f:
            self.assertTrue("9,10,7,4\n3,8,1,2", f.read())

    def test_save_to_csv_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(34, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,34,7,2", f.read())

    def test_save_to_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_csv_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_csv(unittest.TestCase):
    ''' Test load_from_file_csv method '''

    @classmethod
    def tearDown(self):
        ''' Delete files '''
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_csv_first_rectangle(self):
        rec1 = Rectangle(10, 11, 12, 18, 13)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(list_rectangles_output[0]))

    def test_load_from_csv_second_rectangle(self):
        rec1 = Rectangle(10, 9, 7, 3, 41)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(list_rectangles_output[1]))

    def test_load_from_csv_rectangle_types(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_csv_first_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_csv_second_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_csv_square_types(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
