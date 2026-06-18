import yaml
import xml.etree.ElementTree as xml_tree

with open('portfolio.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    # 1.Root
    feed_element = xml_tree.Element('feed', { 'xmlns': 'http://www.w3.org/2005/Atom' })

    # My Page
    link_prefix = yaml_data['link']

    # 2. METADATA - Root level
    xml_tree.SubElement(feed_element, 'title').text = yaml_data['title']
    xml_tree.SubElement(feed_element, 'subtitle').text = yaml_data['subtitle']
    xml_tree.SubElement(feed_element, 'author').text = yaml_data['author']
    
    # Logo of my Page
    xml_tree.SubElement(feed_element, 'logo').text = link_prefix + yaml_data['logo']
    
    # Link and its attributes: 
    """<link rel="enclosure" type="audio/mpeg" length="1337"
        href="http://example.org/audio/ph34r_my_podcast.mp3"/>"""
    xml_tree.SubElement(feed_element, 'link', { 'rel': 'self', 'href': link_prefix })

    # 3. Loop for Items (Entry-Level)
    for item in yaml_data['item']:
        # Individual (<entry>)
        entry_element = xml_tree.SubElement(feed_element, 'entry')
        
        # Basics of an item
        xml_tree.SubElement(entry_element, 'title').text = item['title']
        xml_tree.SubElement(entry_element, 'summary').text = item['description']
        xml_tree.SubElement(entry_element, 'updated').text = item['published']
        
        # --- Link 1: Main Document ---
        file_url = item['file']
        if file_url.startswith('/'):
            file_url = link_prefix + file_url
            
        xml_tree.SubElement(entry_element, 'link', {
            'rel': 'enclosure',
            'type': item.get('type', 'application/pdf'), # Si no se define tipo en el YAML, asume PDF
            'href': file_url
        })
        
        # --- Link 2: Previe if needed ---
        # check for 'preview_img' in the item
        if 'preview_img' in item:
            img_url = item['preview_img']
            if img_url.startswith('/'):
                img_url = link_prefix + img_url
                
            xml_tree.SubElement(entry_element, 'link', {
                'rel': 'enclosure',
                'type': 'image/png',
                'href': img_url
            })

    # 4. Output
    output_tree = xml_tree.ElementTree(feed_element)
    output_tree.write('portfolio.xml', encoding='UTF-8', xml_declaration=True)
