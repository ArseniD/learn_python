import unittest
import pytest

from glided_rose import Item, GlidedRose


examples = (("item_name", "initial_quality", "initial_sellin",
             "updated_quality", "updated_sellin", "comment"),
            (
              ("foo", 0, 0, 0, -1, "typical item"),
              ("foo", 2, -2, 0, -3, "typical item"),
              ("Sulfuras, Hand of Ragnaros", 24, 3, 24, 3, "exceptional item"),
              ("Sulfuras, Hand of Ragnaros", 2, -3, 2, -3, "exceptional item"),
              ("Aged Brie", 0, 0, 2, -1, "brie item"),
              ("Aged Brie", 50, -3, 50, -4, "brie item"),
              ("Backstage passes", 0, 0, 0, -1, "backstage pass item"),
              ("Backstage passes", 20, 12, 21, 11, "backstage pass item"),
              ("Backstage passes", 49, 10, 50, 9, "backstage pass item"),
              ("Backstage passes", 49, 5, 50, 4, "backstage pass item"),
              ("Backstage passes", 51, 5, 51, 4, "backstage pass item"),
            ))


@pytest.mark.parametrize(*examples)
def test_update_quality(item_name, initial_quality, initial_sellin,
                        updated_quality, updated_sellin, comment):

    item = Item(item_name, initial_sellin, initial_quality)
    glided_rose = GlidedRose([item])

    assert str(item) == f'{item_name}, {initial_sellin}, {initial_quality}'

    glided_rose.update_quality()

    assert item.quality == updated_quality
    assert item.sell_in == updated_sellin

# def test_foo():
#     item = Item("foo", 0, 0)
#     glided_rose = GlidedRose([item])
#     glided_rose.update_quality()
#     assert item.quality == -1
#     assert item.sell_in == -1

# def test_sulfuras():
#     item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
#     glided_rose = GlidedRose([item])
#     glided_rose.update_quality()
#     assert item.quality == 0
#     assert item.sell_in == 0
