import pytest

# functions to test
from project import generate_maze, draw_map, get_instructions, walk
# supporting functions
from project import reset_skin, add_walls, add_undefind_tiles, create_entrance, create_finish

dimension = 5
reset_skin()

MAZE = [["🌳","🌳","🌳","🐕","🌳"],
        ["🌳","🟫","🟫","🟫","🌳"],
        ["🌳","🌳","🌳","🟫","🌳"],
        ["🌳","🟫","🟫","🟫","🌳"],
        ["🌳","🏁","🌳","🌳","🌳"]]



def test_generate_maze():
    maze, entrance, finish = generate_maze(dimension)

    assert len(maze) == dimension
    assert len(maze[0]) == dimension

    assert str(type(entrance)) == "<class 'tuple'>"
    assert str(type(finish)) == "<class 'tuple'>"

    assert len(entrance) == 2
    assert len(finish) == 2

    assert entrance[0] == 0
    assert entrance[1] in range(1,dimension-1)

    assert finish[0] == dimension-1
    assert finish[1] in range(1,dimension-1)



def test_draw_map():
    mz_str = "🌳🌳🌳🐕🌳\n🌳🟫🟫🟫🌳\n🌳🌳🌳🟫🌳\n🌳🟫🟫🟫🌳\n🌳🏁🌳🌳🌳"

    assert draw_map(MAZE) == mz_str

    assert draw_map([]) == ""

    with pytest.raises(TypeError):
        assert draw_map() == mz_str
    


def test_get_instructions():
    file = "instructions.txt"
    file2 = "non-existatnt.txt"

    instr_str = "\n*** Instructions ***\n- Type <direction> <number of tiles> to move up, down, left or right.\n  For example, 'left 2' means you'll move two tiles to the left.\n  If you don't type a number, you'll move 1 tile.\n- Type 'map' to see the maze with your currect location.\n- Type 'help' to see the instructions again.\n- Type 'exit' to give up.\n"
    not_found = "\nInstructions are not found\n"

    assert get_instructions(file) == instr_str

    with pytest.raises(TypeError):
        assert get_instructions() == instr_str

    assert get_instructions(file2) == not_found

