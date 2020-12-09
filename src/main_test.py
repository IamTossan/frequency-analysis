from main import char_rot, str_rot

class TestCharRot:
    def test_one_char(self):
        assert char_rot('a', 1) == 'b'

    def test_non_alpha_char(self):
        assert char_rot('/', 1) == '/'

    def test_one_char_edge_case(self):
        assert char_rot('z', 1) == 'a'

    def test_one_char_random_rot_value(self):
        assert char_rot('w', 5) == 'b'

class TetsStringRot:
    def test_string(self):
        assert str_rot('lolilol', 3) == 'oroloro'
