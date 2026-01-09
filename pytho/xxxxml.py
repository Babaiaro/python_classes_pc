import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("\n***** Movie *****")
            # Safely get the title attribute
            title = attributes.get("title", "Unknown Title")
            print("Title:", title)

    # Call when an element ends
    def endElement(self, tag):
        if tag == "type":
            print("Type:", self.type)
        elif tag == "format":
            print("Format:", self.format)
        elif tag == "year":
            print("Year:", self.year)
        elif tag == "rating":
            print("Rating:", self.rating)
        elif tag == "stars":
            print("Stars:", self.stars)
        elif tag == "description":
            print("Description:", self.description)
        # Reset current data to avoid capturing trailing whitespace
        self.CurrentData = ""

    # Call when character data is read
    def characters(self, content):
        # Only capture content if it matches one of our target tags
        if self.CurrentData == "type":
            self.type = content.strip()
        elif self.CurrentData == "format":
            self.format = content.strip()
        elif self.CurrentData == "year":
            self.year = content.strip()
        elif self.CurrentData == "rating":
            self.rating = content.strip()
        elif self.CurrentData == "stars":
            self.stars = content.strip()
        elif self.CurrentData == "description":
            self.description = content.strip()

if __name__ == "__main__":
    # 1. Create a SAX XMLReader object
    parser = xml.sax.make_parser()

    # 2. Turn off namespaces (standard for simple XML)
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 3. Override the default ContextHandler
    handler = MovieHandler()
    parser.setContentHandler(handler)

    # 4. FIX: Use a file object to prevent "unknown url type" errors
    file_path = "/home/bob/Documents/python_classes_pc/pytho/jan/xxxxml.xml"
    
    try:
        with open(file_path, "r") as xml_file:
            parser.parse(xml_file)
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
