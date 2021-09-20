import math
from clean_api_powerpoint_11 import Slide, Slides, load_slides


def test_slide_all_content_shown():
    content="""All
    Lines
    Show
    """
    slide = Slide(content)
    assert str(slide) == content

def test_slide_rows():
    content='\n'.join(['one', 'two'])
    slide = Slide(content)
    slide.row = 2
    assert str(slide) == content
    slide.row = 1
    assert str(slide) == 'one'
    slide.row = 0
    assert str(slide) == 'one'
    slide.row = -1
    assert str(slide) == 'one'

def test_slide_empty():
    slide = Slide('')
    assert str(slide) == ''

def test_slides_simple():
    slides = Slides([content for content in ['one slide']])
    assert str(slides.current) == 'one slide'
    assert slides.page == 1
    slides.page += 1
    slides.page += 3
    assert slides.page == 1
    slides.page -= 1
    slides.page -= math.inf
    assert slides.page == 1

def test_slides_multiple():
    slides = Slides([content for content in ['home', 'middle', 'end']])
    
    slides.page += math.inf
    assert slides.page == 3
    assert str(slides.current) == 'end'
    
    slides.page -= 100
    assert slides.page == 1
    assert str(slides.current) == 'home'
    
    slides.page += 1
    assert str(slides.current) == 'middle'
    
