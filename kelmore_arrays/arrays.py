from typing import List, TypeVar, Any, Union, Optional, Iterable, Tuple, Set, Type

GenT = TypeVar('GenT')
Matrix = List[List[Any]]
Point = Tuple[int, int]
UniqueResp = Union[List[Any], Set[Any]]


class ArrayCheck:

    @staticmethod
    def all_none(*args: Any) -> bool:
        # Checks an array and returns True if all the items are None
        all_none: bool = True
        for item in args:
            all_none = all_none and item is None

        return all_none

    @staticmethod
    def all_not_null(*args: Any) -> bool:
        all_not_none: bool = True
        for item in args:
            all_not_none = all_not_none and item is not None
            if not all_not_none:
                break

        return all_not_none

    @staticmethod
    def any_none(*args: Any) -> bool:
        """
        Checks an array and returns True if any of the values are none, else returns False
        :return: True if array contains a None value, False otherwise
        """
        for item in args:
            if item is None or item == '':
                return True

        return False

    @staticmethod
    def contains_all(array: Iterable[str], check: Iterable[str]) -> bool:
        for item in array:
            if item not in check:
                return False

        return True

    @staticmethod
    def equal_length(list_a: List[Any],
                     list_b: List[Any],
                     raise_error: Optional[bool] = False) -> bool:
        if len(list_a) == len(list_b):
            return True

        if raise_error:
            raise ValueError('The passed arrays were not of equal length')

        return False


class Matrices:

    @staticmethod
    def column(array: Matrix, col: int) -> List[Any]:
        output: List[Any] = []
        for row in array:
            if len(row) > col:
                output.append(row[col])
            else:
                output.append(None)

        return output

    @staticmethod
    def to_json(array: List[List[Any]],
                headers: Optional[List[str]] = None) -> List[dict]:
        output: List[dict] = []
        if not array:
            return output

        headers = array.pop(0) if headers is None else headers
        headers = [str(x) for x in headers]
        for row in array:
            new_json: dict = {}
            for header_idx, header in enumerate(headers):
                if header_idx < len(row):
                    new_json[header] = row[header_idx]
            output.append(new_json)
        return output

    @staticmethod
    def value(array: Matrix, point: Point) -> Any:
        """
        Gets the value from a 2D array using the given point
        :param array: The lookup array
        :param point: The point of the value - defined as (y, x) or (row, col)
        :return: The value
        """
        pos_x = point[0]
        pos_y = point[1]

        datum = None
        if pos_y < len(array):
            row = array[pos_y]
            if pos_x < len(row):
                datum = row[pos_x]

        return datum


class ArrayTransform:

    @staticmethod
    def chunk(array: List[Any], chunk_size: int) -> List[List[Any]]:
        output: List[List[Any]] = []
        idx = 0
        while idx < len(array):
            new_array: List[Any] = []
            while idx < len(array) and len(new_array) < chunk_size:
                new_array.append(array[idx])
                idx += 1

            output.append(new_array)

        return output

    @staticmethod
    def complement(array: Iterable[Any],
                   check_array: Iterable[Any]) -> UniqueResp:
        output: List[Any] = []
        for item in array:
            if item not in check_array:
                output.append(item)

        return output

    @staticmethod
    def diff(array_one: List[Any], array_two: List[Any]) -> List[Any]:
        output: List[Any] = []
        for item in array_one:
            if item not in array_two:
                output.append(item)

        for item in array_two:
            if item not in output and item not in array_one:
                output.append(item)

        return output

    @staticmethod
    def delistify(item: Any, force_first: bool = False):
        if isinstance(item, list):
            if not item:
                return None
            if len(item) == 1:
                return item[0]
            if force_first:
                return item[0]

            return item

        return item

    @staticmethod
    def listify(item: Any):
        if item is None:
            return []

        if not isinstance(item, list) and not isinstance(item, set):
            return [item]

        return item

    @staticmethod
    def force_equal(list_a: List[Any], list_b: List[Any]) -> None:
        while len(list_a) > len(list_b):
            list_a.pop()

        while len(list_b) > len(list_a):
            list_b.pop()

    @staticmethod
    def merge(source: List[Any], dest: List[Any]) -> List[Any]:
        for item in source:
            if item not in dest:
                dest.append(item)

        return dest

    @staticmethod
    def remove_indexes(array: List[GenT], remove_indexes: List[int]) -> List[GenT]:
        remove_indexes.sort()

        count: int = 0
        for idx in remove_indexes:
            del array[idx - count]
            count += 1

        return array

    @staticmethod
    def remove_items(array: List[Any], removal: List[Any]) -> List[Any]:
        for remove in removal:
            if remove in array:
                array.remove(remove)

        return array

    @staticmethod
    def remove_null(array: List[GenT]) -> List[GenT]:
        array = [] if array is None else array
        return [x for x in array if x is not None]

    @staticmethod
    def remove_none(array: List[GenT]) -> List[GenT]:
        return [x for x in array if x is not None]

    @staticmethod
    def reverse(array: List[Any]) -> List[Any]:
        """ prec: s is a list
            postc: returns the reversed list s"""
        return array[::-1]

    @staticmethod
    def swap(array: List[Any], index_one: int, index_two: int) -> List[Any]:
        """ prec: array is a list, index_one and index_two are numbers less than length of array
            postc: swaps the two indexes in the array"""
        temp: Any = array[index_one]

        array[index_one] = array[index_two]
        array[index_two] = temp

        return array

    @staticmethod
    def unique(array: List[GenT]) -> List[GenT]:
        return [] if array is None else list(set(array))


class ArrayTools:
    check: Type[ArrayCheck] = ArrayCheck
    matrices: Type[Matrices] = Matrices
    transform: Type[ArrayTransform] = ArrayTransform

    @staticmethod
    def first(array: Union[List[GenT], GenT]) -> Union[GenT, None]:
        if isinstance(array, list):
            if not array:
                return None

            return array[0]

        return array

    @staticmethod
    def index(array: List[Any], query: Any) -> int:
        """ prec: array is a list, query is a string
            postc: returns the index of the query in the list, or -1 if it is not found"""

        try:
            return array.index(query)
        except ValueError:
            return -1
