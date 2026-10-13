from tafsiri_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_luo_population_is_the_2019_census_figure_and_the_fourth_largest():
    text = str(_fn("luo_language_guide")(None))
    assert "5.07" in text and "fourth" in text and "third largest" not in text
