"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730621513"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Calculates distance between two points."""
        dist: float
        dist = (sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None:
        """Keeps track of ticks."""
        self.location = self.location.add(self.direction)
        if self.is_infected() and self.sickness < constants.RECOVERY_PERIOD:
            self.sickness += 1
        elif self.is_infected():
            self.immunize()

    def contract_disease(self) -> None:
        """Sets sickness to infected status."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Sets a bool dependent on infection status."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Sets a bool dependent on infection status."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
        
    def color(self) -> str:
        """Determines color of cell based on infection status."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "red"
        else:
            return "black"

    def contact_with(self, other: Cell) -> None:
        """Makes cell contract disease if contact with other infected cell."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Immune function."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Sets a bool dependent on infection status."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
        

class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells < 1 or infected_cells >= cells:
            raise ValueError("Number of infected cells not within permitted parameters.")
        if immune_cells < 0 or immune_cells >= cells:
            raise ValueError("Number of immune cells cells not within permitted parameters")
        i: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected_cells:
                cell.contract_disease()
            elif i >= infected_cells and i < infected_cells + immune_cells:
                cell.immunize()
            i += 1
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
        self.time += 1

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X or cell.location.x < constants.MIN_X:
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y or cell.location.y < constants.MIN_Y:
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks to see if cells come into contact."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                first_cell: Cell = self.population[i]
                second_cell: Cell = self.population[j]
                distance_cells: float = first_cell.location.distance(second_cell.location)
                if distance_cells < constants.CELL_RADIUS:
                    first_cell.contact_with(second_cell)
                j += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True