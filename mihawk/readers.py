from xml.dom import minidom

from mihawk import Point


class KMLReader:
    def __init__(self, filename: str):
        self.filename = filename

        with open(filename) as file:
            dom = minidom.parse(file)

        coordinates = dom.getElementsByTagName("coordinates")

        coords = []
        for coord in coordinates:
            text = coord.firstChild.nodeValue
            values = self._clean_coords(text)
            coords.append(values)

    def _clean_coords(self, text: str) -> list:
        """Clean coordinates from KML file."""

        coordinates = text.split(",")
        cleaned = (float(coord) for coord in coordinates)
        return Point(*cleaned)
