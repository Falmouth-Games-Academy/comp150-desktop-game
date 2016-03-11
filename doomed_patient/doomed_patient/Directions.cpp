#include "stdafx.h"
#include "Directions.h"
#include "GridCoordinate.h"

Directions::Directions()
{
}


Directions::~Directions()
{
}

GridCoordinate Directions::getDirectionVector(Direction direction)
{
	switch (direction)
	{
	case Directions::Direction::NORTH:
		return GridCoordinate(0, -1);
	case Directions::Direction::EAST:
		return GridCoordinate(1, 0);
	case Directions::Direction::SOUTH:
		return GridCoordinate(0, 1);
	case Directions::Direction::WEST:
		return GridCoordinate(-1, 0);
	}
}


Directions::Direction Directions::getOpposite(Direction direction)
{
	switch (direction)
	{
	case Direction::NORTH:
		return Direction::SOUTH;
	case Direction::SOUTH:
		return Direction::NORTH;
	case Direction::EAST:
		return Direction::WEST;
	case Direction::WEST:
		return Direction::EAST;
	}
}
