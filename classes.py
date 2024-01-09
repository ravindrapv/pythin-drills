import math

class Point:
    def __init__(self, x, y):
        """
        Initialize the Point object with x and y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self, other_point):
        """
        Calculate and return the distance between two points.
        """
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

# Example usage:
point1 = Point(1, 2)
point2 = Point(4, 6)

distance_between_points = point1.distance(point2)
print(f"The distance between point1 and point2 is: {distance_between_points}")