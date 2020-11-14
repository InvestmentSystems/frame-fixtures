
import numpy as np #type: ignore
# import static_frame as sf #type: ignore
from frame_fixtures.frame_fixtures import Fixture
from frame_fixtures.frame_fixtures import SourceValues



def test_parser_a() -> None:

    msg = 'f(Fg)|i(I,str)|c(IDg,dtD)|v(float)'
    msg = 'f(F)|i((I,I),(str,bool))|c((IN,I),(dtns,int))|v(str,bool,object)|s(10,10)'

    f1 = Fixture.to_frame(msg)


def test_source_values_a() -> None:

    post = SourceValues.get_ints()
    assert len(post) == SourceValues.MAX_SIZE
    # assert post[:3].tolist() == [845545, 563150, 468891]
    # import ipdb; ipdb.set_trace()

def test_source_values_b() -> None:

    post = SourceValues.get_chars()
    assert len(post) == SourceValues.MAX_SIZE
    assert post[:3].tolist() == ['fa14b27e5f09', 'ebbc39aaf008', '04e42a6ee7a9']
    # import ipdb; ipdb.set_trace()


def test_source_valuies_dtype_to_element_iter_a() -> None:

    for dtype in (
            np.dtype('i'),
            np.dtype('u8'),
            np.dtype('f8'),
            np.dtype('c16'),
            np.dtype('?'),
            ):
        gen = SourceValues.dtype_to_element_iter(dtype)
        print(dtype)
        for i in range(5):
            print(next(gen))

if __name__ == '__main__':
    test_parser_a()







