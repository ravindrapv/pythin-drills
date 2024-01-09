def html_dict_search(html_dict, selector):
    """
    Implement `id` and `class` selectors

    Parameters:
    - html_dict: Dictionary representing the HTML structure
    - selector: Selector string, either an ID or a class name

    Returns:
    - List of elements matching the selector
    """
    selected_elements = []

    for tag, attributes in html_dict.items():
       
        if 'id' in attributes and attributes['id'] == selector:
            selected_elements.append((tag, attributes))

    
        if 'class' in attributes and selector in attributes['class']:
            selected_elements.append((tag, attributes))

    return selected_elements


sample_html_dict = {
    'div1': {'id': 'content', 'class': ['section', 'main']},
    'p1': {'class': ['paragraph']},
    'a1': {'id': 'link1', 'class': ['menu', 'link']}
}

id_selector_result = html_dict_search(sample_html_dict, 'content')
print("Elements with id 'content':", id_selector_result)

class_selector_result = html_dict_search(sample_html_dict, 'link')
print("Elements with class 'link':", class_selector_result)