def build_xml_element(tag, content, **attributes):
    attrs = ' '.join(f'{key}="{value.strip()}"' for key, value in attributes.items())
    if attrs:
        opening_tag = f"<{tag} {attrs}>"
    else:
        opening_tag = f"<{tag}>"

    closing_tag = f"</{tag}>"

    return f"{opening_tag} {content} {closing_tag}"

result = build_xml_element("a", "Hello there", href=" https://python.org ", _class=" my-link ", id=" someid ")
print(result)
