"""Simple demo primarily for verifying the development environment."""
from gears import core
from gears import draw


def main():
    node = draw.primitives.Triangle((200, 200), (100, 400))
    node = draw.transforms.SkewX(node, -10)
    # also we should try to see if triangle works when we
    # put the vertices in clockwise order (instead of
    # anticlockwise)
    node2 = draw.primitives.Triangle((200, 200), (100, 400))
    # verify that we can translate twice
    node2 = draw.transforms.Translation(node2, 250, 0)
    node3 = draw.primitives.Triangle((200, 200), (100, 400))
    node3 = node2 = draw.transforms.Translation(node2, 500, 0)
    #node2 = draw.transforms.Translation(node2, 0, 200)
    app = core.Application([])
    app.window.attach_node(node)
    app.window.attach_node(node2)
    app.window.resize(1024, 768)
    app.run()


if __name__ == '__main__':
    main()
